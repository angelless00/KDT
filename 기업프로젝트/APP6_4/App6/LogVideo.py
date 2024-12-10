from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.QtGui import QPixmap, QImage
import sys
import time, datetime
import cv2
from time import sleep
from PyQt5.QtCore import (QThread,pyqtSignal)  # 영상 처리 멀티스레드 // 메인스레드 - 영상용 스레드 신호 연결 목적
from PyQt5 import QtWidgets, QtGui, QtCore
import os, datetime  # 영상 정보 띄우기 목적, datetime
from PyQt5.QtGui import QPainter, QPen, QColor, QBrush
from PyQt5.QtCore import Qt
import threading
from collections import deque 
import warnings
warnings.simplefilter("ignore", DeprecationWarning) # deprecated 오류메세지 ignore 목적


class video_saver(QThread):
    def __init__(self, singal):
        super().__init__()

    
    # 1. 결국 deque 도르마무 (600프레임 기준 3.6기가)
    # 1-1. 30프레임 기준인데 ... 20프레임이나 10프레임으로 낮추고 20초 = 2.4기가
    # 1-2. 20프레임 기준, 
    # 2. 




# class ThreadOflogVideo(QThread, form_class):
#     logvideo_signal = pyqtSignal(QPixmap)
#     log_frame_signal = pyqtSignal(int, float, int)  # length, fps, 현재 프레임 번호 전송
#     # 로그 비디오를 비디오를 남길건데?
#     # 얘는 로그가 만들어지면 그 로그의 정보값을 받아서 그 영상의 시간에 가서 일부를 저장하는 것이에요~~~~
#     # 그럼? 로그가 남겨질 당시의 영상 프레임도 받아오야게쌍르미ㅏㅡㅏㅣㄹㅇ느ㅏㅣㅇㅁㄴㅀㅅ가ㅣㅢㅇ휴
#     def __init__(self, signal, video_file):
#         super().__init__()
#         self.video_file = video_file
#         self.signal = signal
#         self.fps = 0
#         self.current_time = 0
#         self.length = 0
#         self.playing_frame = None

#     def fps_receiver(self, length, fps,current_time):
#         self.length = length
#         self.fps = fps
#         self.current_time = current_time
#         print("fps_receiver 실행 완.")
#         print(self.length,self.fps, self.current_time)

#     def run(self):
#         cap = cv2.VideoCapture(self.video_file)  # 저장된 영상 가져오기 프레임별로 계속 가져오는 듯
#         self.w = round(cap.get(cv2.CAP_PROP_FRAME_WIDTH))   # 프레임 넓이
#         self.h = round(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))  # 프레임 높이
#         if self.current_time == 0:
#             self.signal.log_fps_signal.connect(self.fps_receiver)   # 슬라이드바 상태 따라서 메인뷰에서 fps값 갱신받기

#         # length, fps, current_time 받아서 
#         # 길이가 총 길이 / length/fps 하면 총 시간 

#         # 처음에 시작 프레임 번호 받고 거따가 -10 해서 20만큼 흘러갈 동안만 while문 반복.
#         # self.current_time 에서 -length/fps*10 그리고  +10 되는 구간에서 스탑.
#         print("현재 시간으으응륾아ㅣㅡㅇㄴ르ㅏㅇ랑ㄹㄹㄹ라아아악",self.current_time)
#         self.playtime = 20*self.fps + self.current_time*self.fps
#         # self.running = True
#         # 현재 프레임 번호는 ... length/fps (총 시간)   120초
#         # current_time  (현재 시간) 60초 << 시간*fps 하면 현재 프레임 번호구나!
#         self.fourcc = cv2.VideoWriter_fourcc(*'mp4v')
#         out = cv2.VideoWriter('결과물 테스트.mp4', self.fourcc, self.fps, (self.w, self.h))
        
#         cap.set(cv2.CAP_PROP_POS_FRAMES, self.fps*self.current_time)               # , b 값으로 프레임 번호를 바꿈.

#         while True:
#             self.ret, self.frame = cap.read()
#             if not self.ret:
#                 break
#             # self.ret, self.frame = cap.read()
#             self.playing_frame = int(cap.get(cv2.CAP_PROP_POS_FRAMES))
#             if self.playing_frame ==  self.playtime:
#                 break
#             out.write(self.frame)
#         out.release()
#         cap.release()


        # self.fps

        # self.log_frame_signal.connect() # 로고 프레임 번호 받아오기

        # self.logvideo_signal.connect()
        
        # self.length = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
        # self.fps = cap.get(cv2.CAP_PROP_FPS)
        # self.signal.info_signal.emit(self.length, self.fps)

        # self.current_time = cap.get(cv2.CAP_PROP_POS_MSEC) * 0.001  # 밀리초 단위 현재 위치
        # self.signal.video_playing_signal.emit(self.current_time)  # video_playing_signal을 통해 메인쓰레드로 변수 전송
        # self.signal.silder_signal.emit(self.length, self.fps, self.current_time)

            # self.video_frame.setPixmap(self.p)  # NoneType 오류가 계속 떠요
            # 위 코드에서 아래 코드로 바꾸니까 강제 종료 되던 것이 해결이 .. 되었음.
        # self.pixmap_signal.emit(self.p)

        # cv2.VideoWriter(filename, fourcc, fps, frameSize, isColor=None) 
        # • filename : 비디오 파일 이름 (e.g. 'video.mp4')
        # • fourcc : fourcc (e.g. cv2.VideoWriter_fourcc(*'DIVX'))
        # • fps : 초당 프레임 수 (e.g. 30)
        # • frameSize : 프레임 크기. (width, height) 튜플.
        # • isColor : 컬러 영상이면 True, 그렇지않으면 False. 기본값은 True입니다.
        # • retval : cv2.VideoWriter 객체
