from typing import Optional
from src.collections import EmployeeCollection

def build_report(report_type: Optional[str], employees: EmployeeCollection) -> None:
    if report_type is None:
        employees.print_sorted_by_name()
    elif report_type == "performance":
        employees.print_performance_by_position()