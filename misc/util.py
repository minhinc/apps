import os,re,isodate
import requests
import datetime
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

class utilc:
 def __init__(self,**kwarg):
  self.jsoni=kwarg['jsoni']

 def tokenize(text: str) -> list[str]:
    """Lowercase and extract word tokens, ignoring punctuation."""
    return re.findall(r'\b[a-z0-9]+\b', text.lower())


 def match_percentage(source: str, target: str) -> tuple[float, str]:
    """
    Return (percentage, reason) for how well *source* matches *target*.

    Rules
    -----
    1. Full phrase found  → 100 %
    2. All source words found individually → 100 %  (handles reordered words)
    3. Some source words found → proportional %
    4. No words found → 0 %
    """
    print(f'>< match_percentage {source=} {target=}')
    src = source.strip().lower()
    tgt = target.lower()

    # ── Tier 1: exact phrase present ────────────────────────────────────────
    if src in tgt:
        return 100.0, "exact phrase match"

    # ── Tier 2 / 3: word-level overlap ──────────────────────────────────────
    src_words  = tokenize(src)
    tgt_tokens = set(tokenize(tgt))

    if not src_words:
        return 0.0, "empty source"

    matched   = [w for w in src_words if w in tgt_tokens]
    pct       = len(matched) / len(src_words) * 100

    if pct == 100.0:
        reason = "all words matched (phrase not contiguous)"
    elif pct == 0.0:
        reason = "no words matched"
    else:
        reason = f"words matched: {matched}"

    print(f'<=>percent_match {pct=} {reason=}')
    return round(pct, 1), reason


 def percentmatch(self, *, sourcel_, targets_):
  sourcel_ = [s.strip() for s in (sourcel_ if type(sourcel_)==list or type(sourcel_)==tuple else [sourcel_])]
  documents = sourcel_ + [targets_]
 
