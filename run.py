import base64
import sys

import cv2
import numpy as np
from vietocr.tool.config import Cfg

from cropper import Cropper
from detector import Detector
from reader import OCR
from app.utils import download_weights, Config, Item

if len(sys.argv) != 2:
	print("Usage: python run.py <filename>")
	sys.exit(1)

cfg = Config.load_config()

cropper = Cropper(config_path=download_weights(cfg['cropper']['cfg'], cache='config/yolov4_tiny.cfg'),
                  weight_path=download_weights(cfg['cropper']['weight'], cache='config/yolov4_tiny.weights'))

detector = Detector(config_path=download_weights(cfg['detector']['cfg'], cache='config/yolotinyv4_cccd.cfg'),
                    weight_path=download_weights(cfg['detector']['weight'], cache='config/yolotinyv4_cccd.weights'))

config = Cfg.load_config_from_name('vgg_transformer')
config['weights'] = cfg['reader']['weight']
config['cnn']['pretrained'] = False
config['device'] = 'cpu'
config['predictor']['beamsearch'] = False
reader = OCR(config)

filename = sys.argv[1]
file = open(filename, "rb")
img_object = bytes(file.read())
image = cv2.imdecode(np.fromstring(
            img_object, np.uint8), cv2.IMREAD_COLOR)

is_card, is_id_card, warped = cropper.process(image=image)
if is_card is False and is_id_card is None:
	print("Please choose your id card")
	exit()
if is_id_card is not None and warped is None:
	print("Please choose your id card")
	exit()

info_images = detector.process(warped)

info = dict()

for id in list(info_images.keys()):
	# 7 is id of portrait class
	if id == 7:
		continue
	label = detector.i2label_cc[id]
	if isinstance(info_images[id], np.ndarray):
		info[label] = reader.predict(info_images[id])
	elif isinstance(info_images[id], list):
		info[label] = []
		for i in range(len(info_images[id])):
			info[label].append(reader.predict(info_images[id][i]))

info['nationality'] = 'Việt Nam'
if 'sex' in info.keys():
	if 'Na' in info['sex']:
		info['sex'] = 'Nam'
	else:
		info['sex'] = 'Nữ'

print(info)
