# -*- coding: utf-8 -*-
"""
Created on Mon Apr 17 00:56:46 2023

@author: aslid
"""

# list (ro`yxat)
mevalar=['olma','anjir','shaftoli',"o'rik"]
narhlar=[12000,18000,22000,25000,36000,-25,63.2]
sonlar=['bir','ikki',3,4,5]
ismlar=[]

#print("Birinchi meva",mevalar[0])
#print('Ikkinchi meva',mevalar[1])

#print(mevalar[2].title())
#print(mevalar[3].upper())

#print(narhlar[1]+narhlar[3])
#print(float(narhlar[2]+narhlar[0]))

#elementlarni o`zgartirish
mevalar[0]='anor'
mevalar[-1]="uzum"

#ma`lumot qo`shish  .append
mevalar.append('tarvuz')
#print(mevalar)

#  .insert   index bo`yicha qo`shish
mevalar.insert(0, 'o`rik')
mevalar.insert(-1, 'xurmo')
#print(mevalar)

cars=[]
cars.append('Malibu')
cars.append('Coblt')
cars.insert(0, 'Tiko')
cars.append('Damas')
cars.append('Taho')


#elementlarni o`chirish
del cars[0]
cars.remove('Malibu')


cars.append('Malibu')
cars.append("Tiko")
cars.append('Lada')

#Biror bir elementni sug`irib olish
bozorlik=['un','yog`','kartoshka','piyoz','sabzi','guruch']

mahsulot=bozorlik.pop(0)
mahsulot=bozorlik.pop()

