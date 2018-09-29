import os.path

main_dir = os.path.split(os.path.abspath(__file__))[0]

def load_image(file):
	imagePath = os.path.join(main_dir,'icon',file)
	return imagePath

def load_xlsx(file):
	filePath = os.path.join(main_dir,file)
	return filePath