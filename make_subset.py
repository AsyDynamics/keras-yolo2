#label: bottle, chair, dining table, potted plant, sofa, tv/monitor, persion

def get_file_names(path):
	file_names = [f for f in listdir(path) if isfile(join(path, f))]
	file_num = len(file_names)
	return file_num, file_names

def readtext(filename):
	direct2(label_dir)
	f = open(filename)
	lines = f.readlines()
	line_num = len(lines)
	print('Image num in total: ',line_num)
	return lines

def direct2(path):
	os.chdir(path)

def make_subset():
	lines = readtext(annotation_name)
	# direct2(image_dir)
	sum = 0
	for row in range(0,len(lines)):
		line = lines[row]
		word = line.split()
		if word[1] == '1':
			annot_name = word[0]+'.xml'
			direct2(newANNOTset_dir)
			if os.path.isfile(annot_name) == False:
				direct2(annot_dir)
				if os.path.isfile(annot_name) == True:
					# print('Copy now')
					shutil.copy(annot_name, newANNOTset_dir)
					sum = sum+1
			
	print('Find image num :',sum)

def main():
	print('Start main')

if __name__ == '__main__':
	import os
	import shutil
	label_dir  = '/home/asy/deep_learning/custom_data/VOCdevkit/VOC2012/ImageSets/Main/'
	annot_dir  = '/home/asy/deep_learning/custom_data/VOCdevkit/VOC2012/Annotations/'
	image_dir  = '/home/asy/deep_learning/custom_data/VOCdevkit/VOC2012/JPEGImages'
	newIMset_dir = '/home/asy/deep_learning/custom_data/VOCdevkit/VOC2012/newIMset'
	newANNOTset_dir = '/home/asy/deep_learning/custom_data/VOCdevkit/VOC2012/newANNOTset'
	annotation_name = 'dog_trainval.txt'
	# os.chdir('/home/asy/deep_learning/custom_data/VOCdevkit/VOC2012/ImageSets/Main')
	# os.chdir(label_dir)
	# readtext(annot_name)
	make_subset()