from typing import List, Dict


def assess_linux_interface_health(interfaces: List[Dict[str, str]]) -> List[Dict[str, str]]:
    """
    Evaluate Linux interface health and assign health status and reason.
    """
    results = []

    for interface in interfaces:
        name = interface["interface"]
        state = interface["state"]
        ipv4 = interface["ipv4"]
        interface_type = interface["type"]

        health = "HEALTHY"
        reason = "Interface is operational."

        if interface_type == "loopback":
            health = "INFO"
            reason = "Loopback interface is present."
        elif state != "UP":
            health = "WARNING"
            reason = f"Interface state is {state}."
        elif ipv4 == "unassigned":
            health = "WARNING"
            reason = "Interface is up but has no IPv4 address."
        else:
            health = "HEALTHY"
            reason = "Interface is up and has an IPv4 address."

        results.append(
            {
                "interface": name,
                "state": state,
                "ipv4": ipv4,
                "type": interface_type,
                "health": health,
                "reason": reason,
            }
        )

    return results