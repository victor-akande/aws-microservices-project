import wikipedia


def summary(name="Jesus Christ", length=1):
    """Wikipedia Fetcher"""

    my_wiki = wikipedia.summary(name, length)
    return my_wiki

def search(name):
    """Search Wikipedia Pages"""

    results = wikipedia.search(name)
    return results