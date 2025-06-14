import re

def remove_think_block(text: str) -> str:
    cleaned = re.sub(r"<think>.*?</think>", "", text, flags=re.DOTALL)
    if "<think>" in cleaned:
        cleaned = cleaned.split("<think>")[-1]
    return cleaned.strip()

def prettify_bullet_points(text: str) -> str:
    lines = text.strip().splitlines()
    clean_items = []
    for i, line in enumerate(lines, 1):
        match = re.match(r"-\s*\*\*(.*?)\*\*\s*(\(.*?\))?", line)
        if match:
            title = match.group(1).strip()
            details = match.group(2).strip("()") if match.group(2) else ""
            pretty = f"{i}. **{title}**\n   {details}"
            clean_items.append(pretty)
        else:
            clean_items.append(line)
    return "\n\n".join(clean_items)
