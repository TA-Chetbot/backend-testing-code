import requests
import time
import json

def test_api_response_speed(url, payload):
    response_times = []
    headers = {"Content-Type": "application/json"}
    for _ in range(5):
        start_time = time.time()
        response = requests.post(url, data=json.dumps(payload), headers=headers)
        end_time = time.time()
        response_time = end_time - start_time
        response_times.append(response_time)
        print(f"Response time: {response_time:.6f} seconds")

    average_response_time = sum(response_times) / len(response_times)
    print(f"Average response time: {average_response_time:.6f} seconds")

if __name__ == "__main__":
    print("Testing FastAPI application...")
    fastapi_url = "http://localhost:8000/get_answer"
    fastapi_payload = {"question": "I need help"}
    test_api_response_speed(fastapi_url, fastapi_payload)

    print("\nTesting Flask application...")
    flask_url = "http://localhost:5000/get_answer"
    flask_payload = {"question": "I need help"}
    test_api_response_speed(flask_url, flask_payload)

    print("\nTesting Django REST application...")
    django_url = "http://localhost:8080/get_answer"
    django_payload = {"question": "I need help"}
    test_api_response_speed(django_url, django_payload)