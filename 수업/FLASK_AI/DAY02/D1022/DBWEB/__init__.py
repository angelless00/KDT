#------------------------------------------------------------------------------
#모듈로딩
from flask import Flask

# DB 관련 설정
import config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

DB= SQLAlchemy()
MIGRATE=Migrate()


#-------------------------------------------------------------------------------------
# Application 생성 함수
# - 함수명 : create_app <== 이름변경불가!!
#--------------------------------------------------------------------------------------- 
def create_app():
    # Flask Web Server 인스턴스 생성
    APP=Flask(__name__)

    # DB 관련 초기화 설정
    APP.config.from_object(config)

    # DB 초기화 및 연동
    DB.init_app(APP)
    MIGRATE.init_app(APP,DB)

    # URL 처리 모듈 등록
    from .views import main_view
    APP.register_blueprint(main_view.mainBP)

    
    return APP



















