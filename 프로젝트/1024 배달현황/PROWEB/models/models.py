#--------------------------------------------------------------------------------------
# 데이터 베이스의 테이블 정의 클래스
# -------------------------------------------------------------------------------------- 
# 모듈로딩

from PROWEB import DB




#---------------------------------------------------------------------------------------
# Result
#---------------------------------------------------------------------------------------
class Result(DB.Model):
    # 컬럼정의
    hum=DB.Column(DB.Integer,nullable=False)
    rain=DB.Column(DB.Integet,nullable=False)
    tem=DB.Column(DB.float,nullable=False)
    wind=DB.Column(DB.float,nullable=False)




