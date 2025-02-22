# SoulCare - a mental health support chatbot

Welcome to SoulCare repository! This project utilizes a fine-tuned version of Google's Gemma 2B model, optimized for providing mental health support to patients.

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Model Details](#model-details)
- [Metrics](#metrics)
- [Web App](#web-app)
- [Demo](#demo)
- [License](#license)

## Overview

This project aims to deliver a reliable and efficient mental health support chatbot.

## Features

- **Fine-Tuned Model:** Customized for mental health support with data collected from various HuggingFace repositories.
- **Local LLM Server:** Built with FastAPI, running on `localhost` at port `8000`.
- **User-Friendly Interface:** Interactive web app created with Streamlit.

## Installation

Follow these steps to set up the project locally:

1. **Clone the repository:**
    ```bash
    git clone https://github.com/Jefi-Ryan/Soulcare-mental-health-chatbot
    cd Soulcare-mental-health-chatbot
    ```

2. **Set up a virtual environment:**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Download the fine-tuned model from HuggingFace:**
   [Click here](https://huggingface.co/JefiRyan/Gemma-2B-Unsloth-mental-health-merged) to visit huggingface repository to download our merged model.

## Usage

### Starting the FastAPI Server

1. **Run the FastAPI server:**
    ```bash
    uvicorn llm_server:app --host 0.0.0.0 --port 8000
    ```

    The server will start at `http://localhost:8000`.

### Launching the Streamlit Web App

1. **Run the Streamlit app:**
    ```bash
    streamlit run streamlit_app.py
    ```

    The web app will be accessible at `http://localhost:8501`.

## Model Details

- **Base Model:** Google's Gemma 2B
- **Fine-Tuning:** Conducted with data from various HuggingFace repositories to cater specifically to mental health support scenarios.

## Metrics
<div style="display: flex; flex-direction: row; justify-content: space-around;">
  <div style="flex: 1; text-align: center;">
    <h4>Train/Loss</h4>
    <img src="https://github.com/user-attachments/assets/bf5944c8-421b-43cb-9aa0-6ed4c155158c" alt="Train/Loss" width="800"/>
  </div>
  <div style="flex: 1; text-align: center;">
    <h4>Train/Grad Norm</h4>
    <img src="https://github.com/user-attachments/assets/2780d190-08dc-40c9-8a34-a2d99888491c" alt="Train/Grad Norm" width="800"/>
  </div>
</div>

## Performance Comparison
| Metric                           | UnSloth Gemma (Fine-Tuned) | UnSloth Gemma (Original) |
|---------------------------------|-----------------------------|--------------------------|
| MMLU (Sociology)                | 27.86%                      | 24.88%                   |
| MMLU (Human Aging)              | 29.15%                      | 19.28%                   |
| MMLU (Professional Psychology)  | 30.72%                      | 27.12%                   |
| MMLU (Moral Disputes)           | 28.90%                      | 25.72%                   |
| MMLU (Public Relations)         | 38.18%                      | 25.45%                   |
| Bias                            | 0%                          | 23.81%                   |
| Answer Relevancy                | 90.48%                      | 80.95%                   |
| Faithfulness                    | 38.10%                      | 4.76%                    |



## Web App

The Streamlit web app provides an intuitive interface for users to interact with the chatbot. It is designed to be user-friendly and accessible.

## Demo

![image](https://github.com/user-attachments/assets/c2e7cbc5-60e3-4038-aa7a-d10ba607ea44)



## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

---

We hope you find this project useful!
