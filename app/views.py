from flask import render_template
from app import app

#views

@app.route('/index/<int:index_id>')
def index(index_id):
    '''
    View root page function that returns the index page and its data
    '''
    message = 'NEWS-FLASH'
    title = 'Home - Beyond the Headlines '
    
    return render_template('index.html',id = index_id,message =message,title =title)