from typing import List, Dict


def assess_interface_health(interfaces: List[Dict[str, str]]) -> List[Dict[str, str]]:
    """
    Evaluate interface health and assign a health state and reason.
    """
    results = []

    for interface in interfaces:
        name = interface["interface"]
        ip_address = interface["ip_address"]
        status = interface["status"].lower()
        protocol = interface["protocol"].lower()

        health = "HEALTHY"
        reason = "Interface is operational."

        if "administratively down" in status:
            health = "INFO"
            reason = "Interface is administratively down."
        elif status == "up" and protocol == "down":
            health = "CRITICAL"
            reason = "Interface is up but line protocol is down."
        elif status == "down" and protocol == "down":
            health = "WARNING"
            reason = "Interface is down."
        elif ip_address == "unassigned" and "loopback" not in name.lower():
            health = "WARNING"
            reason = "Interface has no IP address assigned."

        results.append(
            {
                "interface": name,
                "ip_address": ip_address,
                "status": status,
                "protocol": protocol,
                "health": health,
                "reason": reason,
            }
        )

    return results