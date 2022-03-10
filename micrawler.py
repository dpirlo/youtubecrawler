from youtubecrawler.crawl import crawl
import sys

id =str(sys.argv[1])
#print (id)

yt=crawl(video_link="https://www.youtube.com/watch?v="+ id)

views= yt.veiws()
print(views)
videoname= yt.VidTitle()
print(videoname)

