from collector import collect_ssh_output
from host_loader import load_hosts
from linux_parser import parse_ip_a_output
from linux_checker import assess_linux_interface_health
from linux_reporter import generate_linux_report


def main() -> None:
    hosts_file = "data/hosts.txt"
    username = "carlossemeao"
    command = "ip a"
    key_filename = "/home/carlossemeao/.ssh/id_ed25519"

    hosts = load_hosts(hosts_file)

    for host in hosts:
        print(f"\n=== Checking host: {host} ===")

        try:
            output = collect_ssh_output(host, username, command, key_filename)

            ssh_output_path = f"data/{host}_ssh_output.txt"
            with open(ssh_output_path, "w", encoding="utf-8") as file:
                file.write(output)

            interfaces = parse_ip_a_output(ssh_output_path)
            results = assess_linux_interface_health(interfaces)
            report = generate_linux_report(results)

            report_path = f"data/{host}_linux_report.txt"
            with open(report_path, "w", encoding="utf-8") as file:
                file.write(report)

            print(report)

        except Exception as error:
            print(f"FAILED to check host {host}: {error}")


if __name__ == "__main__":
    main()
