# KrushiMitra AI 🌾

## Climate-Adaptive Farming Decision Environment

KrushiMitra AI is a real-world OpenEnv environment designed to help AI agents learn smart farming decisions under changing climate conditions.

This environment simulates realistic agricultural scenarios where an AI agent must decide:

- Which crop to grow
- When to sow
- When and how much to irrigate

---

## Problem Solved

Traditional farming is becoming difficult due to:

- Unpredictable rainfall
- Climate variability
- Water scarcity
- Poor crop planning

KrushiMitra AI helps simulate these challenges and allows an AI agent to learn better farming strategies.

---

## Tasks

### 1. Crop Selection
Choose the most suitable crop based on:
- rainfall forecast
- soil type
- tank level
- water availability

### 2. Sowing Timing
Decide whether sowing should happen now or later based on:
- rain forecast
- soil moisture

### 3. Smart Irrigation
Decide:
- whether to irrigate
- how much water to use

The system rewards:
- proper soil moisture maintenance
- water conservation
- crop health improvement

---

## Environment State

The environment provides the following observations:

- day
- season
- soil_type
- soil_moisture
- temperature
- humidity
- rain_forecast_3d
- rain_forecast_7d
- tank_level
- water_availability
- crop_stage
- selected_crop
- crop_health

---

## Action Space

The agent can take the following actions:

- `crop_choice` (string)
- `sow_now` (true/false)
- `irrigate` (true/false)
- `water_amount` (float)

---

## Reward Logic

### Crop Selection
- Correct crop: `1.0`
- Poor crop: `0.2`

### Sowing Timing
- Correct sowing time: `1.0`
- Wrong decision: `0.2` to `0.3`

### Irrigation
Reward is based on:
- soil moisture range
- water efficiency
- tank preservation
- crop health

Final rewards are normalized in the range `0.0 – 1.0`.

---

## API Endpoints

- `POST /reset`
- `GET /state`
- `POST /step`
- `POST /set_task/{task_name}`

---

## Run Locally

### 1. Create virtual environment
```bash
python3 -m venv venv
source venv/bin/activate
---

## Innovation Highlights 🚀

KrushiMitra AI stands out because it combines:

- **Climate uncertainty simulation**
- **Crop planning intelligence**
- **Water-efficient irrigation strategy**
- **Sequential decision-making for AI agents**
- **Real agricultural logic instead of toy simulations**

Unlike simple recommendation apps, this environment allows an AI model to **learn farming strategy through interaction**.

---

## Real-World Use Cases 🌍

This environment can be extended into:

- Farmer advisory mobile apps
- Smart irrigation assistants
- Village-level crop planning tools
- Climate-risk simulation for agriculture
- AI-powered agri bots for rural decision support

---

## Why It Can Matter in India 🇮🇳

Indian farming is highly affected by:

- delayed monsoons
- sudden rain shifts
- water shortages
- poor crop timing

KrushiMitra AI aims to become a foundation for **AI systems that support farmers with smarter, climate-aware decisions**.
---

## Technical Compliance ✅

This environment includes:

- OpenEnv-compatible API design
- Typed state and action models
- `step()`, `reset()`, and `state()` interaction flow
- 3 benchmark tasks with automated grading
- Normalized reward outputs in range `0.0 – 1.0`
- Reproducible baseline via `inference.py`
- Docker-based deployment support

---

## Benchmark Tasks Summary

| Task | Goal | Reward Range |
|------|------|--------------|
| Crop Selection | Pick the best crop | 0.0 – 1.0 |
| Sowing Timing | Decide whether to sow now | 0.0 – 1.0 |
| Irrigation | Decide when/how much to irrigate | 0.0 – 1.0 |