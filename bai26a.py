# -*- coding: utf-8 -*-
"""
Created on Mon Sep  2 22:53:53 2024

@author: quynh ai
"""

a = float(input("Nhập số a: "))
b = float(input("Nhập số b: "))
c = float(input("Nhập số c: "))

# Sắp xếp các số theo thứ tự tăng dần
if a > b:
    a, b = b, a  # Hoán đổi giá trị a và b
if a > c:
    a, c = c, a  # Hoán đổi giá trị a và c
if b > c:
    b, c = c, b  # Hoán đổi giá trị b và c
# In kết quả ra màn hình
print("Thứ tự tăng dần:", a, b, c)












