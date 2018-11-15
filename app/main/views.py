from flask import render_template,request,redirect,url_for
from . import main
from ..request import get_news,get_sources

#views

@main.route('/')
def sources():
    businness_news = get_sources('business')
    entertainment_news  = get_sources('entertainment')
    general_news  = get_sources('general')
    health_news  = get_sources('health')
    science_news  = get_sources('science') 
    sports_news  = get_sources('sports')
    technology_news  = get_sources('technology')
    title = 'Home - Beyond the Headlines'
    return render_template('index.html', title = title, business = businness_news,entertainment= entertainment_news,general = general_news,health = health_news,science =science_news,sports = sports_news,technology=technology_news)

@main.route('/headlines')
def index():
    '''
    View root page function that returns the index page and its data
    '''
    message = 'NEWS-FLASH'
    
    
    # news = get_news()
    
    news= get_news()
    print(news)
    
    title = 'Home - Beyond the Headlines'
    return render_template('headlines.html', title = title, news = news)
