# Common Utils

Some simple tools that I end up using repeatedly. Will add more utils eventually. 

## Simple hacky tool for writing HTML files using Python
Beware, here there be bugs and experiments. 

Bare bones syntax:

```
web = html.HTMLPage(filename="vis.html", title="vis") # starts the html file

# let's make a table
web.startTable()

web.startRow()
web.startCol(header=True)
web.writeText("some header")
web.endCol()
web.startCol(header=True)
web.writeText("Another header")
web.endCol() 
web.startCol(header=True)
web.writeText("yet another header")
web.endCol() # these endCol and endRow's are optional, but safer to include them. 
web.endRow() # these endCol and endRow's are optional, but safer to include them.

web.startRow()
web.startCol()
web.writeText("<b> some text </b>") # can include any html tags in the writeText()
web.endCol()
web.startCol()
web.writeImage("/path/to/image/file.png", width=290, height=290)
web.endCol()
web.startCol()
web.embed_audio("/path/to/audio/file.mp3")
web.endCol()
web.endRow()

web.endTable()
```

## Simple video manipulation tools

### How to clip videos and extract audio
To extract a subclip of a video, install moviepy by doing `pip install moviepy`

```
from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip
ffmpeg_extract_subclip(video_file, start_time, end_time, targetname="/path/to/output_clipped_video.mp4")
```

The `start_time` and `end_time` are in seconds. 

To extract audio for this video clip, I use `ffmpeg`. In python, you can do:

`os.system("ffmpeg -i video_file_path.mp4 audio_file_path.mp3")` 

### How to extract frames from video
In the `video_utils.py` file, the `get_video_frames()` function can be used to extract frames of a video for a certain interval at a certain fps. 

```
import cv2
vidcap = cv2.VideoCapture(video_file_path)
frames = get_video_frames(vidcap, fps=0.2, interval=(start_time_in_ms, end_time_in_ms))
```

Note that the start and end times here are speicifed in milliseconds. Both the fps and interval arguments are optional. If FPS is not specified, it uses the default max fps for the video file. If duration is not speciifed, it extracts frames for the entire video. 







