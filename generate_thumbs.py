import os
from PIL import Image


inpath = "/Users/aglove2189/photography/images/fulls/"
result = [f for f in os.listdir(inpath) if os.path.isfile(os.path.join(inpath, f))]
result = [os.path.join(dp, f) for dp, dn, filenames in os.walk(inpath) \
			for f in filenames if os.path.splitext(f)[1].lower() == '.jpg']
outpath = "/Users/alove2189/photography/images/thumbs/"
for r in result:
    try:
    	im = Image.open(r)
    	im.thumbnail((512, 512), Image.ANTIALIAS)
    	im.save(os.path.join(outpath, r), "JPEG")
	except IOError:
		print("cannot create thumbnail for '%s'" % r)