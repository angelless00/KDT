from flask import Flask,render_template 

def create_app():
    APP=Flask(__name__)

    @APP.route('/navi')
    def navi():
        return render_template('navi.html')
    
    @APP.route('/footer')
    def footer():
        return render_template('footer.html')

    @APP.route('/')
    def main():
        return render_template('main.html')

    @APP.route('/mbti')
    def mbti():
        return render_template('mbti.html')
    
    @APP.route('/weather')
    def weather():
        return render_template('weather.html')
    
    @APP.route('/xray')
    def xray():
        return render_template('xray.html')   
    
    @APP.route('/news')
    def news():
        return render_template('news.html')


    return APP

    

APP=create_app()


if __name__=='__main__':
    # Flask Web Server 구동
    APP.run()
    