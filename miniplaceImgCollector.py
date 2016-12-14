import os
import shutil
from PIL import Image

path = './images/train/'

images_all = './pictures/'

if not os.path.exists(images_all):
	os.makedirs(images_all)
else:
	shutil.rmtree(images_all)
	os.makedirs(images_all)

for letter in os.listdir(path):
	newPath = path + letter + '/'
	for obj in os.listdir(newPath):
		newerPath = newPath + obj + '/'
		for fileName in os.listdir(newerPath):
			if os.path.isfile((newerPath+fileName)):
				img_type = fileName.rsplit('.', 1)[1]
				if img_type == 'jpeg' or img_type == 'jpg':
					filePath = newerPath + fileName
					img = Image.open(filePath)
					newName = obj + fileName
					finalPath = images_all + newName
					img.save(finalPath)
			else:
				newestPath = newerPath + fileName + '/'
				for fileNameNew in os.listdir(newestPath):
					img_type = fileNameNew.rsplit('.', 1)[1]
					if img_type == 'jpeg' or img_type == 'jpg':
						filePath = newestPath + fileNameNew
						img = Image.open(filePath)
						newName = obj + fileNameNew
						finalPath = images_all + newName
						img.save(finalPath)


