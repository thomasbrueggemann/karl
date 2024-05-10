
import face_recognition
import cv2
import numpy as np

class Eyes:
	def __init__(self):
		self.cam = cv2.VideoCapture(0) # 0 = default cam