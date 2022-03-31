import os,sys,json,requests
from time import sleep as waktu 

M = '\x1b[1;91m' 
H = '\x1b[1;92m'
C = '\x1b[0m' 

banner = ('''

   D U M P 

''')

def folder():
	try:os.mkdir('dump')
	except:pass

id = []

def masuk():
	try:
		token = open('token.txt','r').read()
	except FileNotFoundError:
		os.system('clear')
		token = input (f'\n masukan token > {H}')
		if token =='':
			exit (f'{M} isi yg bener{C}')
		open (f'token.txt','w').write(token)
		Menu(token)
	
	Menu(token)
	
def Menu(token):
	os.system('clear')
	print (banner)
	try:
		r = requests.get(f'https://graph.facebook.com/me?access_token={token}')
		c = json.loads(r.text)
		nama = c['name']
	except (KeyError):
		os.system('rm -rf token.txt')
		masuk()
	print (f'{C} halo {H}{nama}{C}\n ')
	try:
		folder()
		print (' isi me jika ingin dump teman sendiri ')
		uid = input (' masukan id publik : ')
		simpan = input (' simpan nama file : ')
		file = ('dump/'+simpan+'.json').replace(' ', '_')
		cok = open(file, 'w')
		r = requests.get(f'https://graph.facebook.com/{uid}?fields=friends.limit(5001)&access_token={token}')
		z = json.loads(r.text)
		for a in z['friends']['data']:
			id.append(a['id'] + '<=>' + a['name'])
			cok.write(a['id'] + '<=>' + a['name'] + '\n')
			sys.stdout.write (f'\r mengumpulkan id : {str(len(id))} ')
			sys.stdout.flush();waktu(000.01)
			
		cok.close()
		print ('\n\n berhasil dump id')
		print (f' file dump tersimpan : {file}')
		input (' ENTER')
		masuk()
	except Exception as e:
		exit (e)
		
		
masuk()

