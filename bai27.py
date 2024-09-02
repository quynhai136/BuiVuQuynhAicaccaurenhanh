# -*- coding: utf-8 -*-
"""
Created on Mon Sep  2 23:12:22 2024

@author: quynh ai
"""

import math
hinh = input("Nhập loại hình (v: hình vuông, n: hình chữ nhật, t: hình tròn): ").lower()
if hinh == 'v':
    canh = float(input("Nhập độ dài cạnh của hình vuông: "))
    dien_tich = canh ** 2
    chu_vi = 4 * canh
    print(f"Hình vuông có diện tích: {dien_tich} và chu vi: {chu_vi}.")
elif hinh == 'n':
    dai = float(input("Nhập chiều dài của hình chữ nhật: "))
    rong = float(input("Nhập chiều rộng của hình chữ nhật: "))
    dien_tich = dai * rong
    chu_vi = 2 * (dai + rong)
    print(f"Hình chữ nhật có diện tích: {dien_tich} và chu vi: {chu_vi}.")
elif hinh == 't':
    ban_kinh = float(input("Nhập bán kính của hình tròn: "))
    dien_tich = math.pi * ban_kinh ** 2
    chu_vi = 2 * math.pi * ban_kinh
    print(f"Hình tròn có diện tích: {dien_tich} và chu vi: {chu_vi}.")
else:
    print("Lựa chọn không hợp lệ. Vui lòng chọn v, n, hoặc t.")
    