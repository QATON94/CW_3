from pathlib import Path

from src.setings import OPERATION_PATH


def test_path():
    path_ = Path(__file__).parent.parent
    expected_path = path_.joinpath("data", "operations.json")
    assert OPERATION_PATH == expected_path
