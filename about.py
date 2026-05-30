import re,random
from flask import jsonify
def randomnumsum(reset=True, _cache={}):
 if reset:
  min=1;max=300;_cache['num1']=random.randint(min,max);_cache['num2']=random.randint(min,max);_cache['sum']=_cache['num1']+_cache['num2'];
 return tuple(_cache.values())
 return num1,num2,sum

def aboutus(self, **kwarg_):
 return f'''<div class='grid-table'>
 <div class='grid-cell title' style='grid-column:1 / -1'>About Us</div>
 <div class='grid-cell content' style='grid-column:1 / -1;'>Minh. Inc was established in 2015 as Research and Development center.</div>
 <div class='empty'></div>
{chr(10).join([ "<div class='grid-cell title2' style='grid-column:2 / -1'><a href='https://minhinc.github.io/"+ii[0]+"'>"+ii[0].title()+"</a></div>"+chr(10)+"<div class='grid-cell content' style='grid-column:2'><span class='dot'>&bull;</span></div><div class='grid-cell:content' style='grid-column:3 / "+("50" if not kwarg_['mobile'] else "-1")+"'>"+ii[1]+"</div><div class='empty'></div>" for ii in (('research','Company has 22 research papers, published across more than dozen publishers. Research area primary focus is Artifial intelligence, Deep Learning and 3D graphics'),('product','Company has 4 products. Company intend to develop various products in AI and 3D graphics.'),('training','Company provide training in various technologies, primarily in Machine Learning, AI and 3D Graphics.'),('service','Company also provide services in Networking and Health Care areas.'))])}
</div>'''
"""
 <div class='grid-cell title2' style='grid-column:2 / -1'><a href='https://minhinc.github.io/research'>Research</a></div>
 <div class='grid-cell content' style='grid-column:2'><span class='dot'>&bull;</span></div><div class='grid-cell:content' style='grid-column:3 / {"span calc(3*10)" if not kwarg_['mobile'] else "-1"}'>Company has 22 research papers, published across more than dozen publishers. Research area primary focus is Artifial intelligence, Deep Learning and 3D graphics.</div>
 <div class='empty2'></div>
 <div class='grid-cell title2' style='grid-column:2 / span 10'><a href='https://minhinc.github.io/product'>Product</a></div>
 <div class='grid-cell content' style='grid-column:2'><span class='dot'>&bull;</span></div><div class='grid-cell content' style='grid-column:3 / calc(3*14)'>Company has 4 products. Company intend to develop various products in AI and 3D graphics.</div>
 <div class='empty2'></div>
 <div class='grid-cell title2' style='grid-column:2 / span 10'><a href='https://minhinc.github.io/training'>Training</a></div>
 <div class='grid-cell content' style='grid-column:2'><span class='dot'>&bull;</span></div><div class='grid-cell content' style='grid-column:3 / calc(3*14)'>Company provide training in various technologies, primarily in Machine Learning, AI and 3D Graphics.</div>
 <div class='empty2'></div>
 <div class='grid-cell title2' style='grid-column:2 / span 10'><a href='https://minhinc.github.io/service'>Services</a></div>
 <div class='grid-cell content' style='grid-column:2'><span class='dot'>&bull;</span></div><div class='grid-cell content' style='grid-column:3 / calc(3*14)'>Company also provide services in Networking and Health Care areas.</div>
"""

