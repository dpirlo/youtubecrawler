#from youtubecrawler.crawl import crawl
import sys
import json

sys.path.append(".")
from  crawl import crawl

from channel import channel

id =str(sys.argv[1])

# yt=crawl(video_link="https://www.youtube.com/watch?v="+ id)
# views= yt.veiws()
# print(views)
# videoname= yt.VidTitle()
# print(videoname)
# channel_= yt.channel()
# print(channel_)
# json.dumps(channel_)

chan= channel(channelname=id)


about = chan.latest_video()
print(about)
