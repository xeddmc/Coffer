import os
import urllib.request as urllib
from coffer.utils import getRootDir
import tarfile
from coffer.utils import text

def setup():
    root = getRootDir.getCofferDir()
    envs = getRootDir.getEnvsDir()
    os.mkdir(root)
    os.mkdir(envs)
    print (text.downloadingFiles)
    deboot = urllib.urlopen("https://github.com/f-prime/Coffer/blob/master/coffer/deps/debootstrap.tar.gz?raw=true").read()
    path = root + "deboot.tar"
    with open(path, 'wb') as tarf:
        tarf.write(deboot)
    tarfile.open(path).extractall(path=root)
    os.rename(root + "debootstrap-1.0.106", root + "debootstrap") 
    os.remove(path)
    edit = open(root + "debootstrap/debootstrap").read()
    edit = "DEBOOTSTRAP_DIR={}\n".format(root + "debootstrap") + edit
    with open(root + "debootstrap/debootstrap", 'w') as w:
        w.write(edit) 

