from flask import Flask,render_template 

APP=Flask(__name__)

@APP.route('/')
def main():
    return render_template('main.html')


if __name__=='__main__':
    # Flask Web Server 구동
    APP.run()