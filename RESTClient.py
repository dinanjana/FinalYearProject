import requests
import json
import logging

def sendPOST(url , data):
    try:
        import http.client as http_client
    except ImportError:
        # Python 2
        import httplib as http_client
    http_client.HTTPConnection.debuglevel = 1

    # You must initialize logging, otherwise you'll not see debug output.
    logging.basicConfig()
    logging.getLogger().setLevel(logging.DEBUG)
    requests_log = logging.getLogger("requests.packages.urllib3")
    requests_log.setLevel(logging.DEBUG)
    requests_log.propagate = True
    headers = {'Content-type': 'application/x-www-form-urlencoded'}
    r=requests.post(url= url,headers= headers,data=data)
    print r.content

def sendGET (url):
    return