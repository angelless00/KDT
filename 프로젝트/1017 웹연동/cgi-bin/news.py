# 위에 라인 : 셀 내용을 파일로 생성/ 한번 생성후에는 마스킹

# --------------------------------------------------------------------------
# 경로 지정
# --------------------------------------------------------------------------
import sys

# --------------------------------------------------------------------------
# 모듈 로딩
# --------------------------------------------------------------------------

import torch
import os.path                          # 파일 및 폴더 관련
import cgi, cgitb                       # cgi 프로그래밍 관련
import joblib                           # AI 모델 관련
import sys, codecs                      # 인코딩 관련
from pydoc import html                  # html 코드 관련 : html을 객체로 처리?
import RNNutils
from konlpy.tag import Okt
tokenizer=Okt()

# 동작관련 전역 변수----------------------------------
SCRIPT_MODE = True                      # Jupyter Mode : False, WEB Mode : True
cgitb.enable()                          # Web상에서 진행상태 메시지를 콘솔에서 확인할수 있도록 하는 기능


MODEL_PATH=r'C:\KDT\프로젝트\1010 entertain\model\best_model3.pth'
Model = torch.load(MODEL_PATH, weights_only=False)


# 사용자 정의 함수----------------------------------------------------------
# WEB에서 사용자에게 보여주고 입력받는 함수 ---------------------------------
# 함수명 : showHTML
# 재 료 : 사용자 입력 데이터, 판별 결과
# 결 과 : 사용자에게 보여질 HTML 코드

def showHTML(text, msg):
    print("Content-Type: text/html; charset=utf-8")
    print(f"""
    
 <!DOCTYPE html>
    <html lang="en">
        <head>
            <meta charset = 'UTF-8'>
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>가을 날씨 예측</title>
            <link type="text/css" rel="stylesheet" href="../sub.css">
        </head>
        <body>
            <iframe src="../navi.html" width="100%" height="350px" frameborder="0" scrolling="no"></iframe>
            <hr/>
            <div class="content">
                <img src="../신문.png" height="200px">
                <form>
                    <textarea name="text" cols="50" rows="10" placeholder="기사 한문단을 입력하세요.">{text}</textarea><br>
                    <input type="submit">
                </form>
            </div>
            {msg}
            <hr/>
            <iframe id="footer" src="../footer.html" width="100%" height="500px" frameborder="0" scrolling="no"></iframe>
        </body>
    </html>
        """)

# ---------------------------------------------------------------------
# 함수 이름 : predice_model()
# 함수 역할 : 모델 예측 함수
# 매개 변수 : model, data
# ---------------------------------------------------------------------

# def predict_model(model, data):
#     data = [data.split(',')]
#     dataTS = torch.FloatTensor(data).reshape(1,-1)

#     # 검증 모드로 모델 설정
#     model.eval()
#     with torch.no_grad():

#         # 추론/평가
#         pre_val=model(dataTS)
#     # return pre_val
#     print(f"{msg}")

import json
with open("../1010 entertain/cgi-bin/token_to_idx.json", "r", encoding="utf-8") as f:
    token_to_idx=json.load(f)

def getname(num):
    name={0:'드라마',1:'뮤직',2:'해외연예'}
    return name[num]

def predict_model(model1, data):
    try:
        print("기사 한문단을 입력하세요.:", data) # 디버깅용 로그
        data=[data]

        newtokens=RNNutils.getToken(data,tokenizer)
        newvector=RNNutils.padding_vectorize(newtokens,token_to_idx,pad_length=30)
        newTS=torch.tensor(newvector)

        # 검증 모드로 모델 설정
        model1.eval()
        with torch.no_grad():

            # 추론/평가
            pre_y = model1(newTS)
    
        return f'이 기사는 {getname(torch.argmax(pre_y).item())} 기사 입니다.'
    
    except Exception as e:
        print(f"Error during prediction: {e}") # 에러 로그 추가
        return e

# --------------------------------------------------------------------------
# 기능 구현 
# --------------------------------------------------------------------------
# (1) WEB 인코딩 설정
if SCRIPT_MODE:
    sys.stdout = codecs.getwriter('utf-8')(sys.stdout.detach()) # 웹에서만 필요 : 표준출력을 utf-8로

# (2) 모델 로딩
if SCRIPT_MODE:
    pthfile1 = os.path.dirname(__file__)+ '\best_modelmin3.pth' # 웹상에서는 절대경로만

else:
    pthfile1 = Model

    
# langModel = joblib.load(pthfile)

# (3) WEB 사용자 입력 데이터 처리
# (3-1) HTML 코드에서 사용자 입력 받는 form 태그 영역 객체 가져오기
form = cgi.FieldStorage()

# (3-2) Form안에 textarea 태그 속 데이터 가져오기
text = form.getvalue("text", default="")


# (3-3) 판별하기
msg = ""
if len(text):
    result = predict_model(Model, text)
    msg = f"{result}"

# (4) 사용자에게 WEB 화면 제공
showHTML(text, msg)