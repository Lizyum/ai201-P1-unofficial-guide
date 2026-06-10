# import requests
# from pathlib import Path
# from bs4 import BeautifulSoup

# def save_html(url, output_path):
#     response = requests.get(
#         url,
#         headers={"User-Agent": "fgli-rag-project/0.1"}
#     )

#     response.raise_for_status()

#     Path(output_path).parent.mkdir(
#         parents=True,
#         exist_ok=True
#     )

#     with open(output_path, "w", encoding="utf-8") as f:
#         f.write(response.text)

# def process_html_to_markdown(raw_input, processed_output, metadata):
#     input_path = Path(raw_input)
#     output_path = Path(processed_output)

#     output_path.parent.mkdir(parents=True, exist_ok=True)

#     html = input_path.read_text(encoding="utf-8")
#     soup = BeautifulSoup(html, "html.parser")

#     for tag in soup(["script", "style", "nav", "footer", "aside"]):
#         tag.decompose()

#     article = soup.find("article") or soup.find("main") or soup.body

#     paragraphs = []
#     for tag in article.find_all(["h1", "h2", "h3", "p", "li"]):
#         text = tag.get_text(" ", strip=True)
#         if text:
#             paragraphs.append(text)

#     content = "\n\n".join(paragraphs)

#     title = metadata.get("title", "Untitled Webpage")
#     source_type = metadata.get("source_type", "webpage")
#     organization = metadata.get("organization", "")
#     url = metadata.get("url", "")
#     topics = ", ".join(metadata.get("topics", []))

#     markdown = f"""# {title}

# Source Type: {source_type}
# Organization: {organization}
# Source URL: {url}
# Topics: {topics}

# ## Content

# {content}
# """

#     with open(output_path, "w", encoding="utf-8") as f:
#         f.write(markdown)


import html
import re
import requests
from pathlib import Path
from bs4 import BeautifulSoup


def clean_text(text: str) -> str:
    """Clean residual HTML entities, symbols, and extra whitespace."""
    text = html.unescape(text)

    # Remove common leftover symbols/noise
    text = text.replace("\xa0", " ")
    text = text.replace("|", " ")
    text = text.replace("•", " ")
    text = text.replace("●", " ")

    # Collapse repeated whitespace
    text = re.sub(r"\s+", " ", text)

    # Remove repeated punctuation/symbol-only fragments
    text = re.sub(r"^[\W_]+$", "", text)

    return text.strip()


def save_html(url, output_path):
    response = requests.get(
        url,
        headers={"User-Agent": "fgli-rag-project/0.1"}
    )
    response.raise_for_status()

    Path(output_path).parent.mkdir(parents=True, exist_ok=True)

    with open(output_path, "w", encoding="utf-8") as f:
        f.write(response.text)


def process_html_to_markdown(raw_input, processed_output, metadata):
    input_path = Path(raw_input)
    output_path = Path(processed_output)
    output_path.parent.mkdir(parents=True, exist_ok=True)

    html_content = input_path.read_text(encoding="utf-8")
    soup = BeautifulSoup(html_content, "html.parser")

    for tag in soup([
        "script", "style", "nav", "footer", "aside",
        "noscript", "form", "button", "svg"
    ]):
        tag.decompose()

    article = soup.find("article") or soup.find("main") or soup.body

    paragraphs = []
    seen = set()

    for tag in article.find_all(["h1", "h2", "h3", "p", "li"]):
        text = clean_text(tag.get_text(" ", strip=True))

        if not text:
            continue

        # Skip very short noise fragments
        if len(text) < 3:
            continue

        # Avoid duplicate repeated page elements
        if text in seen:
            continue

        seen.add(text)
        paragraphs.append(text)

    content = "\n\n".join(paragraphs)

    title = metadata.get("title", "Untitled Webpage")
    source_type = metadata.get("source_type", "webpage")
    organization = metadata.get("organization", "")
    url = metadata.get("url", "")
    topics = ", ".join(metadata.get("topics", []))

    markdown = f"""# {title}

Source Type: {source_type}
Organization: {organization}
Source URL: {url}
Topics: {topics}

## Content

{content}
"""

    with open(output_path, "w", encoding="utf-8") as f:
        f.write(markdown)