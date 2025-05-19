import requests

def test_chat():
    url = 'http://127.0.0.1:5000/chat'
    message = {"message": "Hi, what can you do?"}
    response = requests.post(url, json=message)
    print(response.json())

if __name__ == '__main__':
    test_chat()