import pytest


@pytest.fixture
def sample_employee_row():
    return {
        "name": "Alex Ivanov",
        "position": "Backend Developer",
        "completed_tasks": "45",
        "performance": "4.8",
        "skills": "Python, Django, PostgreSQL, Docker",
        "team": "API Team",
        "experience_years": "5",
    }
