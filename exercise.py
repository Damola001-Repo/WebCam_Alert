# from turtledemo.penrose import start

import streamlit as st
import cv2
import numpy as np
import time

st.title("Motion Detection")
start = st.button('Start Camera')


if start:
    streamlit_image = st.image([])
    camera = cv2.VideoCapture(1)

    while True:
        check, frame = camera.read()
        frame = cv2.cvtColor(np.flip(frame, 1), cv2.COLOR_BGR2RGB)

        cv2.putText(frame, text=time.strftime("%A"), org=(50, 50), fontFace=cv2.FONT_HERSHEY_PLAIN,
                    fontScale=2, color=(255, 255, 255), thickness=2, lineType=cv2.LINE_AA)
        cv2.putText(frame, text=time.strftime("%H:%M:%S"), org=(50, 120), fontFace=cv2.FONT_HERSHEY_PLAIN,
                    fontScale=2, color=(20, 100, 20), thickness=2, lineType=cv2.LINE_AA)

        streamlit_image.image(frame)

        if not start:
            break

    camera.release()