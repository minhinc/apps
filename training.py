import re

def training(self,**kwarg_):
 if kwarg_['path'].count(r'/')==0:
  return self.research(**kwarg_)
 elif kwarg_['path'].count(r'/')==1:
  subtopic,topic=re.sub(r'^.*?/(.*)',r'\1',kwarg_['path']),re.sub(r'^(.*)/.*$',r'\1',kwarg_['path'])
  index=[ii for ii in range(len(self.jsoni[topic]['data'])) if subtopic==self.utili.gjf(self.jsoni[topic]['data'][ii],'abbreviation')][0]
  return (f'''<div class='downloadleft'>
<ul class='tablist'>
<a href='{kwarg_['staticurl']}/{topic}/'><li class='header'><p>{topic}</p></li></a>
{chr(10).join(["<li class='current'><p class='padtop'>"+self.utili.gjf(self.jsoni[topic]['data'][ii],'title')+"</p></li>" if self.utili.gjf(self.jsoni[topic]['data'][ii],'abbreviation')==subtopic else "<a href='"+kwarg_['staticurl']+"/"+topic+"/"+self.utili.gjf(self.jsoni[topic]['data'][ii],'abbreviation')+"'><li class='"+['light','dark'][ii%2]+"'><p>"+self.utili.gjf(self.jsoni[topic]['data'][ii],'title')+"</p></li></a>" for ii in range(len(self.jsoni[topic]['data']))])}
 </ul>
</div>
<div class='downloadright'>
 <ul class='agenda'>
  <li class='header'><p>{self.utili.gjf(self.jsoni[topic]['data'][index],'title')} Essentials</p></li>
  <li><h1>{self.utili.gjf(self.jsoni[topic]['data'][index],'title')} Essentials</h1>
  <p class='m'>Get familiar with {self.utili.gjf(self.jsoni[topic]['data'][index],'title')} Concepts</p>
  <h3>Course details</h3></li>
  <li><p class='l'>Duration:</p> <p class='r'>{self.utili.gjf(self.jsoni[topic]['data'][index],'duration')} days</p></li>
  <li><p class='l'>Agenda</p>:<a class='r' href='{kwarg_['staticurl']}/{topic}/{subtopic}/advance-{subtopic}-slides'><pre style='font-size:15pt;font-weight:bold;color:#400000;display:inline;padding:0'>Slides</pre></a></li>
  <li><p class='l'>Training materials</p>:<a class='r' href='{kwarg_['staticurl']}/{topic}/{subtopic}/advance-{subtopic}-slides'><pre style='font-size:15pt;font-weight:bold;color:#400000;display:inline;padding:0'>Slides</pre></a><p class='r'> Labs/Results</p></li>
  <li><p class='l'>Written language</p>: <p class='r'>English</p></li>
  <li><p class='l'>Available oral languages:</p> <p class='r'>English</p></li>
  <li><p class='l'>Register For Online Training: </p><p class='r'><a href='{kwarg_['staticurl']}/online' class='bold' style='font-size:16pt;color:#ff4444;'>Click here</a></p></li>
 </ul>
{chr(10).join([" <ul class='publication' style='clear:both;'><li class='header'><p>"+ii+"</p></li>"+chr(10).join(["<li><a href='"+self.utili.gjf(self.jsoni[ii]['data'][jj],'url',**kwarg_)+"'> - "+self.utili.gjf(self.jsoni[ii]['data'][jj],'title')+"</a><p class='italic inline'>"+self.utili.gjf(self.jsoni[ii]['data'][jj],'publisher')+","+self.utili.gjf(self.jsoni[ii]['data'][jj],'date')+"</p><p class='i'>"+self.utili.gjf(self.jsoni[ii]['data'][jj],'description')+"</p></li>" for jj in range(len(self.jsoni[ii]['data'])) if self.utili.percentmatch(sourcel_=self.utili.gjf(self.jsoni[topic]['data'][index],'title'),targets_=self.utili.gjf(self.jsoni[ii]['data'][jj],'description'))])+chr(10)+" </ul>" for ii in ['research','product']])}
</div>
''' if not kwarg_['mobile'] else f''' <ul class='three'>
<li class='header'><pre class='header'>{self.utili.gjf(self.jsoni[topic]['data'][index],'title')} Essentials</pre></li>
<li class='table'><h3>{self.utili.gjf(self.jsoni[topic]['data'][index],'title')} Essentials</h3>
<pre class='f10'>Get familiar with {self.utili.gjf(self.jsoni[topic]['data'][index],'title')} Concepts</pre>
<h4>Course details</h4>
<pre class='f10'><span class='bold'>Duration: </span>{self.utili.gjf(self.jsoni[topic]['data'][index],'duration')} days</pre>
<pre class='f10'><span class='bold'>Agenda: </span><a href='{kwarg_['staticurl']}/{topic}/{subtopic}/advance-{subtopic}-slides'<span class='bold gold f14'>Slides</span></pre></a>
<pre class='f10'><span class='bold'>Training materials: </span><a href='{kwarg_['staticurl']}/{topic}/{subtopic}/advance-{subtopic}-slides'><span class='bold gold f14'>Slides</span></a> <span class='f8'>Labs/Results</span></pre>
<pre class='f10'><span class='bold'>Written language: </span><span class='f8'>English</span></pre>
<pre class='f10'><span class='bold'>Available oral languages: </span><span class='f8'>English</span></pre>
<pre class='f10' style='margin-top:5px'><span class='bold'>Register For Online Training: </span><a href='{kwarg_['staticurl']}/online' class='bold' style='font-size:16pt;color:#ff4444;'>Click here</a></pre></li><div class='clr'></div>
{chr(10).join(["<li class='ht' style='margin-top:5px;'><pre>"+ii+"</pre></li>"+chr(10).join(["<li class='htl'><a class='link' href='"+self.utili.gjf(self.jsoni[ii]['data'][jj],'url',**kwarg_)+"'>"+self.utili.gjf(self.jsoni[ii]['data'][jj],'title')+"</a><pre class='italic inline'>"+self.utili.gjf(self.jsoni[ii]['data'][jj],'publisher')+","+self.utili.gjf(self.jsoni[ii]['data'][jj],'date')+"</pre><pre class='italic'>"+self.utili.gjf(self.jsoni[ii]['data'][jj],'description')+"</pre></li><div class='clr'></div>" for jj in range(len(self.jsoni[ii]['data'])) if self.utili.percentmatch(sourcel_=self.utili.gjf(self.jsoni[topic]['data'][index],'title'),targets_=self.utili.gjf(self.jsoni[ii]['data'][jj],'description'))]) for ii in ['research','product']])}
 </ul>
 <div class='clr'>
</div>
''')
 elif kwarg_['path'].count(r'/')==2:
  return re.sub(r'http:\/\/minhinc.42web.io\/image',kwarg_['imageurl']+'/image',open(self.cwd+'/static/'+re.sub(r'[.]php$','',kwarg_['path'])+('-chap'+kwarg_['request'].args['chap'] if 'chap' in kwarg_['request'].args else '')+('_m' if kwarg_['mobile'] else '')+'.txt').read(),flags=re.I|re.DOTALL)
