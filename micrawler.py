#from youtubecrawler.crawl import crawl
import sys

sys.path.append(".")
from crawl import crawl

id =str(sys.argv[1])

yt=crawl(video_link="https://www.youtube.com/watch?v="+ id)

views= yt.veiws()
print(views)


videoname= yt.VidTitle()
print(videoname)

channel= yt.channel()
print(channel)



def iterator():
    videorefprev=""
    while True:
        videoref= yt.videoRef()
        #print(videoref)
        while videoref == videorefprev: 
                videoref = yt.videoRef()
        yt=crawl(video_link="https://www.youtube.com/watch?v="+ videoref)
        views= yt.veiws()
        print(views)
        videoname= yt.VidTitle()
        print(videoname)
        videorefprev=videoref