def uploadcv(self, **kwarg_):
# subtopic,topic=re.sub(r'^.*?/(.*)',r'\1',kwarg_['path']),re.sub(r'^(.*)/.*$',r'\1',kwarg_['path'])
 subtopic,topic="cv",kwarg_['path']
 return (f'''<div class='downloadleft'>
<ul class='tablist'>
<a href='{kwarg_['staticurl']}/{topic}/'><li class='header'><p>{topic}</p></li></a>
{chr(10).join(["<li class='current'><p class='padtop'>"+self.utili.gjf(self.jsoni[topic]['data'][ii],'title')+"</p></li>" if self.utili.gjf(self.jsoni[topic]['data'][ii],'abbreviation')==subtopic else "<a href='"+kwarg_['staticurl']+"/"+topic+"/"+self.utili.gjf(self.jsoni[topic]['data'][ii],'abbreviation')+"'><li class='"+['light','dark'][ii%2]+"'><p>"+self.utili.gjf(self.jsoni[topic]['data'][ii],'title')+"</p></li></a>" for ii in range(len(self.jsoni[topic]['data']))])}
 </ul>
</div>
<div class='downloadright'>
<ul class='description'>
<li class='header'><p>File Upload Form</p></li>
<li class='light'>
<p>Minh, Inc. is looking for C++ and Python developers in Networking, <br>Multimedia and Graphics domain.</p>
<h3>Upload Resume</h3>
<p>(.doc(x) .pdf)</p>
<form class='common' enctype='multipart/form-data'>
<p>Filename:<input type='file' name='photo' id='attachmentid' class='mandatory'></p>
<p><input type='submit' name='submit' id='submitid' value='Upload' style='background-color:#ffaa88;color:#fff' disabled><pre class="l3" id="iframeid" style="margin-left:5%;color:#001400;font-size:14pt;font-weight:bold;height:30px"></pre></p>
</form>
</li>
</ul>
</div>
''' if not kwarg_['mobile'] else f'''<ul class='seven'>
<li class='header'><pre class='header'>File Upload Form</pre></li>
<li class='light'>
<pre class='f10'>Minh, Inc. is looking for C++ and Python developers in Networking, Multimedia and Graphics domain.</pre>
<h3>Upload Resume</h3>
<p>(.doc(x) .pdf .txt)</p>
<form class='common' enctype='multipart/form-data'>
<div><pre class='bold f12 inline'>Filename:</pre><input class='inline mandatory' type='file' name='photo' id='attachmentid'></div>
<p><input type='submit' name='submit' value='Upload'  id='submitid' style='background-color:#ffaa88;color:#fff' disabled></p>
</form>
</li>
 </ul>
<div class="clr"></div>
''')+f'''
<script type="mpy" config='{{"interpreter":"/static/micropython/micropython.mjs"}}' src="/static/pyscriptevent.py">
</script>
'''

def contact(self, **kwarg_):
 print(f'>< contact {kwarg_=}')
 return f'''<style>
#map {{
height:248px;
width:359px;
}}
</style>
 {"""<ul class='contact'>
  <li class='header'><p>CONTACT US</p></li>
  <li class='main'>
   <div id='map'></div>""" if not kwarg_['mobile'] else """ <ul class='ten'>
 <li class='header'><pre class='header'>CONTACT US</pre></li>
 <li class='main'>
 <div style='clear:both;float:left;width:49%;' id='map'></div>"""}
   <script>
    function initMap(){{
     var uluru={{lat:13.035357,lng:77.576285}};
     var map=new google.maps.Map(document.getElementById('map'),{{ zoom:4, center:uluru }});
     var marker=new google.maps.Marker({{ position:uluru, map:map }});
    }}
  </script>
  <script async defer
   src='https://maps.googleapis.com/maps/api/js?key=AIzaSyCypT5QJIhCg6kqW808Rsn-mXl-dJVtw0M&callback=initMap'>
  </script>
  {"""<div class='r'><p class='b' style='font-family:mytwcenmt;font-size:24pt;color:#004000'>Minh, Inc.</p><div class='dl'><p class='n'>Tel: +91 9483160610<img src='"""+kwarg_['imageurl']+"""/image/whatsapp.png' width='20px' height='20px'> <br>Email: <a href='mailto:tominhinc@gmail.com'><span class='green'>tominhinc@gmail.com</span></a></p></div><div class='dr'><p>#85<br>5th Main<br>P&T Colony<br>SanjayNagar<br>Bangalore-94</p></div></div>
 </li>
</ul>
""" if not kwarg_['mobile'] else """ <div class='right'><pre class='name' style='margin-left:10%'>Minh, Inc.</pre><pre class='f10' style='margin-left:10%;'>#85<br>5th Main<br>P&T Colony<br>SanjayNagar<br>Bangalore-94</pre><pre class='phone f10 bold' style='margin-left:10%'>+91 9483160610 <img src='"""+kwarg_['imageurl']+"""/image/whatsapp.png' width='20px' height='20px'></pre><pre class='f10 bold' style='margin-top:8px;margin-left:10%;color:#4080ff;'><a href='mailto:tominhinc@gmail.com'>tominhinc@gmail.com</a></pre></div>
</li>
<li class='form'>
<a href='{kwarg_['staticurl']}/training/ml'><img style='margin-left:31%;width:38%' src='http://minhinc.42web.io/image/mltraininglogo.gif'></img></a>
"""}
<form class='online' enctype='multipart/form-data' {"style='float:left'" if kwarg_['mobile'] else ""}>
 <h1>Reach Out To Us</h1>
 <div class='row'><pre class='lc bold'>Name:</pre><input type='text' name='name' placeholder='Your Name' class='l'></div>
 <div class='row'><pre class='lc bold'>Email:</pre><input id='emailid' type='text' name='email' placeholder='Email Address' class='l mandatory'><pre class='ls bold star'>*</pre></div>
 <div class='rowtextarea'><pre class='lc bold'>Comment:</pre><textarea id='messageid' rows='5' name='message' cols='40' class='l2 mandatory' ></textarea><pre class='ls bold star'>*</pre></div>
 <div class='row' style='margin-top:20px'><pre class='lc bold' id='quiztextid' style='font-size:14pt;color:#ff0000'>{randomnumsum()[0]}+{randomnumsum(False)[1]}</pre><input type='text' class='quiz-control l mandatory'> <pre class='ls bold star'>*</pre></div>
 <div class="row" style="margin-top:20px"><input data-res={randomnumsum(False)[2]} type="submit" name="submit" value="Submit" class="submit lc bold disable" id="submitid" disabled><pre class="l3" id="iframeid" style="margin-left:5%;color:#001400;font-size:14pt;font-weight:bold;height:30px"></pre></div>
</form>
{"""<a href='{kwarg_['staticurl']}/training/ml'><img style='float:left;width:34%' src='http://minhinc.42web.io/image/mltraininglogo.gif'></img></a>
<div style="clear:both"></div>""" if not kwarg_['mobile'] else """
 </li>
</ul>
<div style="clear:both"></div>"""}
<script type="mpy" config='{{"interpreter":"/static/micropython/micropython.mjs"}}' src="/static/pyscriptevent.py">
</script>'''

