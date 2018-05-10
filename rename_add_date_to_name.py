from sys import argv
from PIL import Image
import glob,os,time

script, input_directory = argv
os.chdir(input_directory)
for file_name in glob.glob("*.jpg"):
    # print '%r' % file_name
	img = Image.open(file_name)
	exif_data = img._getexif()
	# print 'date image taken: %r' % exif_data[36867]
	date_image_taken = exif_data[36867]
	os.rename(file_name, date_image_taken + file_name)