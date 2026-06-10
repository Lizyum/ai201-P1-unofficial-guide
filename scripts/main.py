from ingest_webpage import save_html, process_html_to_markdown
from ingest_youtube import download_youtube_transcript, process_youtube_transcript
from ingest_reddit import process_reddit_json

web_sources = [
    {
        "url": "https://dailynorthwestern.com/2022/11/16/audio/digital-diaries-episode-7-life-as-a-first-generation-and-or-low-income-student/",
        "raw_output": "documents/raw/daily_northwestern_DD_EP7.html",
        "processed_output": "documents/processed/daily_northwestern_DD_EP7.md",
        "title": "Digital Diaries Episode 7",
        "source_type": "news_journal_transcript",
        "organization": "The Daily Northwestern",
        "topics": ["fgli", "belonging", "community", "financial_aid"]
    },
    {
        "url": "https://admissionblog.northwestern.edu/2022/11/08/advice-for-fgli-students-northwestern/",
        "raw_output": "documents/raw/admission_blog_fgli_advice.html",
        "processed_output": "documents/processed/admission_blog_fgli_advice.md",
        "title": "Advice for FGLI Students",
        "source_type": "admission_blog",
        "organization": "Northwestern Admissions",
        "topics": ["fgli", "transition_to_college", "resources", "community"]
    },
    {
        "url": "https://admissionblog.northwestern.edu/2019/10/22/carter-finding-home-at-northwestern-as-a-first-gen-low-income-student/",
        "raw_output": "documents/raw/admission_blog_carter_finding_home.html",
        "processed_output": "documents/processed/admission_blog_carter_finding_home.md",
        "title": "Finding Home at Northwestern as a First-Gen Low-Income Student",
        "source_type": "student_story",
        "organization": "Northwestern Admissions",
        "topics": ["fgli", "belonging", "identity", "community"]
    },
    {
        "url": "https://www.northwestern.edu/studentaffairs/sass/",
        "raw_output": "documents/raw/northwestern_sass.html",
        "processed_output": "documents/processed/northwestern_sass.md",
        "title": "Student Assistance and Support Services",
        "source_type": "official_resource",
        "organization": "Northwestern Student Affairs",
        "topics": ["resources", "student_support", "financial_hardship", "wellbeing"]
    },
    {
        "url": "https://searle.northwestern.edu/resources/learning-teaching-guides/first-generation-college-student-page.html",
        "raw_output": "documents/raw/searle_first_generation_resources.html",
        "processed_output": "documents/processed/searle_first_generation_resources.md",
        "title": "First Generation College Student Resources",
        "source_type": "official_resource",
        "organization": "Searle Center",
        "topics": ["fgli", "academic_success", "resources"]
    },
    {
        "url": "https://northbynorthwestern.com/discountedu-ep-6-intersectionality-latine-fgli/",
        "raw_output": "documents/raw/northbynorthwestern_discountedu_ep6.html",
        "processed_output": "documents/processed/northbynorthwestern_discountedu_ep6.md",
        "title": "DiscountEDU Episode 6: Intersectionality and Latine FGLI",
        "source_type": "newsletter_article",
        "organization": "North by Northwestern",
        "topics": ["fgli", "latine", "identity", "intersectionality"]
    }
]

youtube_sources = [
    {
        "url": "https://www.youtube.com/watch?v=rhX9eEovYug",
        "raw_output": "documents/raw/youtube_fgli_alumni_panel.json",
        "processed_output": "documents/processed/youtube_fgli_alumni_panel.md",
        "title": "FGLI Alumni Panel",
        "source_type": "youtube_transcript",
        "organization": "Northwestern",
        "topics": ["fgli", "alumni", "career", "mentorship"]
    },
    {
        "url": "https://www.youtube.com/watch?v=jWWHa5XdvDQ",
        "raw_output": "documents/raw/youtube_fgli_narratives.json",
        "processed_output": "documents/processed/youtube_fgli_narratives.md",
        "title": "FGLI Narratives",
        "source_type": "youtube_transcript",
        "organization": "Northwestern",
        "topics": ["fgli", "identity", "belonging", "student_experience"]
    }
]

reddit_sources = [
    {
        "url": "https://www.reddit.com/r/evanston/comments/1min35y/where_to_go_to_get_the_northwestern_experience/",
        "raw_output": "documents/raw/reddit_thread_01.json",
        "processed_output": "documents/processed/reddit_northwestern_experience.md",
        "title": "Where to go to get the Northwestern experience",
        "source_type": "reddit_thread",
        "organization": "r/evanston",
        "topics": ["northwestern_experience", "community", "campus_life"]
    },
    {
        "url": "https://www.reddit.com/r/Northwestern/comments/1th3sjt/isolating_firstgen_experience/",
        "raw_output": "documents/raw/reddit_thread_02.json",
        "processed_output": "documents/processed/reddit_isolating_firstgen_experience.md",
        "title": "Isolating First-Gen Experience",
        "source_type": "reddit_thread",
        "organization": "r/Northwestern",
        "topics": ["fgli", "first_generation", "belonging", "isolation"]
    }
]

# ingesting raw website html for each web page source

def ingest_webpages():
    for source in web_sources:
        save_html(
            url=source["url"],
            output_path=source["raw_output"]
        )

        process_html_to_markdown(
            raw_input=source["raw_output"],
            processed_output=source["processed_output"],
            metadata=source
        )

#ingesting raw youtube transcripts

def ingest_youtube():
    for source in youtube_sources:
        download_youtube_transcript(
            url=source["url"],
            raw_output=source["raw_output"]
        )

        process_youtube_transcript(
            raw_input=source["raw_output"],
            processed_output=source["processed_output"],
            metadata=source
    )
        
def ingest_reddit():
    for source in reddit_sources:
        process_reddit_json(
            raw_input=source["raw_output"],
            processed_output=source["processed_output"],
            metadata=source
        )


if __name__ == "__main__":
    # Comment/uncomment depending on what you want to test
    ingest_webpages()
    # ingest_youtube()
    # ingest_reddit()