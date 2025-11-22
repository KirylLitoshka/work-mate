import os
from typing import AnyStr


def file_validation(path: AnyStr) -> AnyStr:
    if not os.path.exists(path):
        print(f"File {path} not found")
        return None
    if not os.path.isfile(path):
        print(f"{path} is not a file")
        return None
    if not path.lower().endswith(".csv"):
        print(f"File {path} doesn't have a .csv extension")
        return None
    if os.path.getsize(path) == 0:
        print(f"File {path} is empty")
        return None
    else:
        return path
