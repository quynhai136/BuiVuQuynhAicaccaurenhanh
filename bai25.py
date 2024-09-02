# -*- coding: utf-8 -*-
"""
Created on Mon Sep  2 22:53:32 2024

@author: quynh ai
"""

chu_cai = input("Nhập một chữ cái: ")
if chu_cai.islower():
    chu_cai = chu_cai.upper()
else:
    chu_cai = chu_cai.lower()
print("Kết quả là:", chu_cai)
