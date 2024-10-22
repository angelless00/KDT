#-------------------------------------------------------------------------------------------------------
# Flask Framework에서 '/'에 대한 라우팅 처리 파일
# - 파일명 : main_views.py
#-------------------------------------------------------------------------------------------------------
# 모듈로딩-----------------------------------------------------------------------------------------------

from flask import Blueprint,render_template 

# Blueprint 인스턴스 생성----------------------------------------------------------------------
main_bp=Blueprint('main',
                  __name__,
                  url_prefix='/',
                  template_folder='templates')
# __name__ 처음에는 main, import 될떄는 파일명

## 라우팅 기능 함수 정의---------------------------------------------------------------------------
@main_bp.route('/',endpoint='hello')
def index():
    return render_template('index.html')





