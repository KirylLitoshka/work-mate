import tempfile
import os
import pytest


@pytest.fixture
def single_csv_file():
    with tempfile.NamedTemporaryFile(
        mode="w", suffix=".csv", delete=False
    ) as f:
        f.write("Lorem ipsum")
        temp_file_path = f.name

    yield temp_file_path

    if os.path.exists(temp_file_path):
        os.unlink(temp_file_path)


@pytest.fixture
def empty_csv_file():
    with tempfile.NamedTemporaryFile(
        mode="w", suffix=".csv", delete=False
    ) as f:
        temp_file_path = f.name

    yield temp_file_path

    if os.path.exists(temp_file_path):
        os.unlink(temp_file_path)


@pytest.fixture
def simple_text_file():
    with tempfile.NamedTemporaryFile(
        mode="w", suffix=".txt", delete=False
    ) as f:
        temp_file_path = f.name
        f.write = "Lorem ipsum"

    yield temp_file_path

    if os.path.exists(temp_file_path):
        os.unlink(temp_file_path)


@pytest.fixture
def sample_csv_file():
    with tempfile.NamedTemporaryFile(
        mode="w+", suffix=".csv", delete=False
    ) as f:
        f.write(
            "name,position,completed_tasks,performance,skills,team,experience_years\n"
        )
        f.write(
            'David Chen,Mobile Developer,36,4.6,"Swift, Kotlin, React Native, iOS",Mobile Team,3\n'
        )
        f.write(
            'Elena Popova,Backend Developer,43,4.8,"Java, Spring Boot, MySQL, Redis",API Team,4\n'
        )
        f.write(
            'Chris Wilson,DevOps Engineer,39,4.7,"Docker, Jenkins, GitLab CI, AWS",Infrastructure Team,5\n'
        )
        f.write(
            'Olga Kuznetsova,Frontend Developer,42,4.6,"Vue.js, JavaScript, Webpack, Sass",Web Team,3\n'
        )
        f.write(
            'Robert Kim,Data Engineer,34,4.7,"Python, Apache Spark, Airflow, Kafka",Data Team,4\n'
        )
        f.write(
            'Julia Martin,QA Engineer,38,4.5,"Playwright, Jest, API Testing",Testing Team,3\n'
        )
        f.write(
            'Tom Anderson,Backend Developer,49,4.9,"Go, Microservices, gRPC, PostgreSQL",API Team,7\n'
        )
        f.write(
            'Lisa Wang,Mobile Developer,33,4.6,"Flutter, Dart, Android, Firebase",Mobile Team,2\n'
        )
        f.write(
            'Mark Thompson,Data Scientist,31,4.7,"R, Python, TensorFlow, SQL",AI Team,4'
        )
        f.close()
        temp_file_path = f.name

    yield temp_file_path

    if os.path.exists(temp_file_path):
        os.unlink(temp_file_path)
