import re

def parse_log(file_path):
    with open(file_path, 'r') as f:
        lines = f.readlines()

    events = []
    for line in lines:
        match = re.match(r'\[(\w+)\]\s+(\w+):\s+(.*)', line)
        if match:
            timestamp, protocol, message = match.groups()
            events.append({
                "timestamp": timestamp,
                "protocol": protocol.upper(),
                "message": message
            })
    return events

def protocol_check(events, allowed_protocols=("SAS", "SATA", "PCIE")):
    violations = [e for e in events if e["protocol"] not in allowed_protocols]
    return violations
