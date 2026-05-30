import datetime,re
def header(self,**kwarg_):
 print(f'>< handler.header {kwarg_=}')
 return f'''<html>
<head>
<style id="fouc-guard">
  body {{ opacity: 0; }}
</style>
<script>
  let loadedCssCount = 0;
  const totalCssFiles = 3; // The number of CSS files you are tracking

  function checkAndReveal() {{
    loadedCssCount++; // Add 1 to the count every time a file finishes
    
    // Only reveal the page if the count matches the total
    if (loadedCssCount === totalCssFiles) {{
      var guard = document.getElementById('fouc-guard');
      if (guard) guard.remove(); 
      
      document.body.style.opacity = '1';
      document.body.style.transition = 'opacity 0.2s';
    }}
  }}
</script>
 <meta charset='UTF-8'>
 <meta name='description' content='Training and Research Tutorials'>
 <meta name='keywords' content='HTML, CSS, JavaScript, Python, Machine Learning, Artificial Intelligence, ML, AI, OpenGL, 3D Graphics'>
 <meta name='author' content='Minh Inc'>
 <meta name='viewport' content='width=device-width, initial-scale=1.0'>
 <link rel='icon' type='image/png' href='{kwarg_['imageurl']}/image/favicon-16x16.png' sizes='16x16'>
 <link rel='icon' type='image/png' href='{kwarg_['imageurl']}/image/favicon-32x32.png' sizes='32x32'>
 <link rel='icon' type='image/png' href='{kwarg_['imageurl']}/image/favicon-48x48.png' sizes='48x48'>
 <title>{'Minh, Inc. Software development and Outsourcing Bangalore India' if re.search("r'^"+chr(92)+"s*$'",kwarg_['path'],flags=re.I) else kwarg_['path']+'| Minh, Inc. Bangalore India'}</title>
 <link rel='stylesheet' type='text/css' href='/static/css/{"main" if not kwarg_['mobile'] else "main_m"}.css' media='all' onload='checkAndReveal()'/>
 <link rel='stylesheet' type='text/css' href='/static/css/{"agenda" if not kwarg_['mobile'] else "agenda_m"}.css' media='all' onload='checkAndReveal()'/>
 <link rel='stylesheet' type='text/css' href='/static/css/custom.css' media='all' onload='checkAndReveal()'/>
 <script type='module' src='{"/static/pyscript/core.js" if not re.search('minhinc.onrender.com',kwarg_['renderurl'],flags=re.I) else "https://pyscript.net/releases/2026.3.1/core.js"}'></script>
 <link rel='stylesheet' href='{"/static/pyscript/core.css" if not re.search('minhinc.onrender.com',kwarg_['renderurl'],flags=re.I) else "https://pyscript.net/releases/2026.3.1/core.css"}'>
</head>
<body>''' + (f''' <a href={kwarg_['staticurl']}><img src='{kwarg_['imageurl']}/image/topconLogo.png'/></a>
 <br>
 <div class='ddm'>
  <ul class='drop'>
  {chr(10).join(["<li><a href='"+kwarg_['staticurl']+"/"+ii+"'"+("style='color:#f38502'" if re.search(r'^'+ii,kwarg_['path'],flags=re.I) else "")+">"+ii.title()+"</a><ul><li class='blank'>' '</li>"+chr(10).join(["<li><a href='"+(self.utili.gjf(self.jsoni[ii]['data'][jj],'url',**kwarg_) if self.utili.gjf(self.jsoni[ii]['data'][jj],'url') else kwarg_['staticurl']+"/"+ii+"/"+self.utili.gjf(self.jsoni[ii]['data'][jj],'abbreviation'))+"'>"+self.utili.gjf(self.jsoni[ii]['data'][jj],'title').title()+"</a></li>" for jj in range(len(self.jsoni[ii]['data']) if 'data' in self.jsoni[ii] else 0 )])+"</ul></li>" for ii in self.jsoni if not ii=='index'])}
  </ul>
 </div>
 <br>
 <ul class='domain'>
  {chr(10).join(["<li><a href='"+kwarg_['staticurl']+"/"+ii[0]+"'"+("style='font-weight:bold;color:#aa4400;'" if kwarg_['path']==ii[0] else '')+">"+ii[1]+"</a></li>"+chr(10)+"<li>|</li>" for ii in (('service/network','Netorking'),('service/multimedia','Multimedia'),('service/medicalsystem','Medical Systems'),('online','Online Training'))])}
 </ul>
 <br>''' if not kwarg_['mobile'] else f'''\n <div class='menubar'>
  <a href='{kwarg_['staticurl']}'><img class='homelogo' src='{kwarg_['imageurl']}/image/topconLogo.png'/></a>
  <span class='linelogo' onclick='myFunction()'>&#9776;</span>
  <div id='myDropdown' class='dropdown-content'>
  {chr(10).join(["   <div class='line'>"+chr(10)+"    <div class='l'>"+chr(10)+"     <a "+("style='color:#f38502;font-weight:bold;'" if re.search(r'^'+ii,kwarg_['path'],flags=re.I) else "")+" href='"+kwarg_['staticurl']+"/"+ii+"'>"+ii.title()+"</a>"+chr(10)+"    </div>"+chr(10)+"""    <div class='right linesubmenu' onclick="myFunction1('linesubmenu')">"""+chr(10)+"     <div class='tr'></div>"+chr(10)+"    </div>"+chr(10)+"   </div>"+chr(10)+"   <div class='submenu'>"+chr(10)+(chr(10).join(["    <div class='linew'><a href='"+self.utili.gjf(self.jsoni[ii]['data'][jj],'url',**kwarg_)+"' style='font-size:"+str((10*30)//len(self.utili.gjf(self.jsoni[ii]['data'][jj],'title')) if len(self.utili.gjf(self.jsoni[ii]['data'][jj],'title'))>30 else 10)+"pt;color:#ff0000>'>"+self.utili.gjf(self.jsoni[ii]['data'][jj],'title').title()+"</a></div>" for jj in range(len(self.jsoni[ii]['data']) if 'data' in self.jsoni[ii] else 0)]))+chr(10)+"   </div>" for ii in self.jsoni if not ii=='index'])}
 <hr class='one'>
 <div class='line' style='border-color:transparent'><div class='l'><a {"style='color:#f38502;font-weight:bold'" if kwarg_['path']=='online' else ""}  href='{kwarg_['staticurl']}/online'>Online Training</a></div></div>
 <div class='line'><div class='l'><a {"style='color:#f38502;font-weight:bold;'" if re.search(r'^.*/qt',kwarg_['path'],flags=re.I) else ""} href='{kwarg_['staticurl']}/training/qt'>Qt Training</a></div></div>
 <div style="width:60%;margin:20px auto;">
{chr(10).join(["<a href='"+ii[0]+"""'><img width='25' height='25' style='float:left;margin-left:8px;' onmouseover="this.src='"""+ii[2]+"""'" onmouseout="this.src='"""+ii[1]+"""'"src='"""+ii[1]+"'/></a>" for ii in [['https://github.com/minhinc',kwarg_['imageurl']+'/image/githubs.png',kwarg_['imageurl']+'/image/githubscolor.png'],['https://linkedin.com/in/pravinkumarsinha',kwarg_['imageurl']+'/image/linkedins.png',kwarg_['imageurl']+'/image/linkedinscolor.png'],['https://facebook.com/minhinc',kwarg_['imageurl']+'/image/fbs.png',kwarg_['imageurl']+'/image/fbscolor.png'],['http://www.youtube.com/minhinc',kwarg_['imageurl']+'/image/youtube.png',kwarg_['imageurl']+'/image/youtubecolor.png']] ])}
   </div>
  </div>
 </div>
''')

