import gradio as gr
import subprocess
import threading
import time
import requests

def run_api():
    subprocess.run(["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "7860"])

threading.Thread(target=run_api, daemon=True).start()

time.sleep(5)

with gr.Blocks() as demo:
    gr.Markdown("# 🌾 KrushiMitra AI")
    gr.Markdown("Climate-Adaptive Farming Decision Environment")
    gr.Markdown("This Space runs the KrushiMitra AI OpenEnv environment.")
    gr.Markdown("Use the API endpoints directly:")
    gr.Markdown("- `/docs`")
    gr.Markdown("- `/reset`")
    gr.Markdown("- `/step`")
    gr.Markdown("- `/state`")

demo.launch()