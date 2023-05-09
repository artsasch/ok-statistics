import requests
import json
from datetime import datetime
from utils.utils import *


# method = "url.getInfo"
# url = "https://ok.ru/ostrov.chistoty"
# sig = md5(method, url)
# 
# params = {
#     "application_key": application_key,
#     "format": request_format,
#     "method": method,
#     "url": url,
#     "sig": sig,
#     "access_token": access_token,
# }


fields = "comments, \
          complaints, \
          content_opens, \
          engagement, \
          feedback, \
          hides_from_feed, \
          left_members, \
          likes, \
          link_clicks, \
          members_count, \
          members_diff, \
          music_plays, \
          negatives, \
          new_members, \
          new_members_target, \
          page_visits, \
          photo_opens, \
          reach, \
          reach_earned, \
          reach_mob, \
          reach_mobweb, \
          reach_own, \
          reach_web, \
          renderings, \
          reshares, \
          topic_opens, \
          video_plays, votes"

method = "group.getStatTrends"
sig = "9baf058da1814d299ca4622f332f05c2"
gid = 52927256723523

params = {
    "application_key": application_key,
    "format": request_format,
    "method": method,
    "gid": gid,
    "sig": sig,
    "access_token": access_token,
    "fields": fields,
    "start_time": 1672806400000,
    "end_time": 1672972800000
}


response = requests.get(api_url, params=params)
data = json.loads(response.text)

for metric, values in data.items():
    for value in values:
        value["time"] = datetime.fromtimestamp(value["time"] / 1000.0).strftime("%Y-%m-%d")

with open('.json/response.json', 'w') as f:
    json.dump(data, f, indent=3)
