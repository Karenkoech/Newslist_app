import urllib.request,json
from .models import News,Reviews

# News=news.News


#Getting api key
api_key = None

#Getting the news base url
base_url = None

def configure_request(app):
    global api_key,base_url
    api_key = app.config['NEWS_API_KEY']
    base_url = app.config['NEWS_API_BASE_URL']

def get_news(category):
    '''
    Function that gets the json response to our url request
    '''
    get_news_url = 'https://newsapi.org/v2/top-headlines?category={}&apiKey=09bbf4df6e5647aab35b0fa99a9beac4'.format(category)
    print (get_news_url)

    with urllib.request.urlopen(get_news_url) as url:
        get_news_data = url.read()
        get_news_response = json.loads(get_news_data)

        news_results = None

        if get_news_response['articles']:
            news_results_list = get_news_response['articles']
            news_results = process_results(news_results_list)

    return news_results

def process_results(news_results_list):
    '''
    Function that processes the news result and transform them to a list of Objects
    Args:
        news_results_list: A list of dictionaries that contain news details
    Returns:
        news_results: A list of news objects
    '''
    news_results = []
    for news_item in news_results_list:
        id = news_item.get('id')
        title = news_item.get('title')
        description = news_item.get('description')
        url = news_item.get('url')
        urlToImage = news_item.get('urlToImage')
        publishedAt = news_item.get('publishedAt')
        content = news_item.get('content')

        if urlToImage:
            news_object = News(id,title,description,url,urlToImage,publishedAt,content)
            news_results.append(news_object)

    return news_results

    



