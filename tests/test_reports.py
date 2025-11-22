from src.reports import build_report
from src.models import Employee
from src.collections import EmployeeCollection
from tests.fixtures.models_fixtures import sample_employee_row


def test_build_default_report(capsys, sample_employee_row):
    employees = EmployeeCollection(
        [Employee.from_csv_row(sample_employee_row)]
    )

    build_report(None, employees)

    captured = capsys.readouterr()
    output = captured.out

    assert "Alex Ivanov" in output
    assert "Python, Django, PostgreSQL, Docker" in output
    assert "Backend Developer" in output


def test_performance_report(capsys, sample_employee_row):
    employees = EmployeeCollection(
        [Employee.from_csv_row(sample_employee_row)]
    )

    build_report("performance", employees)

    captured = capsys.readouterr()
    output = captured.out

    assert "Alex Ivanov" not in output
    assert "Python, Django, PostgreSQL, Docker" not in output
    assert "performance" in output
    assert "position" in output
