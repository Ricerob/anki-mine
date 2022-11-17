import yake
from bs4 import BeautifulSoup
from requests import get


def content_scraper(url):
    total_text = ""
    res = get(url).text
    soup = BeautifulSoup(res, 'html.parser')
    for p in soup.find_all('p'):
        total_text += p.text.strip()
        total_text += '\n'
    print(total_text)
    return total_text


if __name__ == '__main__':
    url = input("URL: \n")
    language = input("Language: \n")
    text = content_scraper(url)
    max_ngram_size = 3
    deduplication_threshold = 0.8
    numOfKeywords = 10
    kw_extractor = yake.KeywordExtractor(lan=language, n=max_ngram_size, dedupLim=deduplication_threshold,
                                         top=numOfKeywords, features=None)
    keywords = kw_extractor.extract_keywords(text)
    for kw in keywords:
        print(kw)
