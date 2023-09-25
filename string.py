# -*- coding: utf-8 -*-
"""
Created on Sun Apr 16 00:14:47 2023

@author: Asliddin Abdimuminov
"""

#string yaratish
#ism='Asliddin'
#familya='Abdimuminov'

# fstring yaratish
#ism_familya=f"{ism} {familya}"
#print(ism_familya)

#tab funksiyasi
#print("Hello \tWorld!")
#Enter funksiyasi
#print('Hello \nWorld!')


# STRING METODLAR

#ism='jemis'
#familya='BOND'

#matnni katta harflada yozish
#print(ism.upper())

#matnni kichkina harflada yozish
#print(familya.lower())

#matndagi har bir so`zni boshini katta harflada yozish qolgan harflarni kichkinaga o`tkazadi
#ism_f=ism+' '+familya
#print(ism_f.title())

#matnni faqat birinchi harfni kattada qolganlarini kichkinada yozish
#print(ism_f.capitalize())

# chap, o`ng va ikki tomondagi bo`sh joyni olib tashlash
#meva = "     olma     "
#print("Men " + meva.lstrip() + " yaxshi ko'raman")
#print("Men " + meva.rstrip() + " yaxshi ko'raman")
#print("Men " + meva.strip() + " yaxshi ko'raman")
#print("Men " + meva + " yaxshi ko'raman")

#Tashqaridan ma`lumot kiritish

#ism=input('Ismni kiriting:')
#print('Assalom alaykum,'+ism)

#ismi=input('Ismingiz nima\n>>>')
#print('Assalomu alaykum , '+ismi.title())

#Quyidagi o'zgaruvchilarni yarating: 
kocha="Bog'bon"
mahalla="Sog'bon"
tuman="Bodomzor" 
viloyat="Samarqand"

#Yuqoridagi o'zgaruvchilarni jamlab, quyidagi ko'rinishda konsolga chiqaring:
#Bog'bon ko'chasi, Sog'bon mahallasi, Bodomzor tumani, Samarqand viloyati
#print(f"{kocha} ko`chasi, {mahalla} mahallasi, {tuman} tumani, {viloyat} viloyati.")

#Yuqoridagi o'zgaruvchilarning (kocha, mahalla, tuman, viloyat) qiymatini foydalanuvchidan so'rang. Va avvalgi mashqni takrorlang.
#kocha=input('Ko`changiz\n>>>')
#mahalla=input('Mahallangiz:\n>>>')
#tuman=input('Tumannigiz:\n>>>')
#viloyat=input('Viloyatingiz\n>>>')
#print(f"{kocha} ko`chasi, {mahalla} mahallasi, {tuman} tumani, {viloyat} viloyati.")

#Yuqoridagi matnni konsolga chiqarishda har bir verguldan keyin yangi qatordan yozing
#print(f"{kocha} ko`chasi, \n{mahalla} mahallasi, \n{tuman} tumani, \n{viloyat} viloyati.")

#Yuqoridagi matnni f-string yordamida, yangi, manzil deb nomlangan o'zgaruvchiga yuklang
#manzil=f"{kocha} ko`chasi, \n{mahalla} mahallasi, \n{tuman} tumani, \n{viloyat} viloyati."
#print(manzil)

#manzilga biz yuqorida o'rgangan title(), upper(), lower() , capitalize() metodlarini qo'llab ko'ring.
#print(manzil.title()+"\n")
#print(manzil.upper()+"\n")
#print(manzil.lower()+"\n")
#print(manzil.capitalize())

#Quyidagi o'zgaruvchilarni yarating: 
kocha="Bog'bon"
mahalla="Sog'bon"
tuman="Bodomzor" 
viloyat="Samarqand"

#Yuqoridagi o'zgaruvchilarni jamlab, quyidagi ko'rinishda konsolga chiqaring:
#Bog'bon ko'chasi, Sog'bon mahallasi, Bodomzor tumani, Samarqand viloyati
#print(kocha+" ko'chasi, "+mahalla+" mahallasi, "+tuman+" tumani, ")
#Yuqoridagi o'zgaruvchilarning (kocha, mahalla, tuman, viloyat) qiymatini foydalanuvchidan so'rang. Va avvalgi mashqni takrorlang.
kocha=input('Ko`changiz\n>>>')
mahalla=input('Mahallangiz:\n>>>')
tuman=input('Tumannigiz:\n>>>')
viloyat=input('Viloyatingiz\n>>>')
#Yuqoridagi o'zgaruvchilarni f-string yordamida, yangi, manzil deb nomlangan o'zgaruvchiga yuklang
#Yuqoridagi matnni konsolga chiqarishda har bir verguldan keyin yangi qatordan yozing
manzil=f"{kocha} ko`chasi, \n{mahalla} mahallasi, \n{tuman} tumani, \n{viloyat} viloyati."
print(manzil)

#manzilga biz yuqorida o'rgangan title(), upper(), lower() , capitalize() metodlarini qo'llab ko'ring.
#print(manzil.title()+"\n")
#print(manzil.upper()+"\n")
#print(manzil.lower()+"\n")
#print(manzil.capitalize())