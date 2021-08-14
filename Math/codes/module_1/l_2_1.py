# -*- coding: utf-8 -*-

org_price = 20
age = 10
discount = 0.0
if age < 10:
    discount = 0.0
if age > 10 and age < 18:
    discount = 0.5
if age > 60:
    discount = 0.0
if age >= 18 and age < 60:
    discount = 1.0
final_price = discount * org_price
