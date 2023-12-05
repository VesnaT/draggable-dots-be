from typing import Dict
import json


def read_data() -> Dict:
    with open("dots.json", "r") as f:
        return json.load(f)


def save_data(dot_data: Dict):
    with open("dots.json", "r") as f:
        data: Dict = json.load(f)

    data.update(dot_data)

    with open("dots.json", "w") as f:
        json.dump(data, f)
