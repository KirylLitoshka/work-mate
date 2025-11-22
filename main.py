from src.parsers import args_parse
from src.collections import EmployeeCollection
from src.reports import build_report


def main() -> None:
    args = args_parse()
    employees = EmployeeCollection.from_csv(args.files)
    build_report(report_type=args.report, employees=employees)


if __name__ == "__main__":
    main()
