#----------------------------------------------------------------------------
# Flask Framework에서 모듈단위 URL 처리 파일
# - 파일명 : main_view.py
# -----------------------------------------------------------------------------
# 모듈로딩
from flask import Blueprint,render_template,url_for,request
#from PROWEB.models.models import Result
from werkzeug.utils import redirect
import torch


# Blueprint 인스턴스 생성
mainBP=Blueprint('main',
                 import_name=__name__,
                 url_prefix='/',
                 template_folder='templates')

model=torch.load('PROWEB/models/best_model1.pth',weights_only=False)

# http://localhost:5000/ URL처리 라우팅 함수 정의
@mainBP.route('/',methods=('GET','POST'))
def index():
    result=0
    if request.method=='POST':
        hum=float(request.form['hum'])
        rain =float(request.form['rain'])
        tem =float(request.form['tem'])
        wind=float(request.form['wind'])
        result=model(torch.FloatTensor([hum,rain,tem,wind])).item()
        return redirect(url_for('main.Result',result=result))
    return render_template('index.html')
    #return redirect(url_for('main.Result',result=0))




@mainBP.route('/result',methods=('POST','GET'))
def Result():
    # if request.method=='POST':
    #     hum=float(request.form['hum'])
    #     rain =float(request.form['rain'])
    #     tem =float(request.form['tem'])
    #     wind=float(request.form['wind'])
    #     result=model(torch.FloatTensor([hum,rain,tem,wind])).item()
    #     return redirect(url_for('main.Result',result=result))

    result = request.args.get('result', 0) 
    return render_template('index copy.html',result=result)
    #return redirect(url_for('main.Result',result=result))

