import random
from colorama import Fore, Style
import sys
while True:
    print("'2*win with *isim yok*' mekanına hoşgeldiniz!")
    isimce = input("ismin???")
    if len(isimce) < 3:
        print(Fore.RED+"isminiz çok kısa, lütfen daha uzun bir isim giriniz.")
        isimce = input("ismin???")
    if len(isimce) > 10:
        isimce = isimce[:10] + "..."
    any_strings_of_list = ["Mr.Ates","Atesbey","**++py++**",isimce]
    xrt = random.choice(any_strings_of_list)
    print(xrt, Style.BRIGHT + Fore.LIGHTGREEN_EX +"çıktı kazandın" if xrt == isimce else Style.BRIGHT + Fore.MAGENTA + "çıktı kaybettin" + Style.RESET_ALL)
    if input("Tekrar oynamak ister misin? (E/H)").upper() != "E":
        print("Oyun bitti, teşekkürler!")
        sys.exit()