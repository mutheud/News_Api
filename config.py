import os
class Config:
    '''
    General configuration parent class
    '''
    NEWS_API_KEY = 'a604a6e8642b41c8b3c334e7dbc7cc47'
    NEWS_API_SOURCES_URL = 'https://newsapi.org/v2/sources?category={}&apiKey={}'
    NEWS_API_ARTICLES_URL ='https://newsapi.org/v2/top-headlines?country=us&apiKey={}'
    SECRET_KEY = os.environ.get('diana')

class ProdConfig(Config):
    '''
    Production  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''
    pass

class DevConfig(Config):
    '''
    Development  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''
    DEBUG = True
    
config_options = {
'development':DevConfig,
'production':ProdConfig
}