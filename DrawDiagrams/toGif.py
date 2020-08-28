from PIL import Image
import os, glob
from pathlib import Path

images = []

png_folder = Path("Generated")

gif_name = 'Version4'
file_list = glob.glob('Generated/**.png') 
list.sort(file_list, key=lambda x: int(x.split('\\')[1].split('.png')[0]))

for file_name in file_list:
    # if file_name.endswith('.png'):
    # print(file_name)
    # file_path = os.path.join(png_dir, file_name)
    images.append(Image.open(file_name))




images[0].save('Generated/{}.gif'.format(gif_name),
               save_all=True, append_images=images[1:], optimize=False, duration=400, loop=0)
