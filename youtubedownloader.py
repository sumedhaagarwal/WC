import os
a=input()
b=input("Enter 1 for mp3 or 2 for mp4 ")
if b=='2':
      os.chdir('/home/sagarwal/Videos')
      os.system('youtube-dl '+a)
else:
      os.chdir('/home/sagarwal/Music')
      os.system('youtube-dl --extract-audio --audio-format mp3 '+a)
