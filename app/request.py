from app import app
import urllib.request,json
from .models import *



# # Getting api key
# api_key = None
# base_url = None


api_key = app.config['NEWS_API_KEY']
sources_url = app.config['NEWS_API_SOURCES_URL']
  

def get_news():
    '''
    Function that gets the json response to our url request  
    '''
    get_news_url = sources_url.format(api_key)
   

    with urllib.request.urlopen(get_news_url) as url:
        
        get_news_data = url.read()
        get_news_response = json.loads(get_news_data)

        news_results = None
        # print(get_news_response)
        if get_news_response['sources']:
            news_results_list = get_news_response['sources']
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
        id= news_item.get('id')
        name= news_item.get('name')
        description= news_item.get('description')
        url= news_item.get('url')
        category= news_item.get('category')
        language= news_item.get('language')
        country= news_item.get('country')
        
        
            
        news_object = (id,name,description,url,category,language,country)
        # print("dee")
        news_results.append(news_object)

    return news_results
        