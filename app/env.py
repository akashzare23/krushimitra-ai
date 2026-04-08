import random
from app.models import FarmState, AgentAction, StepResponse


class KrushiMitraEnv:
    def __init__(self, task_name="crop_selection"):
        self.task_name = task_name
        self.state_data = None
        self.done = False

    def reset(self):
        self.done = False

        self.state_data = FarmState(
            day=1,
            season="kharif",
            soil_type=random.choice(["loamy", "sandy", "clay"]),
            soil_moisture=random.uniform(30, 60),
            temperature=random.uniform(28, 38),
            humidity=random.uniform(40, 80),
            rain_forecast_3d=random.uniform(0, 1),
            rain_forecast_7d=random.uniform(0, 1),
            tank_level=random.uniform(40, 100),
            water_availability=random.choice(["low", "medium", "high"]),
            crop_stage="pre_sowing",
            selected_crop=None,
            crop_health=50.0
        )
        return self.state_data

    def state(self):
        return self.state_data

    def step(self, action: AgentAction):
        reward = 0.0
        info = {}

        if self.task_name == "crop_selection":
            reward, info = self.handle_crop_selection(action)
            self.done = True

        elif self.task_name == "sowing_timing":
            reward, info = self.handle_sowing_timing(action)
            self.done = True

        elif self.task_name == "irrigation":
            reward, info = self.handle_irrigation(action)
            self.state_data.day += 1
            if self.state_data.day >= 7:
                self.done = True

        return StepResponse(
            state=self.state_data,
            reward=round(reward, 2),
            done=self.done,
            info=info
        )

    def handle_crop_selection(self, action: AgentAction):
        crop = (action.crop_choice or "").lower()

        good_crops = []

        if self.state_data.rain_forecast_7d < 0.4 and self.state_data.tank_level < 60:
            good_crops = ["bajra", "jowar", "tur"]

        elif self.state_data.rain_forecast_7d >= 0.4 and self.state_data.soil_type == "clay":
            good_crops = ["rice", "soybean"]

        else:
            good_crops = ["cotton", "soybean", "wheat"]

        self.state_data.selected_crop = crop

        if crop in good_crops:
            return 1.0, {"message": "Good crop selected"}
        else:
            return 0.2, {"message": f"Better options were: {good_crops}"}

    def handle_sowing_timing(self, action: AgentAction):
        sow_now = action.sow_now

        if sow_now is None:
            return 0.0, {"message": "Invalid action"}

        if self.state_data.rain_forecast_3d > 0.5 and self.state_data.soil_moisture >= 40:
            if sow_now:
                self.state_data.crop_stage = "sown"
                return 1.0, {"message": "Perfect sowing time"}
            else:
                return 0.3, {"message": "You should have sown now"}

        else:
            if sow_now:
                return 0.2, {"message": "Poor sowing timing"}
            else:
                return 1.0, {"message": "Good decision to wait"}

    def handle_irrigation(self, action: AgentAction):
        irrigate = action.irrigate
        water_amount = action.water_amount or 0.0

        if not irrigate:
            water_amount = 0.0

        self.state_data.tank_level -= water_amount
        self.state_data.soil_moisture += water_amount * 2
        self.state_data.soil_moisture -= self.state_data.temperature * 0.1

        if self.state_data.rain_forecast_3d > 0.7:
            self.state_data.soil_moisture += 5

        self.state_data.soil_moisture = max(0, min(100, self.state_data.soil_moisture))
        self.state_data.tank_level = max(0, self.state_data.tank_level)

        reward = 0.0

        if 45 <= self.state_data.soil_moisture <= 65:
            reward += 0.5
            self.state_data.crop_health += 5
        elif self.state_data.soil_moisture < 35:
            reward -= 0.2
            self.state_data.crop_health -= 5
        elif self.state_data.soil_moisture > 75:
            reward -= 0.2
            self.state_data.crop_health -= 3

        if water_amount <= 4:
            reward += 0.2
        else:
            reward -= 0.1

        if self.state_data.tank_level <= 10:
            reward -= 0.1

        self.state_data.crop_health = max(0, min(100, self.state_data.crop_health))

        return reward, {"message": "Irrigation step completed"}