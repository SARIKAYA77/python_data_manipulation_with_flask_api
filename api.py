import requests

data = {
    "10:00-11:00": [{"type": "in", "value": 15}, {"type": "out", "value": 12}, {"type": "in", "value": 4}],
    "11:00-12:00": [{"type": "in", "value": 11}, {"type": "out", "value": 14}, {"type": "out", "value": 4}],
    "12:00-13:00": [{"type": "in", "value": 24}, {"type": "out", "value": 4}, {"type": "in", "value": 15}],
    "13:00-14:00": [{"type": "in", "value": 8}, {"type": "out", "value": 25}, {"type": "in", "value": 12}],
    "14:00-15:00": [{"type": "in", "value": 3}, {"type": "out", "value": 5}, {"type": "out", "value": 17},
                    {"type": "out", "value": 10}],
    "15:00-16:00": [{"type": "in", "value": 19}, {"type": "out", "value": 2}],
    "16:00-17:00": [],
    "17:00-18:00": [{"type": "in", "value": 0}, {"type": "out", "value": 18}]
}


response = requests.post("http://127.0.0.1:5000/resource", json=data)
print(response.text)