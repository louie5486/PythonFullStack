from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/test')
def test():
    ls =[1,2,3,4]
    return str(ls)

if __name__ == '__main__':
    app.run()