"""
{chr(10).join([" <ul class='publication' style='clear:both;'><li class='header'><p>"+ii+"</p></li>"+chr(10).join(["<li><a href='"+self.utili.gjf(self.jsoni[ii]['data'][jj],'url',**kwarg_)+"'> - "+self.utili.gjf(self.jsoni[ii]['data'][jj],'title')+"</a><p class='italic inline'>"+self.utili.gjf(self.jsoni[ii]['data'][jj],'publisher')+","+self.utili.gjf(self.jsoni[ii]['data'][jj],'date')+"</p><p class='i'>"+self.utili.gjf(self.jsoni[ii]['data'][jj],'description')+"</p></li>" for jj in range(len(self.jsoni[ii]['data'])) if self.utili.percentmatch(sourcel_=self.utili.gjf(self.jsoni[topic]['data'][index],'title'),targets_=self.utili.gjf(self.jsoni[ii]['data'][jj],'description'))])+chr(10)+" </ul>" for ii in ['research','product']])}

<?php
function draw($util){
$util->drawmenuleft();
$json=json_decode(mysqli_fetch_row($util->db->get('headername','content','name',$util->subitem))[0],true);
$first=TRUE;
echo '<div class="downloadright">
<ul class="screenshot">
<li class="header"><p>Screenshots</p></li>';
foreach($json['image'] as $key){
if($first){
echo '<li> <img src="'.$util->level.'/image/'.$key.'"/>';
}else{
echo '<img src="'.$util->level.'/image/'.$key.'"/></li>';
}
$first=!$first;
}
if(!$first){
echo '</li>';
}
echo '</ul>
<ul class="download">
<li class="header"><p>Download</p></li>
<li class="top"><p class="begin"/><p class="long">32bit</p></li>
<li class="top"><p class="begin"/><p class="short">installer(MB)</p><p class="short">zip(MB)</p></li>';
if(!empty($json['download'])){
echo '<li class="light"><p class="begin">Windows 7</p><a class="short" href="'.$util->level.'/binary/'.$json['download']['win32'][0].'">'.$json['download']['win32'][0].'</a><a class="short" href="'.$util->level.'/binary/'.$json['download']['win32'][1].'">'.$json['download']['win32'][1].'</a></li>';
}
echo ' </ul>
</div>';
}
?>
"""
