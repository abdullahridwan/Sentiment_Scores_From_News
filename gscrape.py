import requests
import bs4

# Make two strings with default google search URL
# 'https://google.com/search?q=' and
# our customized search keyword.
# https://news.google.com/topstories?hl=en-US&gl=US&ceid=US:en&q=nursing+home

def get_info(text):
    query_root = "https://news.google.co.in/"
    url = query_root + text
    request_result = requests.get(url)
    soup = bs4.BeautifulSoup(request_result.text,
                            "html.parser")
    heading_object = soup.find_all('h3')
    headings_list = []

    for info in heading_object:
        print(info.getText())
        headings_list.append(info.getText())