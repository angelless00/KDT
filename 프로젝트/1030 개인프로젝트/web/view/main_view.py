# Flask Framework에서 모듈단위 URL 처리 파일
# - 파일명 : main_view.py
# -----------------------------------------------------------------------------
# 모듈로딩
from flask import Blueprint,render_template,url_for,request
#from PROWEB.models.models import Result
from werkzeug.utils import redirect
import torch
import RNNutils as utils
from konlpy.tag import Okt
tokenizer=Okt()


# Blueprint 인스턴스 생성
mainBP=Blueprint('main',
                 import_name=__name__,
                 url_prefix='/',
                 template_folder='templates')

model=torch.load('model/best_model1.pth',weights_only=False,map_location='cpu')


import json
with open("token_to_idx.json", "r", encoding="utf-8") as f:
    token_to_idx=json.load(f)
with open("idx_to_token.json", "r", encoding="utf-8") as f:
    idx_to_token=json.load(f)

def before(text):
    songtoken=utils.getToken(text,tokenizer)
    songvector=utils.vectorize(songtoken,token_to_idx)
    result=[]
    for vector in songvector:
        for vv in vector:
            if vv is not None:
                result.append(vv)
    return torch.tensor([result[-3:]])



# http://localhost:5000/ URL처리 라우팅 함수 정의
@mainBP.route('/',methods=('GET','POST'))
def index():
    if request.method=='POST':
        st_text=request.form['start']
        length=int(request.form['length'])
        while len(st_text)<length:
            st_text=st_text+' '+str(idx_to_token[str(torch.argmax(model(before(st_text))).item())])
        return redirect(url_for('main.Result',result=st_text))
    return render_template('main.html')
    #return redirect(url_for('main.Result',result=0))

@mainBP.route('navi')
def navi():
    return render_template('navi.html')

@mainBP.route('/result',methods=('POST','GET'))
def Result():
    result = request.args.get('result', '가사생성실패') 
    return render_template('result.html',result=result)