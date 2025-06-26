from flask import Flask
from flask import request

app=Flask(__name__)

app.app_context().push()

@app.route('/', methods=['GET'])
def home():
    if request.method == 'GET':
        return 'This is Home Page'
    
if __name__ == '__main__':
    app.run(host='0.0.0.0',port=8000,debug=True)   
