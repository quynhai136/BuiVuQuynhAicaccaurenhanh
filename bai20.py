# -*- coding: utf-8 -*-
"""
Created on Mon Sep  2 01:36:50 2024

@author: quynh ai
"""

a = float(input("Nhập số nguyên a: "))
b = float(input("Nhập số nguyên b: "))
c = float(input("Nhập số nguyên c: "))
lon_nhat = a 
if b > lon_nhat:
    lon_nhat = b
if c > lon_nhat:
    lon_nhat = c
print("Số lớn nhất là:", lon_nhat)
