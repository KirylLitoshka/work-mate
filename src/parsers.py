import argparse
from src.validators import file_validation


def args_parse() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--files",
        type=file_validation,
        nargs="*",
        default=[],
        help="File paths"
    )
    parser.add_argument(
        "--report",
        type=str,
        default=None,
        nargs="?",
        const=None,
        choices=["performance"],
        help="Report type",
    )
    args = parser.parse_known_args()
    return args[0]
