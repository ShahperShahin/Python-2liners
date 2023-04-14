#firt you need to install a package of python
#run this in your terminal -> pip install pytube  

from pytube import YouTube
link = "<enter the link you want to download>"
yt = YouTube(link)
ys = yt.streams.get_highest_resolution()
ys.download()
