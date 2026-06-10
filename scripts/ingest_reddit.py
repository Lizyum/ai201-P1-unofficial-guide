import json
from pathlib import Path


def extract_comments(comment_children):
    """Recursively extract non-deleted Reddit comments."""
    comments = []

    for child in comment_children:
        if child.get("kind") != "t1":
            continue

        data = child.get("data", {})
        body = data.get("body", "").strip()

        if body and body not in ["[deleted]", "[removed]"]:
            comments.append(body)

        replies = data.get("replies")
        if isinstance(replies, dict):
            nested_children = replies.get("data", {}).get("children", [])
            comments.extend(extract_comments(nested_children))

    return comments


def process_reddit_json(raw_input: str, processed_output: str, metadata: dict) -> None:
    """Convert raw Reddit JSON into clean Markdown with metadata."""
    input_path = Path(raw_input)
    output_path = Path(processed_output)
    output_path.parent.mkdir(parents=True, exist_ok=True)

    with open(input_path, "r", encoding="utf-8") as f:
        reddit_data = json.load(f)

    post = reddit_data[0]["data"]["children"][0]["data"]
    comments_root = reddit_data[1]["data"]["children"]

    post_title = post.get("title", metadata.get("title", "Reddit Thread"))
    post_body = post.get("selftext", "").strip()
    subreddit = post.get("subreddit", "")
    url = metadata.get("url", "")

    title = metadata.get("title", post_title)
    source_type = metadata.get("source_type", "reddit_thread")
    organization = metadata.get("organization", f"r/{subreddit}")
    topics = ", ".join(metadata.get("topics", []))

    comments = extract_comments(comments_root)

    markdown = f"""# {title}

Source Type: {source_type}
Organization: {organization}
Source URL: {url}
Topics: {topics}

## Original Post

{post_body}

## Comments

"""

    for i, comment in enumerate(comments, start=1):
        markdown += f"### Comment {i}\n\n{comment}\n\n"

    with open(output_path, "w", encoding="utf-8") as f:
        f.write(markdown)

    print(f"Saved processed Reddit thread to {processed_output}")