def online(self, **kwarg_):
 print(f'>< online {kwarg_=}')
 return f'''<ul class='common'>
 <li class='header'><pre>Online Training</pre></li>
 <li><pre class='register'>{"Register For Online Training" if kwarg_['path']=='online' else "Ask a Programming Question"}</li>
<!--<span style='color:#ff8844;font-size:14pt'>Upcoming training : Qml <a href='http://minhinc.42web.io/training/advance-qml-agenda.php' style='text-decoration:underline;font-size:14pt;color:#004000'>See Agenda</a></span></pre>--></li>
</ul>
<form class='online'  enctype='multipart/form-data' style='float:left'>
 <div class='row'><pre class='lc bold'>Technology</pre>
 <select id='selecttechid' value='' name='technology' class='l mandatory'>
   <option>-- Select --</option>
   {chr(10).join(["<option>"+self.utili.gjf(self.jsoni['training']['data'][ii],'title')+"</option>" for ii in range(len(self.jsoni['training']['data']))])}
 </select><pre class='ls bold star'>*</pre></div>
 {"""<div class='row'><pre class='lc bold'>Fee:</pre><pre class='l bold' id='chargeid'></pre></div>
 <div class='row'><pre class='lc bold'>Duration:</pre><pre class='l bold' id='durationid'></pre></div>""" if kwarg_['path']=='online' else ''}
 <div class='row'><pre class='lc bold'>Course Content:</pre><a class='l bold block' href='' id='courseid' target='_blank'></a></div>
 <div class='row'><pre class='lc bold'>Name:</pre><input type='text' name='name' placeholder='Your Name' class='l'></div>
 <div class='row'><pre class='lc bold'>Email:</pre><input id='emailid' type='text' name='email' placeholder='Email Address' class='l mandatory'><pre class='ls bold star'>*</pre></div>
 <div class='row' style='margin-top:10px;'><pre class='lc bold' style='font-size:8pt'>Supporting{chr(10)}Document:</pre><input type='file' name='attachment' id='attachmentid' class='l3 mandatory' style='width:50%'><pre class='l3' style='font-size:8pt;width:20%'>pdf,docx{chr(10)}txt,png<2MB</pre></div>
 <div class='rowtextarea' ><pre class='lc bold'>Comment:</pre><textarea id='messageid' rows='5' name='message' cols='40' class='l2 mandatory' ></textarea><pre class='ls bold star'>*</pre></div>
 <div class='row'><pre class='lc bold' style='padding-top:4px'>When you'{chr(10)}need?</pre><input type='date' name='tdate' class='l3 mandatory' id='dateid' ><pre class='ls bold star'>*</pre></div>
 <div class='row' style='margin-top:20px'><pre class='lc bold' id='quiztextid' style='font-size:14pt;color:#ff0000'> {randomnumsum(True)[0]}+{randomnumsum(False)[1]} ?</pre><input type='text' class='quiz-control l mandatory'> <pre class='ls bold star'>*</pre></div>
 <div class="row" style="margin-top:20px;"><input data-res={randomnumsum(False)[2]} type="submit" name="submit" value="Submit" class="submit lc bold disable" id="submitid" disabled><pre class="l3" id="iframeid" style="margin-left:5%;color:#001400;font-size:14pt;font-weight:bold;height:30px;"></pre></div>
</form>
<a href='{kwarg_['staticurl']}/training/py'><img style='float:left;width:34%' src='http://minhinc.42web.io/image/pytraininglogo.gif'></img></a>
<div style='clear:both'></div>
<script type="mpy" config='{{"interpreter":"/static/micropython/micropython.mjs"}}' src="/static/pyscriptevent.py">
</script>'''

