import csv
from tabulate import tabulate
from typing import List
from src.models import Employee


class EmployeeCollection:
    def __init__(self, employees: List[Employee] = None):
        self.employees = employees or []

    @classmethod
    def from_csv(cls, paths: str | List[str]):
        employees = []

        if isinstance(paths, str):
            paths = [paths]

        for path in paths:
            if path is not None:
                with open(path) as file:
                    csv_data = csv.DictReader(file)
                    for row in csv_data:
                        employee = Employee.from_csv_row(row)
                        employees.append(employee)

        return cls(employees)

    def get_performance_by_position(self) -> dict:
        position_stats = {}

        for emp in self.employees:
            if emp.position not in position_stats:
                position_stats[emp.position] = {"count": 0, "performance": 0.0}

            stats = position_stats[emp.position]
            stats["count"] += 1
            stats["performance"] += emp.performance

        for _, stats in position_stats.items():
            stats["performance"] = round(
                stats["performance"] / stats["count"], 2
            )

        sorted_by_performance = dict(
            sorted(
                position_stats.items(),
                key=lambda x: x[1]["performance"],
                reverse=True
            )
        )
        return sorted_by_performance

    def print_performance_by_position(self):
        performance = self.get_performance_by_position()
        table_data = []
        headers = ["", "position", "performance"]

        for i, (position, stats) in enumerate(performance.items(), start=1):
            table_data.append([i, position, stats["performance"]])

        print(tabulate(table_data, headers=headers))

    def print_sorted_by_name(self):
        sorted_employees = sorted(self.employees, key=lambda x: x.name)
        table_data = []
        headers = sorted_employees[0].to_csv_row().keys()

        for index, row in enumerate(sorted_employees, start=1):
            employee = row.to_csv_row()
            table_data.append(employee.values())

        print(tabulate(table_data, headers=headers))
