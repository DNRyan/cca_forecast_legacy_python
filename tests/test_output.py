import json
from src.app import get_summary

def test_output_is_equal_to_golden() -> None:
    with open("tests/data.json", mode="r") as file:
        input_data = json.loads(file.read())

    with open("golden.txt", mode="r",encoding="utf-16") as file:
        file_data = file.read()

    assert "\n".join(list(get_summary(input_data))) == file_data