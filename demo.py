#coding:utf-8
import model
from glob import glob
import numpy as np
from PIL import Image
import time
import sys
paths = glob('./test/*.*')

if __name__ =='__main__':
    image_path = sys.argv[1]

    im = Image.open(image_path)
    img = np.array(im.convert('RGB'))
    t = time.time()
    result,img,angle = model.model(img,model='keras')
    print "It takes time:{}s".format(time.time()-t)
    print "---------------------------------------"
    for key in result:
        print result[key][1]
