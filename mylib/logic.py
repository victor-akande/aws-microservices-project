import wikipedia


def wiki(name="Jesus Christ", length=1):
    """Wikipedia Fetcher"""

    my_wiki = wikipedia.summary(name, length)
    return my_wiki
