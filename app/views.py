from flask import render_template
from app import app
from .request import get_news
#views

@app.route('/')
def index():
    '''
    View root page function that returns the index page and its data
    '''
    message = 'NEWS-FLASH'
    
    
    # news = get_news()
    
    news= get_news()
    print(news)
    
    title = 'Home - Beyond the Headlines'
    return render_template('index.html', title = title, news = news)
