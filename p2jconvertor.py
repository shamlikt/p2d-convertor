

import sys
import os
from wand.image import Image


if len(sys.argv)<4:
    print "program [root_path] [image_hight] [image_width] "
    exit()


rootdir = str(sys.argv[1])
for subdir, dirs, files in os.walk(rootdir):

    for file in files:
        if file.endswith(".pdf"):
            print os.path.join(subdir, file)

               # Converting first page into JPG
            with Image(filename=os.path.join(subdir, file)) as img:
                     img.save(filename=os.path.join(subdir,file.split('.')[0]+".jpg"))
		     

             #Resizing this image

            with Image(filename=os.path.join(subdir,file.split('.')[0]+".jpg")) as img:
                    img.resize(int(sys.argv[2]),int(sys.argv[3]))
                    img.save(filename=str(subdir)+"/thumbnail_resize.jpg")



