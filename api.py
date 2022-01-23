import requests
import json


def get_data_from_api() -> str:
    with open('data.json') as f:
        data = json.load(f)

    response = requests.post("http://127.0.0.1:5000/resource", json=data)
    return response, response.status_code


def main():
    response, status_code = get_data_from_api()
    print(response.text)


if __name__ == "__main__":
    main()
