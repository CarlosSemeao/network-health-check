from collector import collect_ssh_output
from linux_parser import parse_ip_a_output
from linux_checker import assess_linux_interface_health
from linux_reporter import generate_linux_report, save_linux_report


def main() -> None:
    host = "10.211.55.8"
    username = "carlossemeao"
    command = "ip a"
    key_filename = "/home/carlossemeao/.ssh/id_ed25519"
    ssh_output_path = "data/ssh_output.txt"

    output = collect_ssh_output(host, username, command, key_filename)

    with open(ssh_output_path, "w", encoding="utf-8") as file:
        file.write(output)

    interfaces = parse_ip_a_output(ssh_output_path)
    results = assess_linux_interface_health(interfaces)
    report = generate_linux_report(results)

    print(report)
    save_linux_report(report)


if __name__ == "__main__":
    main()