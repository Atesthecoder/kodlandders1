import random
print("'2*win with *isim yok*' mekanına hoşgeldiniz!")
isimce = input("ismin???")
if len(isimce) < 3:
    print("isminiz çok kısa, lütfen daha uzun bir isim giriniz.")
    isimce = input("ismin???")
if len(isimce) > 10:
    isimce = isimce[:10] + "..."
any_strings_of_list = ["Mr.Ates","Atesbey","**++py++**",isimce]
xrt = random.choice(any_strings_of_list)
print(xrt, "çıktı kazandın" if xrt == isimce else "çıktı kaybettin" )