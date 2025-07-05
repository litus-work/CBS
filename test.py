import re
from html import escape

def structure_ai_email(raw: str) -> dict:
    """Убираем <think>, вытягиваем subject и аккуратно формируем тело письма."""
    # 1) вырезаем блок <think> … </think>
    cleaned = re.sub(r"<think>[\s\S]*?</think>", "", raw, flags=re.I).strip()

    # 2) достаём subject
    subj_match = re.search(r"<subject>(.*?)</subject>", cleaned, re.S)
    subject = subj_match.group(1).strip() if subj_match else "Kein Betreff"

    # 3) достаём HTML-документ
    html_match = re.search(r"<!DOCTYPE html>[\s\S]*?</html>", cleaned, re.I)
    html_full = html_match.group(0).strip() if html_match else ""

    # 4) если body отсутствует или не структурирован -- «чинить»
    body_match = re.search(r"<body>([\s\S]*?)</body>", html_full, re.I)
    if body_match:
        body_inner = body_match.group(1).strip()
    else:
        # fallback: превращаем текст-абзацы и "- " пункты в HTML
        text = re.sub(r" {2,}", " ", cleaned)       # убираем двойные пробелы
        paragraphs = []
        bullets = []
        for line in text.splitlines():
            line = line.strip()
            if line.startswith("-"):
                bullets.append(line.lstrip("- ").strip())
            elif line:
                if bullets:
                    paragraphs.append("<ul>" + "".join(f"<li>{escape(b)}</li>" for b in bullets) + "</ul>")
                    bullets = []
                paragraphs.append(f"<p>{escape(line)}</p>")
        if bullets:
            paragraphs.append("<ul>" + "".join(f"<li>{escape(b)}</li>" for b in bullets) + "</ul>")
        body_inner = "\n".join(paragraphs)
        html_full = f"""<!DOCTYPE html>
<html><head><meta charset="UTF-8"></head><body>{body_inner}</body></html>"""

    return {
        "email_subject": subject,
        "email_body_html": html_full
    }

# === n8n ===
cleaned_output = items[0]["json"]["output"]   # или output_cleaned, если уже удалён <think>
result = structure_ai_email(cleaned_output)

return [{"json": result}]
