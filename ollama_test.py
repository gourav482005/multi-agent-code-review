import requests

response = requests.post(
    'http://localhost:11434/api/generate',
    json={
        "model": "llama3",
        "prompt": "Give a security review of this Python code:\ndef login(user, password):\n    if user == 'admin' and password == '1234':\n        print('Access granted')",
        "stream": False
    }
)

print(response.json()['response'])
