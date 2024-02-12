import wikipedia
from textblob import TextBlob


def summary(name="Jesus Christ", length=1):
    """Wikipedia Fetcher"""

    my_wiki = wikipedia.summary(name, length)
    return my_wiki


def search(name):
    """Search Wikipedia Pages"""

    results = wikipedia.search(name)
    return results


def phrases(name):
    """Return phrases from Wikipedia"""

    page = summary(name)
    blob = TextBlob(page)
    return blob.noun_phrases
