import feedparser
from Scraping import get_bbc_text
from t5_model import summarize_text
from summaryToSpeech import getTextToSpeech

def get_rss_feed(url):
    feeds = feedparser.parse(url)
    response = []
    c = 0
    for entry in feeds.entries:
        if c == 1:
            break
        c += 1
        feed = {}
        feed['title'] = entry.title
        feed['url'] = entry.link
        feed['publishedDate'] = entry.published
        feed['paragraph'] = get_bbc_text(feed['url'])
        feed['llm_summary'] = summarize_text(feed['paragraph'])
        print("Calling getTextToSpeech")
        getTextToSpeech(feed['llm_summary'], "audio_1")
        response.append(feed)
    return response
