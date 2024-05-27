import requests
import time
import json

def test_api_response_speed(url1, url2, payload):
    response_times = []
    headers = {"Content-Type": "application/json"}
    for _ in range(5):
        start_time = time.time()
        preprocess_response = requests.post(url1, data=json.dumps(payload), headers=headers)
        preprocessed_question = {"question": preprocess_response.json()["preprocessed_question"]}
        response = requests.post(url2, data=json.dumps(preprocessed_question), headers=headers)
        end_time = time.time()
        response_time = end_time - start_time
        response_times.append(response_time)
        print(f"Response time: {response_time:.6f} seconds")

    average_response_time = sum(response_times) / len(response_times)
    print(f"Average response time: {average_response_time:.6f} seconds")

if __name__ == "__main__":
    print("Testing FastAPI application...")
    fastapi_url1 = "http://localhost:8000/preprocess_question"
    fastapi_url2 = "http://localhost:8000/get_answer"
    fastapi_payload = {"text": "I need help"}
    test_api_response_speed(fastapi_url1, fastapi_url2, fastapi_payload)

    print("\nTesting Flask application...")
    flask_url1 = "http://localhost:5000/preprocess_question"
    flask_url2 = "http://localhost:5000/get_answer"
    flask_payload = {"text": "I need help"}
    test_api_response_speed(flask_url1, flask_url2, flask_payload)

    print("\nTesting Django REST application...")
    django_url1 = "http://localhost:8080/preprocess_question"
    django_url2 = "http://localhost:8080/get_answer"
    django_payload = {"text": "I need help"}
    test_api_response_speed(django_url1, django_url2, django_payload)