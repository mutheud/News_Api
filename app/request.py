import urllib.request,json
from .models import News,Sources

# Getting api key
api_key = None
# Getting the movie base url
base_url = None

sources_url = None

articles_url = None

def configure_request(app):
    global api_key,base_url,sources_url, articles_url
    api_key = app.config['NEWS_API_KEY']
    sources_url = app.config['NEWS_API_SOURCES_URL']
    articles_url = app.config['NEWS_API_ARTICLES_URL']

def get_sources(category):
    get_news_url = sources_url.format(category, api_key)
   

    with urllib.request.urlopen(get_news_url) as url:
        
        get_news_data = url.read()
        get_news_response = json.loads(get_news_data)

        news_results = None
        # print(get_news_response)
        if get_news_response['sources']:
            news_results_list = get_news_response['sources']
            news_results = process_sources(news_results_list)
    return news_results

def process_sources(news_list):
   
    news_results = []
    
    for news_item in news_list:
        id= news_item.get('id')
        name= news_item.get('name')
        url= news_item.get('url')
        category= news_item.get('category')

        if url:    
            news_object = Sources(id,name,url,category)
            # print("dee")
            news_results.append(news_object)

    return news_results
    

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
            news_results = process_articles(news_results_list)
    return news_results


def process_articles(news_list):
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

        
        
        if description:    
            news_object = News(author,description,url,urlToImage,category,language,country)
            # print("dee")
            news_results.append(news_object)

    return news_results
        