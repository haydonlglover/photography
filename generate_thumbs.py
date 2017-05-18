import os
from PIL import Image


inpath = "/Users/aglove2189/photography/images/thumbs/"
result = [os.path.join(dp, f) for dp, dn, filenames in os.walk(inpath) \
			for f in filenames if os.path.splitext(f)[1].lower() == '.jpg']
for r in result:
	try:
		path, file = os.path.split(r)
		im = Image.open(r)
		im.thumbnail((1024, 1024), Image.ANTIALIAS)
		im.save(r, "JPEG")
	except IOError:
		print("cannot create thumbnail for '%s'" % r)