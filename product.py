import re

def product(self,**kwarg_):
 if kwarg_['path'].count(r'/')==0:
  return self.research(**kwarg_)
 elif kwarg_['path'].count(r'/')==1:
  subtopic,topic=re.sub(r'^.*?/(.*)',r'\1',kwarg_['path']),re.sub(r'^(.*)/.*$',r'\1',kwarg_['path'])
  index=[ii for ii in range(len(self.jsoni[topic]['data'])) if subtopic==self.utili.gjf(self.jsoni[topic]['data'][ii],'abbreviation')][0]
  return (f'''{self.utili.downloadleft(subtopic=subtopic,topic=topic,**kwarg_)}
<div class='downloadright'>
 <ul class='screenshot'>
  <li class='header'><p>Screenshots</p></li>
{chr(10).join([("<li> " if not jj%2 else "")+"<img src='"+kwarg_['imageurl']+'/image/'+self.utili.gjf(self.jsoni['product']['data'][index],'image')[jj]+"'/>"+("</li>" if jj%2 or jj==len(self.utili.gjf(self.jsoni['product']['data'][index],'image'))-1 else "") for jj in range(len(self.utili.gjf(self.jsoni['product']['data'][index],'image') or []))])}
 </ul>
<ul class='download'>
 <li class='header'><p>Download</p></li>
 <li class='top'><p class='begin'/><p class='long'>32bit</p></li>
 <li class='top'><p class='begin'/><p class='short'>installer(MB)</p><p class='short'>zip(MB)</p></li>
 {"<li class='light'><p class='begin'>Windows 7</p><a class='short' href=''></a></li>" if self.utili.gjf(self.jsoni['product']['data'][index],'binary') else ""}
 </ul>
</div>''' if not kwarg_['mobile'] else f''' <ul class='four'>
<li class='header'><pre class='header'>Screenshots</pre></li>
{chr(10).join([("<li> " if not jj%2 else "")+"<div class='"+['l','right'][jj%2]+"'><img src='"+kwarg_['imageurl']+'/image/'+self.utili.gjf(self.jsoni['product']['data'][index],'image')[jj]+"'/></div>"+("</li>" if jj%2 or jj==len(self.utili.gjf(self.jsoni['product']['data'][index],'image'))-1 else "") for jj in range(len(self.utili.gjf(self.jsoni['product']['data'][index],'image') or []))])}
<li class='dnld'><pre class='header'>Download</pre></li>
<li class='bit'><pre class='bold center'>32bit</pre></li>
<li class='zip'><pre class='l'>installer(MB)</pre><pre class='right'>zip(MB)</pre></li>
{"<li class='os'><div><pre>Windows 7</pre></div><div class='zip'><pre class='l bold'><a href=''></a></li>" if self.utili.gjf(self.jsoni['product']['data'][index],'binary') else ""}
 </ul>
<div class="clr"></div>
''')

