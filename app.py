from flask import Flask

from model import (
    init_db,insert_url, 
    get_url, 
    increment_visit_count, 
    get_all_urls, 
    delete_url)

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/about')
def about():
    return 'This is the about page.'

if __name__ == '__main__':
    app.run(debug=True)
    
