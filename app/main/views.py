from flask import render_template, request, redirect, url_for
from .import main
from ..requests import get_news


#views
@main.route('/')  #localhost:5000/
def index():

    '''
    View root page function that returns the index page and its data
    '''
    # Getting popular news
    
    business_news = get_news('business')
    sports_news = get_news('sports')
    technology_news = get_news('technology')

    title = 'Home - Welcome to The best News Review Website Online'

    search_news = request.args.get('news_query')

    if search_news:
        return redirect(url_for('main.search', news_name=search_news))
    else:
        return render_template('index.html', title=title, business=business_news, sports=sports_news, technology=technology_news)


@main.route('/news/<id>')
def news(id):
    '''
    View news page function that returns the news details page and its data
    '''
    news = get_news(id)
    title = f'{id}'

    search_news = request.args.get('news_query')

    if search_news:
        return redirect(url_for('main.search', news_name=search_news))
    else:
        return render_template('news.html', title=title, news=news)
        
