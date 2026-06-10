# # scripts/ingest_youtube.py

# import json
# from pathlib import Path
# from urllib.parse import urlparse, parse_qs

# from youtube_transcript_api import YouTubeTranscriptApi


# def get_video_id(url: str) -> str:
#     parsed = urlparse(url)

#     if parsed.hostname in ["www.youtube.com", "youtube.com"]:
#         return parse_qs(parsed.query)["v"][0]

#     if parsed.hostname == "youtu.be":
#         return parsed.path.lstrip("/")

#     raise ValueError("Invalid YouTube URL")


# def ingest_youtube_transcript(url: str, raw_output: str, processed_output: str) -> None:
#     video_id = get_video_id(url)

#     transcript = YouTubeTranscriptApi.get_transcript(video_id)

#     Path(raw_output).parent.mkdir(parents=True, exist_ok=True)
#     Path(processed_output).parent.mkdir(parents=True, exist_ok=True)

#     with open(raw_output, "w", encoding="utf-8") as f:
#         json.dump(transcript, f, indent=2)

#     text = "\n\n".join(item["text"] for item in transcript)

#     with open(processed_output, "w", encoding="utf-8") as f:
#         f.write(text)

#     print(f"Saved raw transcript to {raw_output}")
#     print(f"Saved processed transcript to {processed_output}")

import json
from pathlib import Path
from urllib.parse import urlparse, parse_qs

from youtube_transcript_api import YouTubeTranscriptApi


def get_video_id(url: str) -> str:
    """Extract the YouTube video ID from a YouTube URL."""
    parsed_url = urlparse(url)

    if parsed_url.hostname in ["www.youtube.com", "youtube.com"]:
        return parse_qs(parsed_url.query)["v"][0]

    if parsed_url.hostname == "youtu.be":
        return parsed_url.path.lstrip("/")

    raise ValueError(f"Invalid YouTube URL: {url}")


def download_youtube_transcript(url: str, raw_output: str) -> None:
    """Download a YouTube transcript and save the raw transcript JSON."""
    video_id = get_video_id(url)

    api = YouTubeTranscriptApi()
    fetched_transcript = api.fetch(video_id)

    transcript = [
        {
            "text": snippet.text,
            "start": snippet.start,
            "duration": snippet.duration
        }
        for snippet in fetched_transcript
    ]

    output_path = Path(raw_output)
    output_path.parent.mkdir(parents=True, exist_ok=True)

    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(transcript, f, indent=2)

    print(f"Saved raw YouTube transcript to {raw_output}")


def process_youtube_transcript(
    raw_input: str,
    processed_output: str,
    metadata: dict
) -> None:
    """Convert raw YouTube transcript JSON into clean Markdown with metadata."""
    input_path = Path(raw_input)
    output_path = Path(processed_output)

    output_path.parent.mkdir(parents=True, exist_ok=True)

    with open(input_path, "r", encoding="utf-8") as f:
        transcript = json.load(f)

    transcript_text = "\n\n".join(item["text"] for item in transcript)

    title = metadata.get("title", "YouTube Transcript")
    source_type = metadata.get("source_type", "youtube_transcript")
    organization = metadata.get("organization", "")
    url = metadata.get("url", "")
    topics = ", ".join(metadata.get("topics", []))

    markdown = f"""# {title}

Source Type: {source_type}
Organization: {organization}
Source URL: {url}
Topics: {topics}

## Content

{transcript_text}
"""

    with open(output_path, "w", encoding="utf-8") as f:
        f.write(markdown)

    print(f"Saved processed YouTube transcript to {processed_output}")

# if __name__ == "__main__":
#     print(get_video_id('https://www.youtube.com/watch?v=jWWHa5XdvDQ'))