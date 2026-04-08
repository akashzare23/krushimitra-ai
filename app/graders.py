def grade_crop_selection(response):
    return response.reward


def grade_sowing(response):
    return response.reward


def grade_irrigation(final_state):
    score = 0.0

    if 45 <= final_state.soil_moisture <= 65:
        score += 0.4

    if final_state.crop_health >= 70:
        score += 0.4

    if final_state.tank_level >= 10:
        score += 0.2

    return min(score, 1.0)