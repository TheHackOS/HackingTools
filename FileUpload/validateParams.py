#!/usr/bin/python3

import argparse
import validators
import socket
import re
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

            response = requests.get(domain, timeout=5)
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