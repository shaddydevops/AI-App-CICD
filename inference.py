from huggingface_hub import InferenceClient

def get_model_response(prompt: str, api_key: str) -> str:
    client = InferenceClient(api_key=api_key)

    response = client.chat.completions.create(
        model="deepseek-ai/DeepSeek-R1",
        messages=[
            {"role": "system", "content": "You are a helpful assistant. Do not output your thoughts <think> or internal reflections. Always answer directly."},
            {"role": "user", "content": prompt}
        ],
        max_tokens=200,
    )

    return response.choices[0].message.content
