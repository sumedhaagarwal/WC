import os
a=input("Enter URL: ")
b=input("For audio press 1 and for video press 2: ")
print(b)
M_path = "/Music"
V_path = "/Videos"

if b==1:
    print('1')
    c=input("For default path press 1 and for any other path press 2: ")
    if c==1:
		os.chdir(M_path)
		os.system('youtube-dl --extract-audio --audio-format mp3 '+a)
    else:
		path=input("Enter Path: ")
		os.chdir(path)
		os.system('youtube-dl --extract-audio --audio-format mp3 '+a)
else:
	c=input("For default path press 1 and for any other path press 2: ")
	if c==1:
		os.chdir(V_path)
		os.system('youtube-dl '+a)
	else:
		path=input("Enter Path: ")
		os.chdir(path)
		os.system('youtube-dl '+a)
