from tests.fixtures.file_fixtures import sample_csv_file
from tests.fixtures.models_fixtures import sample_employee_row
from src.collections import EmployeeCollection, Employee


def test_employees_collenction(sample_csv_file):
    collection = EmployeeCollection.from_csv(sample_csv_file)
    assert isinstance(collection.employees, list)
    assert isinstance(collection.employees[0], Employee)


def test_employees_performance(sample_csv_file):
    collection = EmployeeCollection.from_csv(sample_csv_file)
    performance = collection.get_performance_by_position()
    assert isinstance(performance, dict)
    assert len(performance) == 7


def test_print_employees_performance(capsys, sample_employee_row):
    test_employees = [
        Employee.from_csv_row(sample_employee_row),
    ]
    collection = EmployeeCollection(test_employees)
    collection.print_performance_by_position()

    captured = capsys.readouterr()
    output = captured.out

    assert "Backend Developer" in output
    assert "position" in output
    assert "performance" in output
    assert str(4.8) in output
