import datetime
import re

def research(self,**kwarg_):
 print(f'>< research {kwarg_=}')
 if not re.search(r'/',kwarg_['path']):
  return (f'''<ul class='common'>
 <li class='header'><p>{kwarg_['path'].upper()}</p></li>
 <li class="main"><img src='{kwarg_['imageurl']}/image/{kwarg_['path']}.png'/><div><p class='b'>{self.jsoni[kwarg_['path']]['subtitle']}</p><p class="n">{self.jsoni[kwarg_['path']]['description']}</p></div></li>
{chr(10).join(["<li class='entry'><a href='"+self.utili.gjf(self.jsoni[kwarg_['path']]['data'][ii],'url',**kwarg_)+"'><div class='dl'><img src='"+kwarg_['imageurl']+"/image/"+self.utili.gjf(self.jsoni[kwarg_['path']]['data'][ii],'abbreviation')+".png'><div><p class='b'>"+self.utili.gjf(self.jsoni[kwarg_['path']]['data'][ii],'title')+"</p><p>"+self.utili.gjf(self.jsoni[kwarg_['path']]['data'][ii],'description')+"</p><a class='space'></a><p class='space'>"+self.utili.gjf(self.jsoni[kwarg_['path']]['data'][ii],'date')+"</p></div></div></a>"+("</li>" if ii == (len(self.jsoni[kwarg_['path']]['data'])-1) else "") if not ii%2 else "<a href='"+self.utili.gjf(self.jsoni[kwarg_['path']]['data'][ii],'url',**kwarg_)+"'><div class='dr'><img src='"+kwarg_['imageurl']+"/image/"+self.utili.gjf(self.jsoni[kwarg_['path']]['data'][ii],'abbreviation')+".png'><div><p class='b'>"+self.utili.gjf(self.jsoni[kwarg_['path']]['data'][ii],'title')+"</p><p>"+self.utili.gjf(self.jsoni[kwarg_['path']]['data'][ii],'description')+"</p><a class='space'></a><p class='space'>"+self.utili.gjf(self.jsoni[kwarg_['path']]['data'][ii],'date')+"</p></div></div></a></li>" for ii in range(len(self.jsoni[kwarg_['path']]['data']))])}
  </ul>
''' if not kwarg_['mobile'] else f''' <ul class='two'>
<li class='header'><pre class='header'>{kwarg_['path'].upper()}</pre></li>
<li><div class='l'><img src='{kwarg_['imageurl']}/image/{kwarg_['path']}.png'/></div><div class='right'><pre class='bold'>{self.jsoni[kwarg_['path']]['subtitle']}</pre><pre>{self.jsoni[kwarg_['path']]['description']}</pre></div></li>
{chr(10).join(["<li><div class='l'><div class='ll'><img src='"+kwarg_['imageurl']+"/image/"+self.utili.gjf(self.jsoni[kwarg_['path']]['data'][ii],'abbreviation')+".png'/></div><div class='rr'><a href='"+self.utili.gjf(self.jsoni[kwarg_['path']]['data'][ii],'url',**kwarg_)+"'><pre class='bold gold'>"+self.utili.gjf(self.jsoni[kwarg_['path']]['data'][ii],'title')+"</pre><pre>"+self.utili.gjf(self.jsoni[kwarg_['path']]['data'][ii],'description')+"</pre></a><a class='space'></a><pre class='space'>"+self.utili.gjf(self.jsoni[kwarg_['path']]['data'][ii],'date')+"</pre></div></div>"+("</li>" if ii == (len(self.jsoni[kwarg_['path']]['data'])-1) else "")  if not ii%2 else "<div class='right'><div class='ll'><img src='"+kwarg_['imageurl']+"/image/"+self.utili.gjf(self.jsoni[kwarg_['path']]['data'][ii],'abbreviation')+".png'/></div><div class='rr'><a href='"+self.utili.gjf(self.jsoni[kwarg_['path']]['data'][ii],'url',**kwarg_)+"'><pre class='bold gold'>"+self.utili.gjf(self.jsoni[kwarg_['path']]['data'][ii],'title')+"</pre><pre>"+self.utili.gjf(self.jsoni[kwarg_['path']]['data'][ii],'description')+"</pre></a><a class='space'></a><pre class='space'>"+self.utili.gjf(self.jsoni[kwarg_['path']]['data'][ii],'date')+"</pre></div></div></li>" for ii in range(len(self.jsoni[kwarg_['path']]['data']))])}
  </ul>
<div style='clear:both'></div>
''')
 elif re.search(r'^research\/\w+([.]html)?$',kwarg_['path'],flags=re.I):
  return re.sub(r'http://minhinc.42web.io',kwarg_['imageurl'],open(self.cwd+re.sub(r'^research',r'/static',kwarg_['path'])+('.html' if not re.search(r'[.]html$',kwarg_['path'],flags=re.I) else '')).read(),flags=re.DOTALL)
