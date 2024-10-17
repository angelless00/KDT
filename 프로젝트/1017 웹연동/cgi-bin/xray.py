# 위에 라인 : 셀 내용을 파일로 생성/ 한번 생성후에는 마스킹

# --------------------------------------------------------------------------
# 경로 지정
# --------------------------------------------------------------------------
import sys
sys.path.append(r'C:\Users\KDP-50\OneDrive\바탕 화면\Python06\MyClass')

# --------------------------------------------------------------------------
# 모듈 로딩
# --------------------------------------------------------------------------

import torch
import os.path                          # 파일 및 폴더 관련
import cgi, cgitb                       # cgi 프로그래밍 관련
import joblib                           # AI 모델 관련
import sys, codecs                      # 인코딩 관련
from pydoc import html                  # html 코드 관련 : html을 객체로 처리?
import CNNutils as utils
import cv2
from torchvision.transforms import v2
from PIL import Image

# 동작관련 전역 변수----------------------------------
SCRIPT_MODE = True                      # Jupyter Mode : False, WEB Mode : True
cgitb.enable()                          # Web상에서 진행상태 메시지를 콘솔에서 확인할수 있도록 하는 기능


MODEL_PATH=r'C:\KDT\프로젝트\0927 chestX-ray\model\best_model1.pth'
model = torch.load(MODEL_PATH, weights_only=False)


# 사용자 정의 함수----------------------------------------------------------
# WEB에서 사용자에게 보여주고 입력받는 함수 ---------------------------------
# 함수명 : showHTML
# 재 료 : 사용자 입력 데이터, 판별 결과
# 결 과 : 사용자에게 보여질 HTML 코드

def showHTML(msg):
    print("Content-Type: text/html; charset=utf-8")
    print(f"""
            <!DOCTYPE html>
        <html lang="en">
            <head>
                <meta charset = 'UTF-8'>
                <meta name="viewport" content="width=device-width, initial-scale=1.0">
                <title>X-ray 판별</title>
                <link type="text/css" rel="stylesheet" href="../sub.css">
            </head>
            <body>
                <iframe src="../navi.html" width="100%" height="350px" frameborder="0" scrolling="no"></iframe>
                <hr/>
                <h1>X-ray 사진을 넣어주세요.</h1>
                <img src="../ii2.jpg" height="200px">
                <div class="content">
                    <form method="post" enctype="multipart/form-data">
                        <input type="file" accept="img/*" name="xray" onchanege="previewImage(event)" required><br>
                        <input type="submit">
                    </form>
                </div>
                <hr/>
                {msg}
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

def get_disease(num):
    if num==0:
        disease='코로나'
    elif num==1:
        disease='정상'
    elif num==2:
        disease='폐렴'
    elif num==3:
        disease='결핵'
    return disease

def predict_model(model1, data):
    try:

#        data=cv2.imread(data)

        TT=v2.ToImage()(data)
        TT=v2.Resize(size=(256,256),interpolation=v2.InterpolationMode.BILINEAR)(TT)
        TT=TT.unsqueeze(dim=0)
        TT=v2.ToDtype(torch.float32,scale=False)(TT)


        # 검증 모드로 모델 설정
        model1.eval()
        with torch.no_grad():

            # 추론/평가
            pre_y = model(TT)
    
        return f'이 환자는 {get_disease(torch.argmax(pre_y).item())} 입니다.'
    
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
    pthfile1 = model

    
# langModel = joblib.load(pthfile)

# (3) WEB 사용자 입력 데이터 처리
# (3-1) HTML 코드에서 사용자 입력 받는 form 태그 영역 객체 가져오기
form = cgi.FieldStorage()



import io
# (3-3) 판별하기
msg='등록하세요'
if form.getvalue('xray'):
    xray=form.getvalue('xray','')
    data=Image.open(io.BytesIO(xray))
#    data=Image.open(xray)
#    data=xray
    result = predict_model(model, data)
    msg = f"{result}"
#    msg=xray
# except Exception as e :                                                                                                                                                                                                                                                                                  
#     print(e)


# (4) 사용자에게 WEB 화면 제공
showHTML(msg)