def about(self, **kwarg_):
 print(f'>< about {kwarg_=}')
 if re.search(r'^(about|help)$',kwarg_['path'],flags=re.I):
  return aboutus(self,**kwarg_)
 elif re.search(r'^about/contact$',kwarg_['path'],flags=re.I):
  return contact(self,**kwarg_)
 elif re.search(r'^(online|about/question)$',kwarg_['path'],flags=re.I):
  return online(self,**kwarg_)
 elif re.search('^career$',kwarg_['path'],flags=re.I):
  return uploadcv(self,**kwarg_)
 elif re.search(r'^jsonquery$',kwarg_['path'],flags=re.I):
  ret=self.jsoni
  for le in kwarg_['request'].get_json():
    ret=ret[le]
  print(f'<> about {ret=}')
  return jsonify(ret)

def jsonquery(self, **kwarg_):
 return about(**kwarg_)

"""
<?php
function draw($util){
$util->drawmenuleft();
$json=json_decode(mysqli_fetch_row($util->db->get('headername','content','name',$util->headername))[0],true);
echo '<div class="downloadright">
<ul class="description">
<li class="header"><p>File Upload Form</p></li>
<li class="light">
<p>Minh, Inc. is looking for C++ and Python developers in Networking, <br>Multimedia and Graphics domain.</p>
<h3>Upload Resume</h3>
<p>(.doc(x) .pdf)</p>
<form class="common" action="'.$util->level.'/php/upload_manager.php" method="post" target="myIframe" enctype="multipart/form-data">
<p>Filename:<input type="file" name="photo" id="fileSelect"></p>
<p><input type="submit" name="submit" value="Upload"></p>
<iframe name="myIframe" frameborder="0" scrolling="no">
</iframe>
</form>
</li>
</ul>
</div>';
}
?>
<?php
function draw($util){
echo ' <ul class="seven">
<li class="header"><pre class="header">File Upload Form</pre></li>
<li class="light">
<pre class="f10">Minh, Inc. is looking for C++ and Python developers in Networking, Multimedia and Graphics domain.</pre>
<h3>Upload Resume</h3>
<p>(.doc(x) .pdf .txt)</p>
<form class="common" action="'.$util->level.'/php/upload_manager.php" method="post" target="myIframe" enctype="multipart/form-data">
<div><pre class="bold f12 inline">Filename:</pre><input class="inline" type="file" name="photo" id="fileSelect"></div>
<p><input type="submit" name="submit" value="Upload"></p>
<iframe name="myIframe" frameborder="0" scrolling="no">
</iframe>
</form>
</li>
 </ul>
<div class="clr"></div>';
}
?>
"""

def help(self,**kwarg_):
 return self.about(**kwarg_)

def career(self,**kwarg_):
 return self.about(**kwarg_)

