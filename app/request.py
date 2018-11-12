from app import app
import urllib.request,json
from .models import news
News = news.News

# # Getting api key
# api_key = None
# base_url = None


api_key = app.config['NEWS_API_KEY']
articles_url = app.config['NEWS_API_ARTICLES_URL']
  

def get_news():
    '''
    Function that gets the json response to our url request  
    '''
    get_news_url = articles_url.format(api_key)
   

    with urllib.request.urlopen(get_news_url) as url:
        
        get_news_data = url.read()
        get_news_response = json.loads(get_news_data)

        news_results = None
        # print(get_news_response)
        if get_news_response['articles']:
            news_results_list = get_news_response['articles']
            news_results = process_results(news_results_list)
    return news_results


def process_results(news_list):
    '''
    Function  that processes the news result and transform them to a list of Objects

    Args:
        news_list: A list of dictionaries that contain news details

    Returns :
        news_results: A list of news objects
    '''
    news_results = []
    
    for news_item in news_list:
        author= news_item.get('author')
        # name= news_item.get('name')
        description= news_item.get('description')
        url= news_item.get('url')
        urlToImage = news_item.get('urlToImage')
        category= news_item.get('category')
        language= news_item.get('language')
        country= news_item.get('country')

        
        
        if urlToImage:    
            news_object = News(author,description,url,urlToImage,category,language,country)
            # print("dee")
            news_results.append(news_object)

    return news_results
        