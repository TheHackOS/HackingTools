#!/usr/bin/python3

import argparse
import socket
import sys
import os
import requests
from requests.exceptions import ConnectionError

class ValidateUrl(argparse.Action):

    def __init__(self, option_strings=None, dest=None, nargs=None, **kwargs):
        if nargs is not None:
            raise ValueError("nargs not allowed")
        super().__init__(option_strings, dest, **kwargs)

    def __call__(self, parser, namespace, values, option_string=None):
        values = self.validate_existence(values)
        setattr(namespace, self.dest, values)

    def validate_existence(self,domain):
        try:
            if 'http' not in domain:
                domain = f'http://{domain}'

            response = requests.get(domain, timeout=1)
        except ConnectionError:
            return False
        else:
            return response.url

    def check_dns(self,domain):
        try:
            socket.gethostbyname(domain)
            return True
        except socket.gaierror:
            return False

def check_file(filename):
    if not os.path.exists(filename) or os.path.getsize(filename) == 0:
        return False
    lines = []
    with open(filename, "r") as f:
        for line in f:
            lines.append(line.strip())
    return lines

 
class ValidateFile(argparse.Action):
    def __call__(self, parser, namespace, values, option_string=None):
        
        if not values:
            raise argparse.ArgumentError(self, f"Error: '-chk' argument is required.")

        file_extension = check_file(values)
            
        if not file_extension:
            raise parser.error('[!] Error: not exists or empty file')

        setattr(namespace, self.dest, file_extension)
