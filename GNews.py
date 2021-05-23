from GoogleNews import GoogleNews



def get_search(start_date, end_date, target): 
    googlenews = GoogleNews()
    googlenews = GoogleNews(lang='en')
    #googlenews = GoogleNews(period=period)
    googlenews = GoogleNews(start=start_date,end=end_date)
    googlenews = GoogleNews(encode='utf-8')
    googlenews.get_news(target)
    titles = googlenews.get_texts()
    links = googlenews.get_links()
    return titles, links

def clear_search():
    googlenews.clear()