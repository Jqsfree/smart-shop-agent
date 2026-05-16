import json
import requests
from openai import OpenAI
from dotenv import load_dotenv

import os

load_dotenv()

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY"),
    base_url="https://api.deepseek.com"
)

tools = [
    {
        "type": "function",
        "function": {
            "name": "query_customer",
            "description": "Query customer information",
            "parameters": {
                "type": "object",
                "properties": {
                    "customer_name":{
                        "type": "string",
                        "descripation": "Customer name",
                    }
                },
                "required": ["customer_name"]
            }
        }
    }
]

messages = [
    {
        "role": "user",
        "content": "帮我查询 li 的客户信息"
    }
]

response = client.chat.completions.create(
            model="deepseek-v4-flash",
            messages=messages,
            tools=tools
)

message = response.choices[0].message

tool_call = message.tool_calls[0]

tool_args = json.loads(tool_call.function.arguments)


print("AI 决定调用工具:")
print(tool_args)

api_response = requests.post(
    "http://127.0.0.1:8000/customers/query",
    json=tool_args
)

tool_result = api_response.json()

print("\nTool 返回:")
print(tool_result)

messages.append(message)

messages.append({
    "role": "tool",
    "tool_call_id": tool_call.id,
    "content": json.dumps(tool_result)
})

final_response = client.chat.completions.create(
    model="deepseek-v4-flash",
    messages=messages
)

print("\n最终 AI 回复:\n")

print(final_response.choices[0].message.content)