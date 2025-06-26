from flask import Flask
from flask import request

app=Flask(__name__)

app.app_context().push()

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'GET':
        return 'This is Home Page'