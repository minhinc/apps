import re
def switch(reset=False,_cache={}):
 if not 'flag' in _cache: _cache['flag']=False
 if reset: _cache['flag']=not _cache['flag']
 return _cache['flag']

def service(self, **kwarg_):
 print(f'>< service {kwarg_=}')
 if re.search(r'^service$',kwarg_['path'],flags=re.I):
  return f'''{self.utili.downloadleft(topic='service',subtopic='network',**kwarg_) if not kwarg_['mobile'] else ''}
 <div class='serviceright'>
 <ul class='{"desservice" if not kwarg_['mobile'] else "five"}'>
  <li class="header"><p>{self.jsoni[kwarg_['path']]['subtitle']}</p></li>
  <li class="dark"><p>{self.jsoni[kwarg_['path']]['description']}</p></li>
{chr(10).join([(("  <li class='"+['light','dark'][ii%2]+"'>" if not ii%2 else "")+"<div class='"+['l','r'][ii%2]+"'><img src='"+kwarg_['imageurl']+"/image/"+self.utili.gjf(self.jsoni[kwarg_['path']]['data'][ii],'abbreviation')+".png'/><div><p>"+self.utili.gjf(self.jsoni[kwarg_['path']]['data'][ii],'title')+" - "+self.utili.gjf(self.jsoni[kwarg_['path']]['data'][ii],'description')+"</p><a class='red italic' href='"+kwarg_['staticurl']+"/service/"+self.utili.gjf(self.jsoni[kwarg_['path']]['data'][ii],'abbreviation')+"'>...read more</a></div></div>" if not kwarg_['mobile'] else ("  <li class='"+['light','dark'][ii%2]+"'>" if not ii%2 else "")+"<div class='"+['l','right'][ii%2]+"'><img class='ll' src='"+kwarg_['imageurl']+"/image/"+self.utili.gjf(self.jsoni[kwarg_['path']]['data'][ii],'abbreviation')+".png'/><div class='rr'><pre>"+self.utili.gjf(self.jsoni[kwarg_['path']]['data'][ii],'title')+" - "+self.utili.gjf(self.jsoni[kwarg_['path']]['data'][ii],'description')+"</pre><a class='red italic' href='"+kwarg_['staticurl']+"/service/"+self.utili.gjf(self.jsoni[kwarg_['path']]['data'][ii],'abbreviation')+"'>...read more</a></div></div>")+("</li>" if ii%2 or ii==(len(self.jsoni[kwarg_['path']]['data'])-1) else "") for ii in range(len(self.jsoni[kwarg_['path']]['data']))])}
 </ul>
{"</div>" if not kwarg_['mobile'] else "<div style='clear:both;'></div>"}
'''
 elif kwarg_['path'].count(r'/')==1:
  subtopic,topic=re.sub(r'^.*?/(.*)',r'\1',kwarg_['path']),re.sub(r'^(.*)/.*$',r'\1',kwarg_['path'])
  index=[ii for ii in range(len(self.jsoni[topic]['data'])) if subtopic==self.utili.gjf(self.jsoni[topic]['data'][ii],'abbreviation')][0]
  print(f'<=> service {(topic,index)=}')
  return (f'''{self.utili.downloadleft(topic=topic,subtopic=subtopic,**kwarg_)}
<div class='serviceright'>
<ul class='desservice'>
<li class='header'><p>{subtopic.title()}</p></li>
<li class='dark'><p>Company has following products in {self.utili.gjf(self.jsoni[topic]['data'][index],'title')}</p></li>
{chr(10).join([("<li class='"+['light','dark'][switch()]+"'>" if switch(True) else "")+"<div class="+['l','r'][switch()]+"'><img src='"+kwarg_['imageurl']+'/image/'+self.utili.gjf(self.jsoni['product']['data'][jj],'abbreviation')+".png'/><div><p>"+self.utili.gjf(self.jsoni['product']['data'][jj],'title')+" - "+self.utili.gjf(self.jsoni['product']['data'][jj],'description')+"</p><a class='btnBlueGloss' href='"+kwarg_['staticurl']+"/product/"+self.utili.gjf(self.jsoni['product']['data'][jj],'abbreviation')+"'>... more</a></div></div>"+("</li>" if not switch() or jj==(len(self.jsoni['product']['data'])-1) else "") for jj in range(len(self.jsoni['product']['data'])) if self.utili.percentmatch(sourcel_=self.utili.gjf(self.jsoni[topic]['data'][index],'title'),targets_=self.utili.gjf(self.jsoni['product']['data'][jj],'description'))])}
 </ul>
</div>
''' if not kwarg_['mobile'] else f'''<ul class='five'>
 <li class='header'><pre>{subtopic.title()}</pre></li>
 <li class='dark' style='margin-bottom:10px'><pre>Company has following products in {self.utili.gjf(self.jsoni[topic]['data'][index],'title').title()}</pre></li>
{chr(10).join([("<li class='"+['light','dark'][switch()]+"'>" if switch(True) else "")+"<div class="+['l','right'][switch()]+"'><img class='ll' src='"+kwarg_['imageurl']+'/image/'+self.utili.gjf(self.jsoni['product']['data'][jj],'abbreviation')+".png'/><div class='rr'><pre>"+self.utili.gjf(self.jsoni['product']['data'][jj],'title')+" - "+self.utili.gjf(self.jsoni['product']['data'][jj],'description')+"</pre><a class='btnBlueGloss' href='"+kwarg_['staticurl']+"/product/"+self.utili.gjf(self.jsoni['product']['data'][jj],'abbreviation')+"'>... more</a></div></div>"+("</li>" if not switch() or jj==(len(self.jsoni['product']['data'])-1) else "") for jj in range(len(self.jsoni['product']['data'])) if self.utili.percentmatch(sourcel_=self.utili.gjf(self.jsoni[topic]['data'][index],'title'),targets_=self.utili.gjf(self.jsoni['product']['data'][jj],'description'))])}
 </ul>
<div style='clear:both'></div>
''')
"""
$first=TRUE;
$light="";
foreach(json_decode(mysqli_fetch_row($util->db->get('headername','content','name','product'))[0],true)['child'] as $key){
$item=json_decode(mysqli_fetch_row($util->db->get('headername','content','name',$key))[0],true);
if(in_array($util->subitem,$item['service'])){
if($first){
if($light=="light"){$light="dark";}else{$light="light";}
echo '<li class="'.$light.'"><div class="l"><img class="ll" src="'.$util->level.'/image/'.$key.'.png"/><div class="rr"><pre>'.$item['title'].' - '.$item['description'].'</pre><a class="btnBlueGloss" href="'.$util->level.'/product/'.$key.'">... more</a></div></div>';
}else{
echo '<div class="right"><img class="ll" src="'.$util->level.'/image/'.$key.'.png"/><div class="rr"><pre>'.$item['title'].' - '.$item['description'].'</pre><a class="btnBlueGloss" href="'.$util->level.'/product/'.$key.'">... more</a></div></div></li>';
}
$first=!$first;
}
}
if(!empty($light) and !$first){
echo '</li>';
}
echo '</ul>
<div style="clear:both"></div>';
}
?>
"""
