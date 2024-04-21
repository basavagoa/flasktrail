from flask import Flask,render_template

#craete application

app=Flask(__name__)
@app.route('/')
def home():
    return "<h2>Hello world</h2>"



@app.route('/welcome')
def welcome():
    return "<h1>welcome to my website</h1>"


@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/logi')
def logi():
    return render_template('logi.html')


@app.route('/photo')
def photo():
    return render_template('photo.html')


if __name__=='__main__':
    app.run(debug=True)