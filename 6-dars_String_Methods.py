matn = "men Mohirfestda ishtirok etayapma"
print(matn.title())

print(matn.capitalize())

print(matn.swapcase())

#suz necha marta qatnashganini chiqaradi
print(matn.count("men"))

# boshlovchi indexini aniqlash
print(matn.find("ishtirok"))

print(matn.index("eta")) #yuq bo`lsa eror bo`ladi

txt= "dhsdhwd654"
print(txt.isalnum()) #ichida raqam yoki harflardan borligini aniqlaydi
txt2="2345"
print(txt2.isalpha())
print(txt2.isdigit())

#stringni qo`shish uchun ishlatiladi
g=["olma","anor","nok"]
h=" va ".join(g)
print(h)

rrr="salom hammaha ha"
print(rrr.startswith("sa"))
print(rrr.endswith("fa"))

#nol bilan to`ldirish
numer3="9"
z=numer3.zfill(5)
print(z)