# avtomillar=["bmw", 'shevralet', 'lasette', 'lamgine','iszu']
# for avto in avtomillar:
#     if avto == 'bmw':
#         print(avto.upper())
#     else:
#         print(avto.title())

# ism=input("Ismingizni kiriting?\n>>>")
# if ism.title()!="Ali":
#     print(f"Uzur {ism.title()}, biz Alini kutayapmiz")
# else:
#     print("Salom Ali")

# javob= float(input("12*6 nechiga teng\n>>>"))
# if javob!=72:
#     print("Noto`g`ri!!!")

# yosh=int(input("Yoshingiz nechida?\n>>>"))
# if yosh>=18:
#     print('Xush kelibsiz!!')
# else:
#     print("Sizga kirishga mumkin emas!!!")

# login=input("Yangi login kiriting:\n>>>")
# if len(login)<=5:
#     print("Loginda belgilar soni 5 tadan ko`p bo`lishi kerak")


# yil=int(input("Tug'ulgan kuningizni kiriting\n>>>"))
# if 2023-yil<18:
#     print(f"Yoshingiz {2023-yil} da ekan\n Kirish mumkin emas!")
# else:
#     print("Hush kelibsiz")

# x,y=50,60
# print("x>y") if x>y else print("x<y")
    
# cars = ['toyota', 'mazda', 'hyundai', 'gm', 'kia']
# for a in cars:
#     print(a.title()) if a.upper()!="GM" else print(a.upper())
    
# ism=input("Logingizni kiriting: ")
# print(f"Xush kelibsiz, {ism.upper()}") if ism.title=='Admin' else print(f"Xush kelibsiz, {ism}!")


# x,y=map(int,input("Ikkita son kiriting bir qatorda: ").split())
# if x==y: print("Sonlar teng")

# x=int(input("Istalgan soningizni kiriting: "))
# print("Manfiy son") if x<0 else print("Musbat son")
x=int(input("Istalgan soningizni kiriting: "))
print("Musbat son kiriting") if x<0 else print(x**(1/2))