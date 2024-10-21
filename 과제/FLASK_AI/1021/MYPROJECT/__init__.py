from flask import Flask,render_template 

APP=Flask(__name__)

@APP.route('/')
def main