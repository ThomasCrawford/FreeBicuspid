from PIL import Image
import os, glob
from pathlib import Path

images = []

#Specify hard coded path, name for gif
#--To be automated--
path = 'Generated/4'
gif_name = 'Version3'


file_list = glob.glob(path+ '/*.png') 
list.sort(file_list, key=lambda x: int(x.split('\\')[-1].split('.png')[0]))

for file_name in [file_list[0]] + [file_list[0]] + file_list:
	x = Image.open(file_name)
	x = x.resize((800,600))
	# x = x.resize((1600,1200))
	images.append(x)




images[0].save(path+'/'+gif_name+'.gif',\
		save_all=True, append_images=images, optimize=False, duration=100, loop=0)
