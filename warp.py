import urllib.request
import json
import datetime
import random
import string
import time
import os
import sys

os.system("title WARP-PLUS-CLOUDFLARE")
os.system('cls' if os.name == 'nt' else 'clear')
print("[+] ABOUT SCRIPT:")
print("[-] With this script, you can getting unlimited GB on Warp+.")
print("[-] Version: 4.0.0")
referrer = os.environ["DEVICEID"]
if referrer is None: referrer = input("[#] Enter the WARP+ ID:")
print(f"[#] The WARP+ ID: {referrer}")

def gen_string(string_length):
	try:
		letters = string.ascii_letters + string.digits
		return ''.join(random.choice(letters) for _ in range(string_length))
	except Exception as error:
		print(error)


def digit_string(string_length):
	try:
		digit = string.digits
		return ''.join((random.choice(digit) for _ in range(string_length)))
	except Exception as error:
		print(error)


url = f'https://api.cloudflareclient.com/v0a{digit_string(3)}/reg'


def run():
	try:
		install_id = gen_string(22)
		body = {
			"key": "{}=".format(gen_string(43)),
			"install_id": install_id,
			"fcm_token": "{}:APA91b{}".format(install_id, gen_string(134)),
			"referrer": referrer,
			"warp_enabled": False,
			"tos": datetime.datetime.now().isoformat()[:-3] + "+02:00",
			"type": "Android",
			"locale": "es_ES"
		}
		data = json.dumps(body).encode('utf8')
		headers = {
			'Content-Type': 'application/json; charset=UTF-8',
			'Host': 'api.cloudflareclient.com',
			'Connection': 'Keep-Alive',
			'Accept-Encoding': 'gzip',
			'User-Agent': 'okhttp/3.12.1'
		}
		req = urllib.request.Request(url, data, headers)
		response = urllib.request.urlopen(req)
		status_code = response.getcode()
		return status_code
	except Exception as error:
		print(error)


good = 0
bed = 0

print("")
print("                  WARP-PLUS-CLOUDFLARE (script)")
print("")

while True:
	result = run()
	if result == 200:
		good += 1
		os.system('cls' if os.name == 'nt' else 'clear')
		animation = [
			"[■□□□□□□□□□] 10%", "[■■□□□□□□□□] 20%", "[■■■□□□□□□□] 30%", "[■■■■□□□□□□] 40%",
			"[■■■■■□□□□□] 50%", "[■■■■■■□□□□] 60%", "[■■■■■■■□□□] 70%", "[■■■■■■■■□□] 80%",
			"[■■■■■■■■■□] 90%", "[■■■■■■■■■■] 100%"
		]
		for i in range(len(animation)):
			time.sleep(0.5)
			sys.stdout.write("\r[+] Preparing... " + animation[i % len(animation)])
			sys.stdout.flush()
		print(f"\n[-] WORK ON ID: {referrer}")
		print(f"[:)] {good} GB has been successfully added to your account.")
	else:
		b += 1
		os.system('cls' if os.name == 'nt' else 'clear')
		print("[:(] Error when connecting to server.")
		if b > 3000: os._exit()

	print(f"[#] Total: {good} Good {bed} Bad")
	print("[*] After 18 seconds, a new request will be sent.")
	time.sleep(18)
