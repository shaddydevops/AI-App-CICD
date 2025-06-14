import re

def normalize_numbered_list(text: str) -> str:
    lines = text.strip().split("\n")
    output = []
    count = 1

    for line in lines:
        if re.match(r"^\d+\.\s+\*\*", line):
            line = re.sub(r"^\d+\.", f"{count}.", line)
            count += 1
        output.append(line)

    return "\n".join(output)
