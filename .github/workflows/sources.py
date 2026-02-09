import feedparser
from datetime import datetime, timedelta

EU_KEYWORDS = [
    "europe", "eu", "remote", "germany", "france", "netherlands",
    "spain", "italy", "portugal", "poland", "sweden"
]

def get_jobs():
    feeds = [
        "https://weworkremotely.com/categories/remote-programming-jobs.rss",
        "https://remoteok.com/remote-dev-jobs.rss",
    ]

    jobs = []
    one_week_ago = datetime.now() - timedelta(days=7)

    for feed_url in feeds:
        feed = feedparser.parse(feed_url)

        for entry in feed.entries:
            published = datetime(*entry.published_parsed[:6])

            if published < one_week_ago:
                continue

            text = (entry.title + entry.get("summary", "")).lower()

            if not any(k in text for k in EU_KEYWORDS):
                continue

            jobs.append({
                "title": entry.title,
                "company": entry.get("author", "Unknown"),
                "link": entry.link,
                "date": published.strftime("%Y-%m-%d")
            })

    return jobs
