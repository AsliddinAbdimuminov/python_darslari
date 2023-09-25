# -*- coding: utf-8 -*-
"""
Created on Sun Apr 16 17:57:22 2023

@author: aslid
"""

#a=20
#b=5.5
#temp=36.6

#Sonlarning typeni ko`rsatadi
#print(type(a))

#o`qish qulay bo`lish uchun tag chiziqcha bilan ham yozsa bo`ladi
#aholi_soni=7_589_316_414
#print(aholi_soni)

#bir qatorda 3 ta o`zgaruvchini kiritish
#x, y, z = 13, 5.5, 8

#ikkita type ni ko`paytirib float hosil qilinadi
#c=a*b
#print(c)
#d=100/2
#f=100//2

#Dasturda o`zgaruvchi faqat katta harifda kirititsa u constanta qiymat hisoblanadi uni dasturchilar kelishib olingan pythonda
#PI=3.14
#YOSH=24
#print(PI*YOSH)

#integer type dagi ma`lumotni string turiga o`tkazish boxing
#ism='Jahongir'
#yosh=36
#xabar=ism+' '+str(yosh)+' yoshda'
#print(xabar)

#t_yil=int(input('Tug`ulgan yilingizni kiriting: '))
#yosh=2023-t_yil
#print('Siz',yosh,'yoshda ekansiz')


#TOPSHIRIQLAR
#Foydalanuvchi kiritgan sonning kvadrati va kubini konsolga chiqaruvchi dastur
#son=int(input('Istalagan soni kiriting:\n>>>'))
#print(f'{son} ning kvadrati {son**2} ga teng')
#print(f"{son} ning kubi {son**3} ga teng")

#Foydalanuvchining yoshini so'rab, uning tug'ilgan yilini hisoblab, konsolga chiqaruvchi dastur
#yosh=int(input('Yoshingiz nechida?\n>>>'))
#print(f"Siz {2023-yosh} da tug'ilgansiz")

birinchi_son=int(input("Birinchi sonni kiriting:"))
ikkinchi_son=int(input('Ikkinchi sonni kiriting:'))
print(f'{birinchi_son}+{ikkinchi_son}={float(birinchi_son+ikkinchi_son)}')
print(f'{birinchi_son}-{ikkinchi_son}={float(birinchi_son-ikkinchi_son)}')
print(f'{birinchi_son}*{ikkinchi_son}={float(birinchi_son*ikkinchi_son)}')
print(f'{birinchi_son}/{ikkinchi_son}={birinchi_son/ikkinchi_son}')

