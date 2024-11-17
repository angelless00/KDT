import torch
from ultralytics import YOLO
import os
import cv2


def auto_laveler_IMG(IMAGE_PATH, model):
    """IMAGE 폴더안에 있는 모든 img 라벨링 후 라벨 텍스트 저장"""
    image_list = os.listdir(IMAGE_PATH)
    for image in image_list:
        model.predict(IMAGE_PATH + "/" + image, save_txt=True)


def video_capture(video_path, image_path, second, model):
    """
    video 캡쳐
    second=몇초마다캡쳐할건지
    """
    video = cv2.VideoCapture(video_path)
    if not os.path.exists(image_path):
        os.mkdir(image_path)
    num_frame = video.get(cv2.CAP_PROP_FPS)  # 현재 파일의 FPS
    frame_step = second * num_frame
    i = 1
    ret = True

    while ret:
        ret, frame = video.read()
        cv2.imwrite(f"{image_path}/vv{i}.jpg", frame)
        video.set(cv2.CAP_PROP_POS_FRAMES, int(i * frame_step))
        i += 1


def detect_save(IMAGE_PATH, model):
    """IMAGE_PATH안에 있는 파일중 detect 된 파일과 라벨만 folder 안에 저장"""
    image_list = os.listdir(IMAGE_PATH)

    for image in image_list:
        try:
            result = model.predict(IMAGE_PATH + image, save_txt=False)
            for r in result:
                r = r.to_json()
                if len(r) > 2:
                    model.predict(
                        IMAGE_PATH + image, save=True, save_txt=True, show_boxes=False
                    )
        except Exception as e:
            os.remove(IMAGE_PATH + image)
