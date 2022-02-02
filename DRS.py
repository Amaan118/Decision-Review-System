import tkinter
from tkinter.constants import ANCHOR
import cv2
import PIL.Image
import PIL.ImageTk
from functools import partial
import time
import imutils
import threading

SET_HEIGHT = 368
SET_WIDTH = 650

stream = cv2.VideoCapture("clip.mp4")


def replay(speed):
    frame1 = stream.get(cv2.CAP_PROP_POS_FRAMES)
    stream.set(cv2.CAP_PROP_POS_FRAMES, frame1 + speed)

    grabbed, frame = stream.read()
    frame = imutils.resize(frame, width=SET_WIDTH, height=SET_HEIGHT)
    frame = PIL.ImageTk.PhotoImage(
        image=PIL.Image.fromarray(frame))
    canvas.image = frame
    canvas.create_image(0, 0, image=frame, anchor=tkinter.NW)


def decision(dec):
    frame = cv2.cvtColor(cv2.imread("Decision.png"), cv2.COLOR_BGR2RGB)
    frame = imutils.resize(frame, width=SET_WIDTH, height=SET_HEIGHT)
    frame = PIL.ImageTk.PhotoImage(
        image=PIL.Image.fromarray(frame))
    canvas.image = frame
    canvas.create_image(0, 0, image=frame, anchor=tkinter.NW)

    time.sleep(1)

    frame = cv2.cvtColor(cv2.imread("Sponsor.png"), cv2.COLOR_BGR2RGB)
    frame = imutils.resize(frame, width=SET_WIDTH, height=SET_HEIGHT)
    frame = PIL.ImageTk.PhotoImage(
        image=PIL.Image.fromarray(frame))
    canvas.image = frame
    canvas.create_image(0, 0, image=frame, anchor=tkinter.NW)

    time.sleep(3)

    if dec == 'ot':
        img = "Out.png"
    elif dec == 'no':
        img = "Not_out.png"

    frame = cv2.cvtColor(cv2.imread(img), cv2.COLOR_BGR2RGB)
    frame = imutils.resize(frame, width=SET_WIDTH, height=SET_HEIGHT)
    frame = PIL.ImageTk.PhotoImage(
        image=PIL.Image.fromarray(frame))
    canvas.image = frame
    canvas.create_image(0, 0, image=frame, anchor=tkinter.NW)


def not_out():
    thread = threading.Thread(target=decision, args=("no", ))
    thread.daemon = 1
    thread.start()


def out():
    thread = threading.Thread(target=decision, args=("ot", ))
    thread.daemon = 1
    thread.start()


window = tkinter.Tk()
window.title("Decision Review System - Amaan Khan")

cv_img = cv2.cvtColor(cv2.imread("Start.png"), cv2.COLOR_BGR2RGB)
canvas = tkinter.Canvas(window, width=SET_WIDTH, height=SET_HEIGHT)
photo = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(cv_img))
image_on_canvas = canvas.create_image(0, 0, anchor=tkinter.NW, image=photo)
canvas.pack()

btn = tkinter.Button(window, text="<< Back ",
                     width=25, command=partial(replay, -25))
btn.pack()

btn = tkinter.Button(window, text="<< Back Slow ",
                     width=25, command=partial(replay, -15))
btn.pack()

btn = tkinter.Button(window, text="<< Back Vey Slow ",
                     width=25, command=partial(replay, -5))
btn.pack()

btn = tkinter.Button(window, text="Next >>",
                     width=25, command=partial(replay, 5))
btn.pack()

btn = tkinter.Button(window, text="Next Fast >>",
                     width=25, command=partial(replay, 15))
btn.pack()

btn = tkinter.Button(window, text="Next Very Fast >>",
                     width=25, command=partial(replay, 25))
btn.pack()

btn = tkinter.Button(window, text="Decision : OUT",
                     width=25, command=out)
btn.pack()

btn = tkinter.Button(window, text="Decision : NOT OUT",
                     width=25, command=not_out)
btn.pack()

window.mainloop()
