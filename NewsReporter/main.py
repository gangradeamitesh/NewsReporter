from flask import Flask, jsonify , request
from GetFeeds import get_rss_feed
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import text

app = Flask(__name__)




@app.route("/")
def hellp_world():
    return "Hello World"

@app.route("/getData", methods=['GET'])
def get_data():
    print(url)
    return jsonify(get_rss_feed(url))

if __name__ == '__main__':
    url = "http://feeds.bbci.co.uk/news/technology/rss.xml"
    print("Running the main function")
    app.run(host='0.0.0.0', port=80,debug=True)