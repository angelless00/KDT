import sys
from PyQt5.QtGui import QPixmap, QPainter, QPen
from PyQt5.QtCore import Qt, pyqtSignal
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QGridLayout, QWidget
from PyQt5 import uic

# UI 파일 로드
form_class = uic.loadUiType("drawing.ui")[0]

class Drawing(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        
        # PaintView 인스턴스 하나만 생성
        self.paintview = PaintView(self.drawingArea)
        self.paintview.setGeometry(self.drawingArea.rect())
        
        self.rect_x1 = None
        self.rect_y1 = None
        self.rect_x2 = None
        self.rect_y2 = None
        
        # 시그널 연결
        self.paintview.rect_signal.connect(self.xy_position)
        
        # 라디오 버튼 이벤트 연결
        self.radioBtn_rec1.clicked.connect(self.recxy_send)
        self.radioBtn_rec2.clicked.connect(self.recxy_send)
        self.radioBtn_rec3.clicked.connect(self.recxy_send)

    def recxy_send(self):
        if self.radioBtn_rec1.isChecked():
            print("[rec1]", end=" ")
            self.paintview.rect_type = 1
        elif self.radioBtn_rec2.isChecked():
            print("[rec2]", end=" ")
            self.paintview.rect_type = 2
        elif self.radioBtn_rec3.isChecked():
            print("[rec3]", end=" ")
            self.paintview.rect_type = 3
        
        if self.rect_x1 is not None:
            print(f"x1: {self.rect_x1}, y1: {self.rect_y1}, x2: {self.rect_x2}, y2: {self.rect_y2}")

    def xy_position(self, x1, y1, x2, y2):
        self.rect_x1 = x1
        self.rect_y1 = y1
        self.rect_x2 = x2
        self.rect_y2 = y2
        print(f"x1: {self.rect_x1}, y1: {self.rect_y1}, x2: {self.rect_x2}, y2: {self.rect_y2}")

class PaintView(QLabel):
    rect_signal = pyqtSignal(int, int, int, int)

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setMouseTracking(True)
        
        # 변수 초기화
        self.past_x = None
        self.past_y = None
        self.present_x = None
        self.present_y = None
        self.rect_x1 = None
        self.rect_y1 = None
        self.rect_x2 = None
        self.rect_y2 = None
        self.rect_type = None
        self.drawing = False
        
        # 배경 이미지 로드
        self.img = QPixmap("back.png")
        self.setPixmap(self.img)

    def paintEvent(self, event):
        painter = QPainter(self)
        # 배경 이미지 그리기
        painter.drawPixmap(0, 0, self.img)
        
        # 사각형 그리기
        if self.drawing and self.past_x is not None and self.present_x is not None:
            painter.setPen(QPen(Qt.black, 3, Qt.SolidLine))
            
            # 사각형 좌표 계산
            x = min(self.past_x, self.present_x)
            y = min(self.past_y, self.present_y)
            width = abs(self.present_x - self.past_x)
            height = abs(self.present_y - self.past_y)
            
            painter.drawRect(x, y, width, height)
            
            # 좌표 저장
            self.rect_x1 = x
            self.rect_y1 = y
            self.rect_x2 = width
            self.rect_y2 = height
            
            # 시그널 발생
            self.rect_signal.emit(self.rect_x1, self.rect_y1, self.rect_x2, self.rect_y2)

    def mousePressEvent(self, event):
        self.drawing = True
        self.past_x = event.x()
        self.past_y = event.y()

    def mouseMoveEvent(self, event):
        if self.drawing:
            self.present_x = event.x()
            self.present_y = event.y()
            self.update()

    def mouseReleaseEvent(self, event):
        if self.drawing:
            self.present_x = event.x()
            self.present_y = event.y()
            self.drawing = False
            self.update()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = Drawing()
    myWindow.show()
    sys.exit(app.exec_())