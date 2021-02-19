# Video Clips Grabber
Python/OpenCV based Video Player with keyboard and mouse controls. 
Useful for Research purposes, when one wishes to monitor the video frame by frame.

Directory Structure:<br>

BallData<br>
|<br>
|___MatchName<br>
|&emsp;&emsp;    |<br>
|&emsp;&emsp;    |___Type(In Air)<br>
|&emsp;&emsp;         |&emsp;&emsp;  |<br>
|&emsp;&emsp;         |&emsp;&emsp;        |___InstanceNumber(1)<br>
|&emsp;&emsp;         |&emsp;&emsp;        |&emsp;&emsp;   |___1.mp4<br>
|&emsp;&emsp;         |&emsp;&emsp;        |___2<br>
|&emsp;&emsp;         |&emsp;&emsp;        |&emsp;&emsp;|___2.mp4<br>
|&emsp;&emsp;         |
|&emsp;&emsp;    |<br>
|&emsp;&emsp;    |___Type(In Air)<br>
|&emsp;&emsp;         |&emsp;&emsp;  |<br>
|&emsp;&emsp;         |&emsp;&emsp;        |___InstanceNumber(1)<br>
|&emsp;&emsp;         |&emsp;&emsp;        |&emsp;&emsp;   |___1.mp4<br>
|&emsp;&emsp;         |&emsp;&emsp;        |___2<br>
|&emsp;&emsp;         |&emsp;&emsp;        |&emsp;&emsp;|___2.mp4<br>
|&emsp;&emsp;         .&emsp;&emsp;        .&emsp;&emsp;        <br>
.&emsp;&emsp;         .&emsp;&emsp;        .<br><br><br><br>
Contributions are welcome!

To run the program: <br>

<code> $ python clips_grabber.py video_file.mp4 </code>
<br><br>
W/w: "Play" <br>
S/s: "Stay" (Pause) [I like keeping things rhyming!] <br>
D/d: "Next" (Next frame) <br>
A/a: "Prev" (Previous frame) <br>
F/f: "Fast" (Increase playing speed) <br>
Q/q: "Slow" (Decrease playing speed) <br>
C/c: "Snap" (Screenshot feature)<br>
J/j: "In Air" (label 1)<br>
K/k: "rolling" (label 2)<br>
T/t: "timestamp" (Get current timestamp)<br>
N/n: "Clear Timestamp" (Clear timestamp)<br>

[VideoPlayer designed by @maximus009](https://github.com/maximus009/VideoPlayer)
