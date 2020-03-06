# kivy_multiple_video
Use of Kivy 'Video'-Widget to call multiple Videos

This is my basic template for a kiosk terminal to choose between different videos. Parts are taken from "videoplayer.py"
from kivy examples. Tested with:

Windows 10
Python 3.7
Kivy 1.11.1
Gstreamer 0.2.0

for stable operation more than 10 hours. Should also work with "ffpyplayer".

Remarks:
1. Never set Video.source to '' which results in error on closing the application when no video is running.
