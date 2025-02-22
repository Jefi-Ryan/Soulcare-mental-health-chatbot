import os
import time
from dotenv import load_dotenv
from fastapi import FastAPI
import torch
from transformers import AutoTokenizer, AutoModelForCausalLM, BitsAndBytesConfig
from peft import AutoPeftModelForCausalLM
from transformers import AutoTokenizer

# print(f"Memory allocated: {torch.cuda.memory_allocated()} bytes")
torch.cuda.empty_cache()

load_dotenv(verbose=True)

os.environ['CACHE_DIR'] = r"E:\LLM\model_cache"
cache_dir = os.environ['CACHE_DIR']
ov_config = {"PERFORMANCE_HINT": "LATENCY", "NUM_STREAMS": "1", "CACHE_DIR": cache_dir}

path = r"E:\LLM\gemma-2b-soulcare"
model_id = path
offload_folder = r"E:\offload_folder"

model = AutoModelForCausalLM.from_pretrained(model_id, device_map="auto", cache_dir=cache_dir)
tokenizer = AutoTokenizer.from_pretrained(model_id, device_map="auto", cache_dir=cache_dir)

# chat = """You are a therapist and your name is SoulCare. Your goal is to provide mental health support and counseling to users. Ensure that your responses are empathetic, supportive, and non-judgmental. Prioritize the user’s well-being and safety at all times.
#         Write a response that is appropriate for the input."""

# -------------------------

def run_generation(prompt):
    # global chat

    # alpaca_prompt = chat + """
    #
    #     ### Input:
    #     {}
    #
    #     ### Response:
    #     {}"""

    alpaca_prompt = """You are a therapist and your name is SoulCare. Your goal is to provide mental health support and counseling to users. Ensure that your responses are empathetic, supportive, and non-judgmental. Prioritize the user’s well-being and safety at all times.
        Write a response that is appropriate for the input. Always give response in mark down format.
        
        ### Input:
        {}

        ### Response:
        {}"""

    inputs = tokenizer(
        [
            alpaca_prompt.format(
                prompt,  # input
                "",  # output - leave this blank for generation!
            )
        ], return_tensors="pt")

    outputs = model.generate(**inputs, max_new_tokens=128, use_cache=True)
    res = tokenizer.batch_decode(outputs)

#     response = res[0].split("### Response:")[-1].split("<eos>")[0].lstrip("\\n").strip().rstrip("]")
#
#     chat += """
#
# ### Input:
# {}
#
# ### Response:
# {}""".format(prompt,response)
#
#     print(chat)

    return res


app = FastAPI()


@app.get('/chatbot/')
async def root(query: str = None):
    if query:
        ans = run_generation(query)
        return {'response': f'{ans}'}
    return {'response': ''}


# API reference
# http://127.0.0.1:8000/docs

# How to run (You need to have uvicorn and streamlit -> pip install uvicorn streamlit)
# uvicorn openvino-rag-server:app