from src.app import main

def test_output_is_equal_to_golden() -> None:
    output = main()
    with open("golden.txt", mode="r",encoding="utf-16") as file:
        file_data = file.read()
    assert output==file_data