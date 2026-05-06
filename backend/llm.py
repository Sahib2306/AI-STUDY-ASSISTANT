from huggingface_hub import InferenceClient
import os

def load_llm():
    client = InferenceClient(
        model="Qwen/Qwen2.5-72B-Instruct",
        token=os.getenv("HF_TOKEN")
    )
    return client