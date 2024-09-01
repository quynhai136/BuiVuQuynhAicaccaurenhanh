# -*- coding: utf-8 -*-
"""
Created on Mon Sep  2 01:42:21 2024

@author: quynh ai
"""

# Nhập các hệ số a và b
a = float(input("Nhập hệ số a: "))
b = float(input("Nhập hệ số b: "))

# Giải và biện luận phương trình bậc nhất
if a == 0:
    if b == 0:
        print("Phương trình có vô số nghiệm.")
    else:
        print("Phương trình vô nghiệm.")
else:
    x = -b / a
    print(f"Phương trình có nghiệm x = {x}.")
