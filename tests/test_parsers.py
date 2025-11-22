import sys
import pytest
from src.parsers import args_parse
from tests.fixtures.file_fixtures import single_csv_file


def test_get_empty_args(monkeypatch):
    test_args = ["main.py"]
    monkeypatch.setattr(sys, "argv", test_args)
    args = args_parse()
    assert args.files == []
    assert args.report is None


@pytest.mark.parametrize(
    "test_args, result_or_exception",
    [
        (["main.py --report"], None),
        (["main.py", "--report", "performance"], "performance"),
    ],
)
def test_report_args(monkeypatch, test_args, result_or_exception):
    monkeypatch.setattr(sys, "argv", test_args)
    args = args_parse()
    assert args.report == result_or_exception


def test_report_choice_exeption(monkeypatch):
    test_args = ["main.py", "--report", "123"]
    monkeypatch.setattr(sys, "argv", test_args)
    with pytest.raises(SystemExit) as exc_info:
        args_parse()

    assert exc_info.value.code == 2


def test_bad_files_args(monkeypatch):
    test_args = ["main.py", "--files", "temp.csv"]
    monkeypatch.setattr(sys, "argv", test_args)
    args = args_parse()
    assert args.files == [None]


def test_existed_files_args(monkeypatch, single_csv_file):
    test_args = ["main.py", "--files", single_csv_file]
    monkeypatch.setattr(sys, "argv", test_args)
    args = args_parse()
    assert single_csv_file in args.files
   
