import re
import json

def markdown_to_json(text: str) -> dict:
    lines = text.strip().split("\n")
    data = {}
    current_key = None
    current_val = []

    for line in lines:
        match = re.match(r"^\d+\.\s+\*\*(.+?)\*\*", line)
        if match:
            if current_key:
                value = " ".join(current_val).strip()
                if value:
                    data[current_key] = value
            current_key = match.group(1).strip()
            current_val = []
        else:
            current_val.append(line.strip())

    if current_key:
        value = " ".join(current_val).strip()
        if value:
            data[current_key] = value

    return data
