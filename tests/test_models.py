from src.models import Employee
from tests.fixtures.models_fixtures import sample_employee_row


def test_creation_employee_from_csv(sample_employee_row):
    employee = Employee.from_csv_row(sample_employee_row)
    assert employee.name == "Alex Ivanov"
    assert employee.position == "Backend Developer"
    assert employee.completed_tasks == 45
    assert employee.performance == 4.8
    assert employee.skills == ["Python", "Django", "PostgreSQL", "Docker"]
    assert employee.team == "API Team"
    assert employee.experience_years == 5


def test_employee_to_csv(sample_employee_row):
    employee = Employee.from_csv_row(sample_employee_row)
    csv_row = employee.to_csv_row()
    assert isinstance(csv_row, dict)
