from typing import List, Dict


def generate_report(results: List[Dict[str, str]]) -> str:
    """
    Generate a readable health report.
    """
    lines = []
    lines.append("NETWORK HEALTH CHECK REPORT")
    lines.append("=" * 50)

    for item in results:
        lines.append(f"Interface : {item['interface']}")
        lines.append(f"IP Address: {item['ip_address']}")
        lines.append(f"Status    : {item['status']}")
        lines.append(f"Protocol  : {item['protocol']}")
        lines.append(f"Health    : {item['health']}")
        lines.append(f"Reason    : {item['reason']}")
        lines.append("-" * 50)

    return "\n".join(lines)

def save_report_to_file(report: str, output_path: str = "report.txt") -> None:
    """
    Save the generated report to a file.
    """
    with open(output_path, "w", encoding="utf-8") as file:
        file.write(report)