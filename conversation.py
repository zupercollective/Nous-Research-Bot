import http.client
import json
import time

# Constants for API config
API_KEY = "api_key"  # Replace with your real key
MODEL = "model_name" # Replace with actual model name
HOST = "inference-api.nousresearch.com"
MAX_TOKENS = 1024  # Default token count to avoid cutoff

# HTTP headers for API request
headers = {
    'Authorization': f'Bearer {API_KEY}',
    'Content-Type': 'application/json'
}

# Function to call the Nous API
def call_api(messages, max_tokens=512):
    conn = http.client.HTTPSConnection(HOST)
    payload = json.dumps({
        "model": MODEL,
        "messages": messages,
        "max_tokens": max_tokens
    })

    # Send the POST request
    conn.request("POST", "/v1/chat/completions", payload, headers)
    res = conn.getresponse()
    body = res.read()

    try:
        data = json.loads(body)

        # If there's an API error, return None
        if "error" in data:
            print("[API ERROR]", data["error"]["message"])
            return None, "error"

        # Extract the assistant's message
        choice = data["choices"][0]
        message = choice["message"]["content"]
        finish_reason = choice.get("finish_reason", "stop")

        # Warn if output is incomplete
        if finish_reason != "stop":
            print("[WARN] Assistant reply may be incomplete. Retrying with higher max_tokens...")

        return message, finish_reason

    except Exception as e:
        print("Failed to parse API response:", body)
        return None, "error"

# Retry wrapper with increasing tokens
def generate_reply(messages, max_retries=4, initial_tokens=1024):
    tokens = initial_tokens
    for attempt in range(max_retries):
        reply, finish_reason = call_api(messages, max_tokens=tokens)
        if reply is None:
            print("[ERROR] No reply. Retrying...")
        elif finish_reason != "stop":
            print(f"[WARN] Incomplete reply. Retrying with more tokens (was {tokens})...")
            tokens = min(tokens + 512, 4096)  # cap at 4096 tokens
        else:
            return reply
        time.sleep(2)  # avoid rate limit or server overload
    return None  # return None if all retries fail

# Main interaction loop (auto-conversational)
def chat_loop():
    messages = [
        {
            "role": "system",
            "content": (
                "You are a deep thinking AI. You may use extremely long chains of thought "
                "and enclose your internal thoughts in <think> </think> tags."
            )
        },
        {
            "role": "user",
            "content": "What do you think about Indonesia?"
        }
    ]

    while True:
        # Send request to assistant
        reply = call_api(messages, max_tokens=2048)
        if reply is None or reply[0] is None:
            print("No reply from assistant. Retrying...")
            time.sleep(10)
            continue

        print("\n[Assistant Reply]")
        print(reply[0])

        messages.append({"role": "assistant", "content": reply[0]})

        # Ask the assistant to generate a follow-up prompt
        followup_prompt = [
            {
                "role": "system",
                "content": "Based on the previous message, generate a clever follow-up question to continue the discussion."
            },
            {
                "role": "user",
                "content": reply[0]
            }
        ]

        followup = call_api(followup_prompt, max_tokens=256)
        followup_text = followup[0] if followup and followup[0] else "Could you elaborate on that?"

        print(f"\n[Follow-up Question]\n{followup_text}\n")
        messages.append({"role": "user", "content": followup_text})

# Start the chat loop
chat_loop()
