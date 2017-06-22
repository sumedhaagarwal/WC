import datetime
from urllib.request import urlopen, urlretrieve
from xml.dom import minidom
import os
import sys
import time

dir_path = os.path.dirname(os.path.realpath(__file__))
save_dir = dir_path+'/'+'images'
if not os.path.exists(save_dir):
	os.makedirs(save_dir)


def set_wallpaper(pic_path):
	os.system('gsettings set org.gnome.desktop.background picture-uri file://'+pic_path)
	return

def reg_change():
	path = '/home/sagarwal/codes/images'
	paths = [os.path.join(path,fn) for fn in next(os.walk(path))[2]]
	nums = len(paths)
	num=0
	for path in paths:
		set_wallpaper(path)
		num=num+1
		time.sleep(1000)
		if(num==nums):
			reg_change()


def download_wallpaper(idx=0):
	try:
		usock = urlopen('http://www.bing.com/HPImageArchive.aspx?format=xml&idx='+str(idx)+ '&n=1&mkt=ru-RU')
	except:
		pass
	try:
		xmldoc = minidom.parse(usock)
	except:
		return
	for element in xmldoc.getElementsByTagName('url'):
		url = 'http://www.bing.com' + element.firstChild.nodeValue
		now = datetime.datetime.now()
		date = now - datetime.timedelta(days=int(idx))
		pic_path = save_dir+'/'+date.strftime('bing_wp_%d-%m-%Y')+'.jpg'
		if os.path.isfile(pic_path):
			return
		urlretrieve(url.replace('_1366x768', '_1920x1200'), pic_path)

download_wallpaper()
reg_change()