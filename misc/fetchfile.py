#!/usr/bin/env python3
import sys,os,re,traceback
from ftplib import FTP
if len(sys.argv)==1 or re.search(r'^(-H|--help)',sys.argv[1],flags=re.I):
 print(f'[python3] apps/misc/fetch.py <sourcefilename>\n  apps/misc/fetch.py apps/research.py\n  python3 apps/misc/fetch.py *\n  python3 apps/misc/fetch.py apps/*')
 print(f'Note : all paths must be for file and relative to /htdocs/render at ftpupload.net')
 sys.exit(-1)
try:
 ftp=FTP("ftpupload.net")
 ftp.login(os.getenv("FTP_USER"),os.getenv("FTP_PASSWORD"))
 root_dir='/htdocs/render'
 def retfile(remote_file):
  print(f'>< retfile {remote_file=}')
  with open(remote_file,'wb') as f:
   ftp.retrbinary(f'RETR {root_dir+"/"+remote_file}',f.write)
 def copyfile(remote_file):
  print(f'><copyfile {remote_file=}')
  if re.search(r'[*]$',remote_file):
   remote_dir=re.sub(r'/?[*]$','',remote_file)
   for remote_file, facts in ftp.mlsd(root_dir+r'/'+remote_dir):
    remote_file=remote_dir+'/'+remote_file if remote_dir else remote_file
    if facts['type']=='dir':
     os.makedirs(remote_file,exist_ok=True)
     copyfile(remote_file+'/*')
    elif facts['type']=='file':
     retfile(remote_file)
  else:
   retfile(remote_file)
 copyfile(sys.argv[1])
 ftp.close()
except Exception as e:
 print(f'Exception occured at outer layer {e=}')
 traceback.print_exc()
