import os
import shutil

from PIL import Image

directory = './pictures/'
new_dir = './new_pics/'

SIZE = 160, 144

# Create new directory to put resized color and gray images
if not os.path.exists(new_dir):
	os.makedirs(new_dir)
else:
	shutil.rmtree(new_dir)
	os.makedirs(new_dir)

for fileName in os.listdir(directory):
	img_name = fileName.rsplit('.', 1)[0] # extract 'imgName' from 'imgName.jpg'
	path = directory + fileName
	img = Image.open(path)
	img = img.resize(SIZE, Image.ANTIALIAS)
	resizedName = img_name + '_resized' + '.png'
	resizedPath = new_dir + resizedName
	img.save(resizedPath)
	img = img.convert('LA')
	finalName = img_name + '_resized' + '_gray' + '.png'
	finalPath = new_dir + finalName
	img.save(finalPath)


	
	


	

