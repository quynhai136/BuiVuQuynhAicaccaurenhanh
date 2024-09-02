# -*- coding: utf-8 -*-
"""
Created on Mon Sep  2 22:47:14 2024

@author: quynh ai
"""

gio = float(input("Nhập giờ: "))
phut = float(input("Nhập phút: "))
giay = float(input("Nhập giây: "))
if 0 <= gio < 24 and 0 <= phut < 60 and 0 <= giay < 60:
    print("Giờ, phút, giây hợp lệ.")
else:
    print("Giờ, phút, giây không hợp lệ.")
    