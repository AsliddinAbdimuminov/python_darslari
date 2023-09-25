# -*- coding: utf-8 -*-
"""
Created on Sun Sep 24 19:46:20 2023

@author: aslid
"""

# kun =input('Bugungi kunni kiriting"\n>>>')
# if kun.lower()=='shanba' or kun.lower()=='yakshanba':
#     print('Bugun dam olish kuni')
# else: print(f'{kun} ish kuni')

# kun =input('Bugungi kunni kiriting"\n>>>')
# havo=input('Havo haroratini yozing: ')
# if kun.lower()=='yakshanba' and havo>=30:
#     print('Cho`milishga kettik')
# elif kun.lower()=='yakshanba' and havo<30:
#     print('Uyda dam olamiz!!')

# narh=1500
# choy= True
# salat=False
# if choy and salat:
#     narh=narh+10000
# elif choy or salat:
#     narh=narh+5000
# print(f'Jami narh {narh} so`m')

# Asliddin = ['ali', 'sali', 'qani']
# 'ali' in Asliddin

# menu = ['osh', 'manti', 'salat']
# buyurtma= input('Nima ovqat buyurtma berasiz: ')
# if buyurtma.lower() in menu:
#     print("Buyurtma qabul qilindi!!!")
# else: print('Bu ovqat menuda yo`q')


# # to`plamda shu yo`mi

# if 'shurva' not in menu:
#     print('Kechirasiz, u ham yuq')
# else: print('menuda bor')

# buyur= []
# if  buyur:
#     print('bush emas')
# else: print('Bo`sh')

# ss=int(input('Iltimos juft sonini kiriting: '))
# if ss%2==0: print('Rahmat')
# else: print('Bu juft soni emas')

# x=int(input('Iltimos yoshingizni kiriting: '))
# if x<4 or x>60: print('Sizga belit bepul')
# elif x<18: print(10000,'so`m')
# else: print(20000,'so`m')

# print('Iltimos ikkita son kiriting:')
# x,y=float(input('Birinchi sonni kiriting: ')),float(input('Ikkinchi sonni kiriting: '))
# if x==y:print(x,'=',y)
# elif x>y:print(x,'>',y)
# else: print(x,'<',y)

# mahsulotlar=['sabzi', 'guruch','piyoz','apelsin','mandarin','limon','go`sht','ko`kat','nok','olma']
# salat=[]
# print('5 ta salatga mahsulotlarni kiriting:')
# for n in range(5):
#     salat.append(input(f'{n+1}: '))
# for f in salat:
#     if f in mahsulotlar:
#         print(f'Do`konimizda {f} bor')
#     else: print(f'Do`konimizda {f} yo`q')

# mahsulotlar=['sabzi', 'guruch','piyoz','apelsin','mandarin','limon','go`sht','ko`kat','nok','olma']
# salat=[]
# print('5 ta salatga mahsulotlarni kiriting:')
# for n in range(5):
#     salat.append(input(f'{n+1}: '))
# print('Do`konimizda siz so`ragan quidagi mahsulotlar yo`q:')
# for f in salat:
#     if f not in mahsulotlar:
#         print(f)

# foydalanuvchilar=['Asliddin', 'O`ktam','Barno','Yulduz','Zebo']
# x=input('Yangi login tanlang:')
# if x not in foydalanuvchilar:
#     print('Xush kelibsiz')
# else: print('Login band, yangi login tanlanag!!')

son = int(input('Istalgan butun son kiriting: '))
# for w in range(2,10):
#     if son%w==0:
#         print(f"{son} soni {w} qoldig`siz bo`linadi")
# for w in range(2,10):
#     if not son%w:
#         print(f"{son} soni {w} qoldig`siz bo`linadi")