import re,datetime
def main(self,**kwarg_):
 print(f'>< main {kwarg_}')
 return (f'''<div class='leftpan'>''' if not kwarg_['mobile'] else '')+f'''
 <div class='container'>
    <a href='{self.utili.ym()['video_link']}'><img class='thumbnail' src='{"https://i.ytimg.com/vi/"+self.utili.ym()['video_id']+"/maxresdefault.jpg" if self.utili.ym()['video_id'] else kwarg_['imageurl']+'/image/main_front.png'}'></img></a>
    <img class='youtube-logo' src='https://upload.wikimedia.org/wikipedia/commons/b/b8/YouTube_Logo_2017.svg'></img>
    <div class='subscribers'> {self.utili.ym()['subscriber_count']+' Subscribers'}</div>
    <p class='title'>{self.utili.ym()['video_title']}</p>
    <pre class='toptitle'>Watch Technology at YouTube</pre>
</div>'''+(f'''
 <div class='research'>
  <ul class='research'>
   <a href='{kwarg_['staticurl']}/research/'><li class='header'><p>Research</p></li></a>
   {chr(10).join(["<a href='"+self.utili.gjf(self.jsoni['research']['data'][ii],'url',**kwarg_)+"'><li class='"+['light','dark'][ii%2]+"'><p class='t'>"+self.utili.gjf(self.jsoni['research']['data'][ii],'title')+"</p><p class='b'>"+self.utili.gjf(self.jsoni['research']['data'][ii],'publisher')+","+datetime.datetime.fromisoformat(self.utili.gjf(self.jsoni['research']['data'][ii],'date')).strftime('%Y %B')[:8]+"</p><img src='"+kwarg_['imageurl']+"/image/"+self.utili.gjf(self.jsoni['research']['data'][ii],'abbreviation')+".png'/></li></a>" for ii in range(len(self.jsoni['research']['data']))])}
  </ul>
 </div>
 <div class='product'>
  <ul class='research'>
   <a href='{kwarg_['staticurl']}/product/'><li class='header'><p>Product</p></li></a>
   {chr(10).join(["<a href='"+self.utili.gjf(self.jsoni['product']['data'][ii],'url',**kwarg_)+"'><li class='"+['light','dark'][ii%2]+"'><p class='t'>"+self.utili.gjf(self.jsoni['product']['data'][ii],'title')+"</p><p class='bp'>"+datetime.datetime.fromisoformat(self.utili.gjf(self.jsoni['research']['data'][ii],'date')).strftime('%Y %B')[:8]+"</p><img src='"+kwarg_['imageurl']+"/image/"+self.utili.gjf(self.jsoni['product']['data'][ii],'abbreviation')+".png'/></li></a>" for ii in range(len(self.jsoni['product']['data']))])}
  </ul>
 </div>
</div>
<div class='rightpan'>
 <ul class='events'>
  <li class='header'><p>Upcoming Events</p></li>
   {chr(10).join(["<a href='"+self.utili.gjf(self.jsoni['training']['data'][ii],'url',**kwarg_)+"'><li class='"+['light','dark'][ii%2]+"'><p class='t'>"+self.utili.gjf(self.jsoni['training']['data'][ii],'title')+" Training </p><p class='b'>"+(datetime.datetime.now()+datetime.timedelta(days=(0 if datetime.datetime.now().day<=15 else 15))).strftime("%B")+" "+str(datetime.datetime.now().year)+"</p></li></a>" for ii in range(len(self.jsoni['training']['data'])) if re.search('(machine|artificial|python)',self.jsoni['training']['data'][ii][0],flags=re.I)])}
 </ul>
 <ul class='next'>
  <a href='{kwarg_['staticurl']}/training/'><li class='header'><p>Training</p></li></a>
   {chr(10).join(["<li class='"+['light','dark'][ii%2]+"'><a class='ls' href='"+self.utili.gjf(self.jsoni['training']['data'][ii],'url',**kwarg_)+"'>Slides</a><a href='"+self.utili.gjf(self.jsoni['training']['data'][ii],'url',**kwarg_)+"'><img class='l' src='"+kwarg_['imageurl']+'/image/'+self.utili.gjf(self.jsoni['training']['data'][ii],'abbreviation')+".png'/></a>"+("</li" if ii == (len(self.jsoni['training']['data'])-1) else "") if not ii%2 else "<a class='rs' href='"+self.utili.gjf(self.jsoni['training']['data'][ii],'url',**kwarg_)+"'>Slides</a><a href='"+self.utili.gjf(self.jsoni['training']['data'][ii],'url',**kwarg_)+"'><img class='r' src='"+kwarg_['imageurl']+"/image/"+self.utili.gjf(self.jsoni['training']['data'][ii],'abbreviation')+".png'/></a></li>" for ii in range(len(self.jsoni['training']['data']))])}
 </ul>
</div>
''' if not kwarg_['mobile'] else f'''
 <div class='one'> <ul class='events'>
  <li class="header"><p>Upcoming Events</p></li>
   {chr(10).join(["<a href='"+self.utili.gjf(self.jsoni['training']['data'][ii],'url',**kwarg_)+"'><li class='"+['light','dark'][ii%2]+"'><p class='t'>"+self.utili.gjf(self.jsoni['training']['data'][ii],'title').title()+" Training </p><p class='b'>"+(datetime.datetime.now()+datetime.timedelta(days=(0 if datetime.datetime.now().day<=15 else 15))).strftime("%B")+" "+str(datetime.datetime.now().year)+"</p></li></a>" for ii in range(len(self.jsoni['training']['data'])) if re.search('(machine|artificial|python)',self.jsoni['training']['data'][ii][0],flags=re.I)])} </ul>
 </div>

{chr(10).join(["<div class='one'><a href='"+kwarg_['staticurl']+"/"+ii+"'><pre class='title'>"+ii.title()+"</pre></a><pre class='subtitle'>"+self.jsoni[ii]['description']+"</pre></div>"+chr(10)+"  <ul class='one'>" + chr(10).join(["  <li class='"+['light','dark'][jj%2]+"' style='clear:both;'><a href='"+self.utili.gjf(self.jsoni[ii]['data'][jj],'url',**kwarg_)+"'><img src='"+kwarg_['imageurl']+"/image/"+self.utili.gjf(self.jsoni[ii]['data'][jj],'abbreviation')+".png'/><pre>"+self.utili.gjf(self.jsoni[ii]['data'][jj],'title').title()+"</pre></a></li>" for jj in range(len(self.jsoni[ii]['data']))])+ chr(10)+" </ul>"+chr(10)+"  <div style='clear:both'>"+chr(10)+" </div>" for ii in self.jsoni if ii in ['research','product','training']])}
''') +f''' <script>
const MIN_PX = 6;
const MAX_PX = 96;

function fitParagraph(p) {{
  const parent = p.parentElement;
  const maxWidth = parent.clientWidth * 0.9;

  // Binary search for largest font-size that fits
  let lo = MIN_PX, hi = MAX_PX, best = MIN_PX;

  while (lo <= hi) {{
    const mid = (lo + hi) / 2;
    p.style.fontSize = mid + 'px';

    if (p.scrollWidth <= maxWidth) {{
      best = mid;
      lo = mid + 0.5;
    }} else {{
      hi = mid - 0.5;
    }}
  }}

  p.style.fontSize = best + 'px';
}}

// Collect all <p> elements inside .container divs
const paragraphs = document.querySelectorAll('.container p');

// Initial fit
paragraphs.forEach(fitParagraph);

// Re-fit whenever the div is resized (handles mobile rotation,
// window resize, and the drag-to-resize handle on desktop)
const ro = new ResizeObserver(() => {{
  paragraphs.forEach(fitParagraph);
}});

document.querySelectorAll('.container').forEach(container => ro.observe(container));
</script>
'''
