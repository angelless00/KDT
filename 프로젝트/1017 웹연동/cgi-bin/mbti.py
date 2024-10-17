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
import utils

# 동작관련 전역 변수----------------------------------
SCRIPT_MODE = True                      # Jupyter Mode : False, WEB Mode : True
cgitb.enable()                          # Web상에서 진행상태 메시지를 콘솔에서 확인할수 있도록 하는 기능

MODEL_IE=r'C:\KDT\프로젝트\0905 mbti예측\model\best_model_ie.pth'
MODEL_NS=r'C:\KDT\프로젝트\0905 mbti예측\model\best_model_ns.pth'
MODEL_FT=r'C:\KDT\프로젝트\0905 mbti예측\model\best_model_ft.pth'
MODEL_JP=r'C:\KDT\프로젝트\0905 mbti예측\model\best_model_JP.pth'
IE_model=torch.load(MODEL_IE,weights_only=False)
NS_model=torch.load(MODEL_NS,weights_only=False)
FT_model=torch.load(MODEL_FT,weights_only=False)
JP_model=torch.load(MODEL_JP,weights_only=False)


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
            <title>MBTI 예측</title>
            <link type="text/css" rel="stylesheet" href="../sub.css">
        </head>
        <body>
            <iframe src="../navi.html" width="100%" height="350px" frameborder="0" scrolling="no"></iframe>
            <hr/>
            <div class="content">
                <img src="../mbti.png" height="100px">
                <form>
                    <table>
                        <tr>
                            <td>리트윗</td>
                            <td><input type="text" name="retweet"><br></td>
                        </tr>
                        <tr>
                            <td>해시태그</td>
                            <td><input type="text" name="hash"><br></td>
                        </tr>
                        <tr>
                            <td>좋아요</td>
                            <td><input type="text" name="favor"><br></td>
                        </tr>
                        <tr>
                            <td>URL</td>
                            <td><input type="text" name="url"><br></td>
                        </tr>
                        <tr>
                            <td>멘션</td>
                            <td><input type="text" name="mension"><br></td>
                        </tr>
                        <tr>
                            <td>미디어</td>
                            <td><input type="text" name="media"><br></td>
                        </tr>
                    </table>
                    <input type="submit">
                </form>
            </div>
            <hr/>
            {msg}
            <iframe id="footer" src="../footer.html" width="100%" height="500px" frameborder="0" scrolling="no" ></iframe>
        </body>
    </html>
    """)

def predict_model(model1,model2, data):
    try:
        #print("오늘의 최저기온, 최고기온, 강수량, 습도를 입력하세요.:", data) # 디버깅용 로그
        data = map(float, data)
        dataTS = torch.FloatTensor(list(data)).reshape(1,-1)

        # 검증 모드로 모델 설정
        model1.eval()
        model2.eval()
        with torch.no_grad():

            # 추론/평가
            pre_min = model1(dataTS)
            pre_max = model2(dataTS)
        return f'내일의 최저기온은 {pre_min.item():.2f}, 최고기온은 {pre_max.item():.2f}도 입니다.'
    
    except Exception as e:
        print(f"Error during prediction: {e}") # 에러 로그 추가
        return '오류 발생!!'

# --------------------------------------------------------------------------
# 기능 구현 
# --------------------------------------------------------------------------
# (1) WEB 인코딩 설정
if SCRIPT_MODE:
    sys.stdout = codecs.getwriter('utf-8')(sys.stdout.detach()) # 웹에서만 필요 : 표준출력을 utf-8로

# (2) 모델 로딩
if SCRIPT_MODE:
    pthfile1 = os.path.dirname(__file__)+ '\best_modelmin4.pth' # 웹상에서는 절대경로만
    pthfile2 = os.path.dirname(__file__)+ '\best_modelmax1.pth'
else:
    pthfile1 = IE_model
    pthfile2 = FT_model
#     pthfile3=
#     pthfile4=
    
# langModel = joblib.load(pthfile)

# (3) WEB 사용자 입력 데이터 처리
# (3-1) HTML 코드에서 사용자 입력 받는 form 태그 영역 객체 가져오기
form = cgi.FieldStorage()

# (3-2) Form안에 textarea 태그 속 데이터 가져오기
retweet = form.getvalue("retweet", default="")
hash = form.getvalue("hash", default="")
favor = form.getvalue("favor", default="")
url = form.getvalue("url", default="")
mension = form.getvalue("mension", default="")
media=form.getvalue("media",default="")
text=[hash,retweet,favor,url,mension,media]

# (3-3) 판별하기
msg = ""
if len(text):
    result = predict_model(IE_model,FT_model, text)
    msg = f"{result}"

# (4) 사용자에게 WEB 화면 제공
showHTML( msg)