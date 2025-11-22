from src.validators import file_validation
from tests.fixtures.file_fixtures import *


def test_file_not_found_validation(capsys):
    result = file_validation("nonexistent_file.csv")
    captured = capsys.readouterr()
    assert result is None
    assert "File nonexistent_file.csv not found" in captured.out


def test_path_is_not_file(capsys):
    result = file_validation("/")
    captured = capsys.readouterr()
    assert result is None
    assert "/ is not a file" in captured.out


def test_wrong_extension_validation(capsys, simple_text_file):
    result = file_validation(simple_text_file)
    captured = capsys.readouterr()
    assert result is None
    assert f"File {simple_text_file} doesn't have a .csv extension" in captured.out


def test_empty_file_validation(capsys, empty_csv_file):
    result = file_validation(empty_csv_file)
    captured = capsys.readouterr()
    assert result is None
    assert f"File {empty_csv_file} is empty" in captured.out


def test_valid_path_validation(sample_csv_file):
    result = file_validation(sample_csv_file)
    assert result is sample_csv_file