#  vectorizer = TfidfVectorizer()
  vectorizer = TfidfVectorizer(
    lowercase=True,
    token_pattern=r'(?u)[a-zA-Z0-9\+#]+'
  )
  tfidf = vectorizer.fit_transform(documents)
 
  target_vec = tfidf[-1]
  score=0
  for i, src in enumerate(sourcel_):
   score += cosine_similarity(tfidf[i], target_vec)[0][0] * 100
  return True if score/len(sourcel_) > 10 else False

 def match(self, sources1_, sources2_):
  return re.search("r'^"+sources1_+"$'", sources2_, flags=re.I)

 def gjf(self,list_,fields_, **kwarg_):#gjf->getjsonfield
  try:
   retval=list_[self.jsoni['index'].index(fields_)]
  except:
   return None
  return re.sub(r'^(?P<id>(static|render))\b',lambda m,kwarg_=kwarg_:eval(r'kwarg_["'+m.group('id')+'url'+r'"]'),retval) if type(retval)==str and ('staticurl' in kwarg_ or 'renderurl' in kwarg_) else retval

 def ym(self,reset=False,_cache={}):#youtube metadata
  def format_number(num):
      if num >= 1_000_000:
          val = num / 1_000_000
          suffix = 'M'
      elif num >= 1000:
          val = num / 1000
          suffix = 'K'
      else:
          return f"{num}"
   
      # Use :g to drop trailing zeros, then format to max 2 decimal places
      # We round first to adhere to the requested two-digit precision
      return f"{round(val, 2):g} {suffix}"
  if self.nextday() or not _cache:
   try:
    print(f'>< utilc.ym REFETCHING From YouTube')
    API_KEY = os.getenv("YOUTUBE_API_KEY")
    CHANNEL_HANDLE = "@minhinc"
    url = "https://www.googleapis.com/youtube/v3/channels"
    params = {
        "part": "snippet,statistics",
        "forHandle": CHANNEL_HANDLE,
        "key": API_KEY
    }
    response = requests.get(url, params=params)
    data = response.json()
    item = data["items"][0]
    channel_id = item["id"]
    _cache['subscriber_count'] = format_number(int(item["statistics"]["subscriberCount"]))
    
    search_url = "https://www.googleapis.com/youtube/v3/search"
    
    search_params = {
        "part": "snippet",
        "channelId": channel_id,
        "maxResults": 1,
        "order": "date",
        "type": "video",
        "key": API_KEY
    }
    
    search_response = requests.get(search_url, params=search_params)
    search_data = search_response.json()
    video = search_data["items"][0]
    _cache['video_id'] = video["id"]["videoId"]
    _cache['video_title'] = video["snippet"]["title"]

    _cache['thumbnail_url'] = video["snippet"]["thumbnails"]["high"]["url"]
    _cache['video_link'] = f"https://www.youtube.com/watch?v={_cache['video_id']}"
   except Exception as e:
    print(f'<=> utilc.ym Exception {e=}') 
    if not _cache:
     _cache['subscriber_count'] = '_'
     _cache['video_id'] = ''
     _cache['video_title'] = 'x'*100
     _cache['video_link']=''
   
  return _cache

 def nextday(self,_cache={}):
  hour=datetime.datetime.now().hour
  if not _cache or not _cache['today'] == (datetime.datetime.now().strftime("%Y%m%d") + str(hour % 6)):
   print(f'<=> nextday RECALCULATTING {datetime.datetime.now().strftime("%Y%m%d")+str(hour)=}')
   _cache['today']=datetime.datetime.now().strftime("%Y%m%d") + str(hour % 6)
   return True
  return False

 def downloadleft(self, **kwarg_):
  return f'''<div class='downloadleft'>
<ul class='tablist'>
<a href='{kwarg_['staticurl']}/{kwarg_['topic']}/'><li class='header'><p>{kwarg_['topic']}</p></li></a>
{chr(10).join(["<li class='current'><p class='padtop'>"+self.gjf(self.jsoni[kwarg_['topic']]['data'][ii],'title')+"</p></li>" if self.gjf(self.jsoni[kwarg_['topic']]['data'][ii],'abbreviation')==kwarg_['subtopic'] else "<a href='"+kwarg_['staticurl']+"/"+kwarg_['topic']+"/"+self.gjf(self.jsoni[kwarg_['topic']]['data'][ii],'abbreviation')+"'><li class='"+['light','dark'][ii%2]+"'><p>"+self.gjf(self.jsoni[kwarg_['topic']]['data'][ii],'title')+"</p></li></a>" for ii in range(len(self.jsoni[kwarg_['topic']]['data']))])}
 </ul>
</div>'''

 def maxhourlinkyoutube(self, **kwarg_):
  if not hasattr(utilc.maxhourlinkyoutube,'videos'):
   utilc.maxhourlinkyoutube.videos=[]
  if not utilc.maxhourlinkyoutube.videos:
   API_KEY = os.getenv("YOUTUBE_API_KEY")
   CHANNEL_HANDLE = "@minhinc"
   if not API_KEY:
       raise RuntimeError("YOUTUBE_API_KEY environment variable not found")
   # ============================================================
   # 1. Get Channel ID and Uploads Playlist ID
   # ============================================================
   url = "https://www.googleapis.com/youtube/v3/channels"
   params = {
       "part": "snippet,contentDetails,statistics",
       "forHandle": CHANNEL_HANDLE,
       "key": API_KEY
   }
   response = requests.get(url, params=params)
   response.raise_for_status()
   data = response.json()
   if not data.get("items"):
    raise RuntimeError("YouTube channel not found")
   channel = data["items"][0]
   channel_id = channel["id"]
   channel_title = channel["snippet"]["title"]
   subscriber_count = channel["statistics"].get(
       "subscriberCount", "0"
   )
   uploads_playlist_id = (
       channel["contentDetails"]
       ["relatedPlaylists"]
       ["uploads"]
   )
   print("Channel       :", channel_title)
   print("Channel ID    :", channel_id)
   print("Subscribers   :", subscriber_count)
   print("Uploads ID    :", uploads_playlist_id)
   # ============================================================
   # 2. Get ALL video IDs from Uploads Playlist
   # ============================================================
   video_ids = []
   next_page_token = None
   while True:
    url = "https://www.googleapis.com/youtube/v3/playlistItems"
    params = {
        "part": "contentDetails",
        "playlistId": uploads_playlist_id,
        "maxResults": 50,
        "key": API_KEY
    }
    if next_page_token:
     params["pageToken"] = next_page_token
    response = requests.get(url, params=params)
    response.raise_for_status()
    data = response.json()
    for item in data.get("items", []):
     video_id = item["contentDetails"]["videoId"]
     video_ids.append(video_id)
    next_page_token = data.get("nextPageToken")
    if not next_page_token:
     break
   
   print()
   print("Total videos found:", len(video_ids))
   # ============================================================
   # 3. Get detailed information for videos
   #
   # YouTube accepts up to 50 video IDs in one videos.list call.
   # ============================================================
   #utilc.maxhourlinkyoutube.videos = []
   for start in range(0, len(video_ids), 50):
    batch = video_ids[start:start + 50]
    url = "https://www.googleapis.com/youtube/v3/videos"
    params = {
           "part": "snippet,contentDetails,statistics",
           "id": ",".join(batch),
           "key": API_KEY
       }
    response = requests.get(url, params=params)
    response.raise_for_status()
    data = response.json()
    for item in data.get("items", []):
     duration_text = item["contentDetails"].get( "duration", "PT0S")
     duration = isodate.parse_duration(duration_text)
     duration_seconds = int( duration.total_seconds())
     utilc.maxhourlinkyoutube.videos.append({
               #"id": item["id"],
               "title": item["snippet"]["title"],
               "duration_seconds": duration_seconds,
               #"duration_iso": duration_text,
               #"thumbnail": item["snippet"]["thumbnails"]["high"]["url"],
               "link": f"https://www.youtube.com/watch?v={item['id']}",
               "views": item.get("statistics", {}).get("viewCount", "0")
           })
   # ============================================================
   # 4. Sort ALL videos by duration
   # ============================================================
   utilc.maxhourlinkyoutube.videos.sort(
       key=lambda video: video["duration_seconds"],
       reverse=True
   )
   utilc.maxhourlinkyoutube.videos[50:]=[]
  html=''
  for number, video in enumerate(utilc.maxhourlinkyoutube.videos,start=1):
   html+=f'<span style="font-size:7pt;font-weight:bold;">{number}.</span> <a href="{video["link"]}">{video["title"]}</a> {video["duration_seconds"]//3600:02d}:{(video["duration_seconds"]%3600)//60:02d}:{video["duration_seconds"]%60:02d} {video["views"]}</br>'
  return html
