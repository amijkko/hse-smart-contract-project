from app import app
from flask import request, render_template, flash, redirect
from .search import mapping

from extract_from_contract import get_title, get_url


@app.route('/', methods=['GET', 'POST'])
@app.route('/search', methods=['GET', 'POST'])
def search():
    if request.method == 'POST':
        search_str = request.form['search']
        result = get_title(search_str)
        result_url = get_url(search_str)
        if result is None:
            result = 'На ваш запрос нет результатов'
        src_url = "https://www.bing.com/search?q={}".format(search_str)
        return render_template('result.html', title='Result', result=result,
                            result_url=result_url, src_url=src_url)
    return render_template('search.html', title='Search')