"""
$fontsize="10";$link="";$fontmargin=30;
$json=json_decode(mysqli_fetch_row($this->db->get('headername','content','name','main'))[0],true);
foreach($json['child'] as $key){
 $color='';
 if($key==$this->headername) {$color='style="color:#f38502;font-weight:bold;"';}else{$color='';}
 $returnstring .= '<div class="line"><div class="l"><a '.$color.' href='.$this->level.'/'.$key.'>'.ucfirst($key).'</a></div><div class="right linesubmenu" onclick="myFunction1(\'linesubmenu\')"><div class="tr"></div></div></div>
  <div class="submenu">';
  $json1=json_decode(mysqli_fetch_row($this->db->get('headername','content','name',$key))[0],true);
  foreach($json1['child'] as $key1){
   $fontsize="10";
   if($key1==$this->subitem) {$color=';color:#f38502;font-weight:bold;';}else{$color='';}
   if(empty(json_decode(mysqli_fetch_row($this->db->get('headername','content','name',$key1))[0],true)['link']))
    $link=$this->level.'/'.$key.'/'.$key1;
   else
    $link=json_decode(mysqli_fetch_row($this->db->get('headername','content','name',$key1))[0],true)['link'];
   if(strlen(json_decode(mysqli_fetch_row($this->db->get('headername','content','name',$key1))[0],true)['title'])>$fontmargin)
    $fontsize=($fontsize*$fontmargin)/strlen(json_decode(mysqli_fetch_row($this->db->get('headername','content','name',$key1))[0],true)['title']);
    $returnstring .= '<div class="linew"><a href="'.$link.'" style="font-size:'.$fontsize.'pt;'.$color.'">'.ucfirst(json_decode(mysqli_fetch_row($this->db->get('headername','content','name',$key1))[0],true)['title']).'</a></div>'; }
 $returnstring .= '</div>';
}
$returnstring .= '<hr class="one">';
if($this->subitem=='online') {$color='style="color:#f38502;font-weight:bold;"';}else{$color='';}
$returnstring .= '<div class="line" style="border-color:transparent"><div class="l"><a '.$color.' href="'.$this->level.'/online">Online Training</a></div></div>';
if($this->headername=='training' && $this->subitem=='qt') {$color='style="color:#f38502;font-weight:bold;"';}else{$color='';}
$returnstring .= '<div class="line"><div class="l"><a '.$color.' href="'.$this->level.'/training/qt">Qt Training</a></div></div>';
$returnstring .= '<div style="width:60%;margin:20px auto;">';
foreach(Array(Array('https://github.com/minhinc',$this->level.'/image/githubs.png',$this->level.'/image/githubscolor.png'),Array('https://linkedin.com/in/pravinkumarsinha',$this->level.'/image/linkedins.png',$this->level.'/image/linkedinscolor.png'),Array('https://facebook.com/minhinc',$this->level.'/image/fbs.png',$this->level.'/image/fbscolor.png'),Array('http://www.youtube.com/channel/UChmiKM2jr7e9iUOrVPKRTXQ',$this->level.'/image/youtube.png',$this->level.'/image/youtubecolor.png')) as $element){
$returnstring .= '<a href="'.$element[0].'"><img width="25" height="25" style="float:left;margin-left:8px;" onmouseover=\'this.src="'.$element[2].'"\' onmouseout=\'this.src="'.$element[1].'"\' src="'.$element[1].'"/></a>';
}
$returnstring .= '</div>';
return $returnstring;
}


  </div>
 </div>

$json=json_decode(mysqli_fetch_row($this->db->get('headername','content','name','main'))[0],true);
if (!empty($json['comingevents']) && $this->headername != "about" && $this->subitem != "online"){
echo '<div style="width:90%;height:40px;margin:10px auto;background-color:#0707a2"><pre style="float:left;padding-left:5%;line-height:40px;color:#ffffff;font-family:mytwcenmt;font-size:10px;">';
echo $json['comingtraining'];
echo '</pre><a href="http://www.minhinc.42web.io/online" style="float:right;margin:5px 5%;padding:0px 5px;border-radius:5px;display:block;background-color:#53616e;line-height:30px;font-size:10px;color:#ffffff";font-family:arial, helvetica, sans;>...Know More</a></div><div style="clear:both"></div>';
}
}

"""







