# 한글 폰트 설정 => 폰트 매니저 모듈 사용
from matplotlib import font_manager as fm
from matplotlib import rc

# 적용할 폰트 파일
Font_file=r'C:\Windows\Fonts\gulim.ttc'

# 폰트 패밀리 이름 가져오기
font_name=fm.FontProperties(fname=Font_file).get_name()

# 새로운 폰트 패밀리 이름지정
rc('font',family=font_name)