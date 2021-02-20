'''
How to use:
Syntax:
$ python <python_file>.py <video name.mp4>
Example:
$ python videoplayer.py "Arsenal vs WestHam 2-1.mp4"


Annotator for 3D ball trajectory estimation project
Video clips and frame grabber
'''

import cv2, numpy as np
import os
import glob
import shutil
import sys
from time import sleep
from pathlib import Path


def time_converter(milliseconds):
    '''
    Method to convert cv2 timestamp input into 
    useable for ffmpeg
    input
    cv2     :   0000000.00 miliSec
    return
    ffmpeg  :   HH:MM:SS.mSec
    '''
    seconds = milliseconds//1000
    milliseconds = milliseconds%1000
    minutes = 0
    hours = 0
    if seconds >= 60:
        minutes = seconds//60
        seconds = seconds % 60

    if minutes >= 60:
        hours = minutes//60
        minutes = minutes % 60
    
    return str(f"{int(hours)}:{int(minutes)}:{int(seconds)}.{int(milliseconds)}")


def place_clip(type, start, end, match_name):
    '''
    Ojectives:
    1) Create directories
    2) Trim clips

    Arguments:
    type        :   "In Air", "rolling"
    start       :   trim start time
    end         :   trim end time
    match_name  :   match name to create directory
    '''
    # Create the folders
    #BASE_PATH = "../../BallData"                       # For linux
    BASE_PATH = "C:/Users/A/Music/omno.ai/BallData"     # For Windows
    match_name = "Arsenal vs WestHam 2-1"
    x = ""
    instance = 0
    clip_path = ""
    if not os.path.exists(os.path.join(BASE_PATH, match_name, type)):
        os.makedirs(os.path.join(BASE_PATH, match_name, type))
    instance = str((len(next(os.walk(os.path.join(BASE_PATH, match_name, type)))[1]) + 1))
    x = os.path.join(BASE_PATH, match_name, type)
    if not os.path.exists(os.path.join(x, instance)):
        try:  
            os.mkdir(os.path.join(x, instance))
            clip_path = os.path.join(x, instance)  
        except OSError as error:  
            print(error)  
        print("clip_path")
        print(clip_path)
        os.system(f"ffmpeg -ss {start} -i \"{match_name}.mp4\" -to {end} -c copy \"{clip_path}/{instance}.mp4\"")
        return
    else:
        print("else part")
        clip_path = os.path.exists(os.path.join(x, instance))
        os.system(f"ffmpeg -ss {start} -i \"{match_name}.mp4\" -to {end} -c copy \"{clip_path}/{instance}.mp4\"")
    

def flick(x):
    pass

video = sys.argv[1]
match_name = video[:-4]
print(match_name)


cv2.namedWindow('image')
cv2.moveWindow('image',250,150)
cv2.namedWindow('controls')
cv2.moveWindow('controls',250,50)

controls = np.zeros((50,1150),np.uint8)
cv2.putText(controls, "W/w: Play, S/s: Stay/Pause, A/a: Prev, D/d: Next, F/f: Fast, Q/q: Slow, T/t: Time, N/n: Clear Time, J/j: In Air, k/K: rolling, Esc: Exit", (40,20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, 255)

'''
video = sys.argv[1]
match_name = video[:-4]
print(match_name)
'''
cap = cv2.VideoCapture(video)

tots = cap.get(cv2.CAP_PROP_FRAME_COUNT)
i = 0
cv2.createTrackbar('S','image', 0,int(tots)-1, flick)
cv2.setTrackbarPos('S','image',0)

cv2.createTrackbar('F','image', 1, 100, flick)
frame_rate = 30
cv2.setTrackbarPos('F','image',frame_rate)

def process(im):
    return cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)

# Get current timestamp
def current_time(cap):
    '''
    Function:
    get current timestamp
    '''
    return cap.get(cv2.CAP_PROP_POS_MSEC)

status = 'stay'
start  = None
end    = None

while True:
  cv2.imshow("controls",controls)
  try:
    if i==tots-1:
      i=0
    cap.set(cv2.CAP_PROP_POS_FRAMES, i)
    ret, im = cap.read()
    r = 750.0 / im.shape[1]
    dim = (750, int(im.shape[0] * r))
    im = cv2.resize(im, dim, interpolation = cv2.INTER_AREA)
    if im.shape[0]>600:
        im = cv2.resize(im, (500,500))
        controls = cv2.resize(controls, (im.shape[1],25))
    #cv2.putText(im, status, )
    cv2.imshow('image', im)
    status = { ord('s'):'stay', ord('S'):'stay',
                ord('w'):'play', ord('W'):'play',
                ord('a'):'prev_frame', ord('A'):'prev_frame',
                ord('d'):'next_frame', ord('D'):'next_frame',
                ord('q'):'slow', ord('Q'):'slow',
                ord('f'):'fast', ord('F'):'fast',
                ord('c'):'snap', ord('C'):'snap',
                ord('j'):'in Air', ord('J'):'in Air',
                ord('k'):'rolling', ord('K'):'rolling',
                ord('t'):'timestamp', ord('T'):'timestamp',
                ord('n'):'clear_time', ord('N'):'clear_time',
                -1: status, 
                27: 'exit'}[cv2.waitKey(10)]

    # key
    if status == 'play':
      frame_rate = cv2.getTrackbarPos('F','image')
      sleep((0.1-frame_rate/1000.0)**21021)
      i+=1
      cv2.setTrackbarPos('S','image',i)
      continue
    if status == 'stay':
      i = cv2.getTrackbarPos('S','image')
    if status == 'exit':
        break
    if status=='prev_frame':
        i-=1
        cv2.setTrackbarPos('S','image',i)
        status='stay'
    if status=='next_frame':
        i+=1
        cv2.setTrackbarPos('S','image',i)
        status='stay'
    if status=='slow':
        frame_rate = max(frame_rate - 5, 0)
        cv2.setTrackbarPos('F', 'image', frame_rate)
        status='play'
    if status=='fast':
        frame_rate = min(100,frame_rate+5)
        cv2.setTrackbarPos('F', 'image', frame_rate)
        status='play'
    if status=='snap':
        cv2.imwrite("./"+"Snap_"+str(i)+".jpg",im)
        print("Snap of Frame",i,"Taken!")
        status='stay'
    if status=='timestamp':
        if start is None:
            start = time_converter(current_time(cap))
            print(f"Time extracted: {start}")
        else:
            end = time_converter(current_time(cap))
            print(f"Time extracted: {end}")
        status='stay'
    if status=='in Air':
        if start is None or end is None:
            print("Please select start and end time")
        else:
            place_clip(status, start, end, match_name)
            start, end = None, None
            print("In Air Clip extracted")
        status='stay'
    if status=='rolling':
        if start is None or end is None:
            print("Please select start and end time")
        else:
            place_clip(status, start, end, match_name)
            start, end = None, None
            print("Rolling Clip extracted")
        status='stay'
    if status=='clear_time':
        start = None
        end = None
        print("Time is cleared")
        status='stay'

  except KeyError:
      print("Invalid Key was pressed")
cv2.destroyWindow('image')
