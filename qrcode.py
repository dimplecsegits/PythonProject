# -*- coding: utf-8 -*-
"""
Created on Thu May 16 22:51:28 2024

@author: Dimple Upadhyay
"""
import pyqrcode
from pyqrcode import QRCode
s="my name is dimple upadhyay"
url=pyqrcode.create(s)
url.svg("mydetails.svg",scale=8)