def footer(self,**kwarg_):
 print(f'>< handler.footer {kwarg_=}')
 return (f'''<div class="footer">
<hr>
<ul class='fl'>
 <li><p class='bold' style='margin:0px;padding:0px;'>Minh, Inc.</p></li>
 <li><p>#85, 5th Main, P&T<br>
  SanjayNagar, Bangalore<br>
  Karnataka, India 560094<br><br>
  <b>tominhinc@gmail.com</b><br></p>
  <p style='display:flex;align-items:center;gap:10px'><b>+91 9483160610</b> <img src='{kwarg_['imageurl']}/image/whatsapp_s.png' width='20px' height='20px'></p>
 </li>
</ul>
<ul class='menu'>
 {chr(10).join(["<li class='top'><a href='"+kwarg_['staticurl']+"/"+ii+"'>"+ii.title()+"</a>"+chr(10)+" <ul>"+chr(10)+" <li><hr class='product' "+('style='+chr(34)+'background-color:#f38502'+chr(34) if re.search(r'^'+ii,kwarg_['path'],flags=re.I) else '')+"></li>"+chr(10).join([" <li><a href='"+(self.utili.gjf(self.jsoni[ii]['data'][jj],'url',**kwarg_) if self.utili.gjf(self.jsoni[ii]['data'][jj],'url') else kwarg_['staticurl']+"/"+ii+"/"+self.utili.gjf(self.jsoni[ii]['data'][jj],'abbreviation'))+"' "+('style='+chr(34)+'font-weight:bold;color:#aa4400;'+chr(34) if re.search("r'"+self.utili.gjf(self.jsoni[ii]['data'][jj],'abbreviation')+"$",kwarg_['path']) else '')+">"+self.utili.gjf(self.jsoni[ii]['data'][jj],'title').title()+"</a><li>" for jj in range(len(self.jsoni[ii]['data']) if 'data' in self.jsoni[ii] else 0) if not re.search(r'^research$',ii,flags=re.I)])+chr(10)+" </ul></li>" for ii in self.jsoni if not ii in ['index','about']])}
</ul>
<ul class="fr">
 <li><p>&copy Minh Inc 2015-{datetime.datetime.now():%Y}</p></li>
 <li class="img">
{chr(10).join(['<a href='+i[0]+'><img width=25 height=25 src='+chr(34)+i[1]+chr(34)+'/></a>' for i in [['https://github.com/minhinc',kwarg_['imageurl']+'/image/githubs.png',kwarg_['imageurl']+'/image/githubscolor.png'],['https://linkedin.com/in/pravinkumarsinha',kwarg_['imageurl']+'/image/linkedins.png',kwarg_['imageurl']+'/image/linkedinscolor.png'],['https://facebook.com/minhinc',kwarg_['imageurl']+'/image/fbs.png',kwarg_['imageurl']+'/image/fbscolor.png'],['http://www.youtube.com/minhinc',kwarg_['imageurl']+'/image/youtube.png',kwarg_['imageurl']+'/image/youtubecolor.png']]])}
 </li>
</ul>
</div>''' if not kwarg_['mobile'] else f''' <div class='footer'>
  <div class='l'>
   <pre style='margin-left:5%;'>
Minh, Inc.
#85, 5th Main, P&T
SanjayNagar, Bangalore
Karnataka, India 560094

tominhinc@gmail.com</pre>
<pre style='margin-left:5%;display:flex;align-items:center;gap:10px'>+91 9483160610&nbsp&nbsp<img src='{kwarg_['imageurl']}/image/whatsapp_s.png' width='15px' height='15px'/></pre>
   <div style='margin:15px 0px 5px 0px'>
{chr(10).join(["<a href='"+ii[0]+"""'><img width='25' height='25' style='float:left;margin-left:8px;' onmouseover="this.src='"""+ii[2]+"""'" onmouseout="this.src='"""+ii[1]+"""'"src='"""+ii[1]+"'/></a>" for ii in [['https://github.com/minhinc',kwarg_['imageurl']+'/image/githubs.png',kwarg_['imageurl']+'/image/githubscolor.png'],['https://linkedin.com/in/pravinkumarsinha',kwarg_['imageurl']+'/image/linkedins.png',kwarg_['imageurl']+'/image/linkedinscolor.png'],['https://facebook.com/minhinc',kwarg_['imageurl']+'/image/fbs.png',kwarg_['imageurl']+'/image/fbscolor.png'],['http://www.youtube.com/minhinc',kwarg_['imageurl']+'/image/youtube.png',kwarg_['imageurl']+'/image/youtubecolor.png']] ])}
   </div>
  </div>
  <div class="right">
{chr(10).join(["""   <div class='fline' style='margin-bottom:10px;'><div class='inline tv footermenu' onclick="myFunction1('footermenu')"></div><a class='inline' style='margin-left:10px;font-size:13px;"""+("color:#f38502" if re.search(r'^'+ii,kwarg_['path']) else "")+"' href='"+kwarg_['staticurl']+"/"+ii+"'>"+ii.title()+"</a></div>"+chr(10)+"   <div class='fsubmenu'>"+chr(10)+chr(10).join(["    <div class='flinew' style='margin-bottom:5px;'><div class='fltleft ths'></div><a style='margin-left:5px;"+("color:#f38502" if self.utili.gjf(self.jsoni[ii]['data'][jj],'abbreviation')==re.sub(r'^.*/','',kwarg_['path']) else "")+"' href='"+self.utili.gjf(self.jsoni[ii]['data'][jj],'url',**kwarg_)+"'>"+self.utili.gjf(self.jsoni[ii]['data'][jj],'title').title()+"</a></div>" for jj in range(len(self.jsoni[ii]['data']) if 'data' in self.jsoni[ii] else 0)])+chr(10)+"   </div>" for ii in self.jsoni if not ii in ['index','about']])}
  </div>
  <div style="clear:both"></div>
  <pre style="text-align:center;margin-top:20px">&copy Minh, Inc 2015-{datetime.datetime.now().year}</pre>
 </div>

<script>
var menuheight={(len(self.jsoni)-1+4)*50};
var availableheight=document.documentElement.clientHeight-document.getElementById("myDropdown").getBoundingClientRect().top-20;
document.getElementById("myDropdown").style.height=(menuheight>availableheight?availableheight:menuheight) + "px";
window.onscroll=function(e){{
if(this.oldScroll > this.scrollY){{
 document.getElementById("myDropdown").style.height=(menuheight>availableheight?availableheight:menuheight) + "px";
 }}else{{
 document.getElementById("myDropdown").style.height=(menuheight>availableheight?availableheight:menuheight)+document.getElementById("myDropdown").getBoundingClientRect().top+20+"px";
}}
this.oldScroll = this.scrollY;
}}
function myFunction() {{
/*    document.getElementById("myDropdown").classList.toggle("show"); */
 if(document.getElementById("myDropdown").style.width==="70%"){{
  document.getElementById("myDropdown").style.width="0";
 }}else{{
  document.getElementById("myDropdown").style.width="70%";
 }}
}}

function myFunction1(id){{
var i;
var acc=document.getElementsByClassName(id);
 for(i=0;i<acc.length;i++){{
  if(acc[i].contains(event.target)){{
   var panel=acc[i].parentNode.nextElementSibling;
   if (panel.style.display === "block") {{
    acc[i].classList.remove("th");
    acc[i].classList.add("tv");
    panel.style.display = "none";
   }} else {{
    acc[i].classList.remove("tv");
    acc[i].classList.add("th");
    panel.style.display = "block";
   }}
  }}
 }}
}}

/* if (document.getElementsByClassName("linelogo")[0].contains(event.target)){{*/
/*window.onclick=function(event) {{
 if (!event.target.matches(".myDropdown") && !event.target.matches(".linelogo")) {{
    document.getElementById("myDropdown").classList.remove("show");
 }}
}}*/
window.onclick=function(event) {{
 if(!document.getElementById("myDropdown").contains(event.target) && !document.getElementsByClassName("linelogo")[0].contains(event.target)){{
  document.getElementById("myDropdown").style.width="0";
  /*document.getElementById("myDropdown").classList.remove("show");*/
 }}
}}
</script>
''')+f'''
</body>
</html>
'''
