import os
import hashlib
import traceback
import sys
try:
	import urllib2
except Exception, e:
    traceback.print_exc()
    
full_path=sys.argv[1]
language=sys.argv[2]
#full_path="/home/rs/Desktop/java training/Crash.avi"
#language="en"
#print "rahil sharam"

def get_hash(name):
        readsize = 64 * 1024
        with open(name, 'rb') as f:
            size = os.path.getsize(name)
            data = f.read(readsize)
            f.seek(-readsize, os.SEEK_END)
            data += f.read(readsize)
        return hashlib.md5(data).hexdigest()
        
hash_value=get_hash(full_path)
#hash_value="ffd8d4aa68033dc03d1c8ef373b9028c"
if not os.path.exists(full_path+".srt"):

        headers = { 'User-Agent' : 'SubDB/1.0 (quick-subtitles/1.0; http://github.com/rs91092/quick-subtitles)' }
        url = "http://api.thesubdb.com/?action=download&hash="+hash_value+"&language="+language
        req = urllib2.Request(url, '', headers)
        response = urllib2.urlopen(req).read()
        with open (full_path+".srt","wb") as subtitle:
            subtitle.write(response)
