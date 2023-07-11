import requests

url = 'http://localhost:5000/generate'  # Replace with your server's URL

data = {
    'prompt': 'Hello, GPT4All!'
}

response = requests.post(url, json=data, stream=True)

if response.status_code == 200:
    for chunk in response.iter_content(chunk_size=1024):
        if chunk:
            print(chunk.decode('utf-8'))
else:
    print(f"Request failed with status code {response.status_code}")

