# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
def gst(org_cost,net_price):
    return(((net_price-org_cost)*100)/org_cost)
  
print("GST Calculator.")
org_cost = float(input("Enter Original Price:"))
net_price = float(input("Enter Net Price:"))
print("GST = ",end='')  
print(round(gst(org_cost, net_price)) ,end='')   
print("%")