matn = "Xojiakbar mening do`stim"
print(matn)

#index bo`yicha bo`laklash
print(matn[0:9])
print(matn[4:9])
print(matn[:13])
print(matn[11:])
print(matn[-11:-3])
print(matn[-12:-1])
print(len(matn))
print("-------------------")

matn2 = "Mening ismim Asliddin"
print(matn2.upper())
matn3 = "HAMMAGA SALOM PYTHON"

print(matn3.lower())
print("------------------------")

matn3=matn3.replace("PYTHON","java")
print(matn3)

matn4= "Hamma biladi python nimaga qodir emasligini"
matn_list=matn4.split(' ')
print(matn_list)

yoshi = 18
names= "Asliddin"
jumla= "Uning ismi {} yoshi {} da".format(names,yoshi)
print(jumla)
natija= f"Uning yoshi {yoshi}  ismi esa {names}"
print(natija)
print(natija+str(yoshi))
