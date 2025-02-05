import re


def replace_static(raw: str, output: str):
    pattern = r'"(assets/[^"]*")'

    def replace(match):
        new = '"{% static "About/lol %}"'
        return new.replace('lol', match.group(1))

    with open(raw, 'r', encoding='utf-8') as f:
        raw_html = f.read()

    pretty_html = re.sub(pattern, replace, raw_html)
    with open(output, 'w', encoding='utf-8') as f:
        f.write(pretty_html)
