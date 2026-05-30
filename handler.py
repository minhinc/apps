import re,json, os
import apps.misc.util,apps.headerfooter,apps.main,apps.research,apps.about,apps.service,apps.product,apps.training
class handlerc:
 def __init__(self, *arg, **kwarg):
  print(f'>< handler.init {arg=} {kwarg=}')
  self.cwd=os.getcwd()
  print(f'<=> {self.cwd=}')
  self.jsoni=json.loads(open(self.cwd+"/static/site.json").read(),object_pairs_hook=lambda m,re=re:{(int(k) if re.search(r'^\d+$',k) else k):v for k,v in m})
  self.utili=apps.misc.util.utilc(jsoni=self.jsoni)
  [exec('handlerc.'+re.sub(r'^.*?[.]','',x)+'=apps.'+x,{'self':self,'apps':apps,'handlerc':handlerc}) for x in ('main.main','research.research','product.product','service.service','training.training','about.about','about.help','about.online','about.jsonquery','headerfooter.header','headerfooter.footer','about.career')]
