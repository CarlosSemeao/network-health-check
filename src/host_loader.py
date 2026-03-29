from typing import List


def load_hosts(file_path: str) -> List[str]:
    """
    Load target hosts from a text file, ignoring blank lines.
    """
    with open(file_path, "r", encoding="utf-8") as file:
        return [line.strip() for line in file if line.strip()]
