import os,re
import requests
import datetime

import asyncio
import aiohttp
import isodate
import time

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

 async def maxhourlinkyoutube(self, **kwarg_):

  async def get_uploads_playlist_id(session):
   """Step 1: Get the hidden 'uploads' playlist ID for the channel."""
   url = f"https://www.googleapis.com/youtube/v3/channels?part=contentDetails&id={CHANNEL_ID}&key={API_KEY}"
   async with session.get(url) as response:
    data = await response.json()
    return data['items'][0]['contentDetails']['relatedPlaylists']['uploads']

  async def fetch_video_ids(session, playlist_id):
   """Step 2: Fetch all video IDs sequentially using nextPageToken (The Bottleneck)."""
   video_ids = []
   page_token = ""
    
   while True:
    url = f"https://www.googleapis.com/youtube/v3/playlistItems?part=contentDetails&playlistId={playlist_id}&maxResults=50&key={API_KEY}"
    if page_token:
     url += f"&pageToken={page_token}"
            
    async with session.get(url) as response:
     data = await response.json()
     for item in data.get('items', []):
      video_ids.append(item['contentDetails']['videoId'])
                
     page_token = data.get('nextPageToken')
     if not page_token:
      break
                
   return video_ids

  async def fetch_video_details_chunk(session, chunk):
   """Worker function to fetch both title AND duration for 50 IDs at once."""
   ids_string = ",".join(chunk)
   # Requesting both snippet (title) and contentDetails (duration)
   url = f"https://www.googleapis.com/youtube/v3/videos?part=snippet,contentDetails&id={ids_string}&key={API_KEY}"
    
   async with session.get(url) as response:
    data = await response.json()
    results = {}
    for item in data.get('items', []):
     results[item['id']] = {
      'title': item['snippet']['title'],
      'duration': item['contentDetails']['duration']
     }
    return results


  start_time=time.time()
  if not hasattr(utilc.maxhourlinkyoutube,'videos'):
   utilc.maxhourlinkyoutube.final_video_data={}
  if not utilc.maxhourlinkyoutube.final_video_data:
   API_KEY = os.getenv("YOUTUBE_API_KEY")
   CHANNEL_ID = 'UChmiKM2jr7e9iUOrVPKRTXQ' # e.g., UC_x5XG1OV2P6uZZ5FSM9Ttw
   if not API_KEY:
       raise RuntimeError("YOUTUBE_API_KEY environment variable not found")
    
   async with aiohttp.ClientSession() as session:
    print("1. Fetching Playlist ID...")
    playlist_id = await get_uploads_playlist_id(session)
         
    print("2. Fetching all Video IDs (Sequential - please wait)...")
    video_ids = await fetch_video_ids(session, playlist_id)
    print(f"   Found {len(video_ids)} videos.")
         
    print("3. Fetching Durations (Fully Asynchronous)...")
    # Split the 3000 IDs into chunks of 50
    chunks = [video_ids[i:i + 50] for i in range(0, len(video_ids), 50)]
         
    # Create asynchronous tasks to run them all at exactly the same time
    #tasks = [fetch_durations_chunk(session, chunk) for chunk in chunks]
    tasks = [fetch_video_details_chunk(session, chunk) for chunk in chunks]
         
    # Gather all results simultaneously 
    results_list = await asyncio.gather(*tasks)
         
    # Combine the list of dictionaries into one dictionary
    #final_video_data = {}
    for res in results_list:
     utilc.maxhourlinkyoutube.final_video_data.update(res)
             

  html=f'<pre><b>Finished! Total time: {time.time() - start_time:.2f} seconds</b><br>'
  for number, (vid, duration) in enumerate(sorted(utilc.maxhourlinkyoutube.final_video_data.items(),key=lambda item: int(isodate.parse_duration(item[1]['duration']).total_seconds()),reverse=True)[:int(kwarg_['request'].args['cmd']) if 'cmd' in kwarg_['request'].args else 50],start=1):
   second=int(isodate.parse_duration(duration['duration']).total_seconds())
   html+=f'<span style="font-size:7pt;font-weight:bold;">{number}.</span> <a href="https://www.youtube.com/watch?v={vid}">{duration['title']}</a> {second//3600:02d}:{(second%3600)//60:02d}:{second%60:02d}</br>'
  return html
