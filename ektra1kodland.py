import random
from colorama import Fore, Style
import sys
while True:
    print(Fore.LIGHTBLUE_EX + "'2*win with *isim yok*' mekanına hoşgeldiniz!")
    isimce = input("ismin???"+Style.BRIGHT + Fore.YELLOW)
    if len(isimce) < 3:
        print(Fore.RED+"isminiz çok kısa, lütfen daha uzun bir isim giriniz.")
        isimce = input(Fore.RED+"ismin???")
    if len(isimce) > 10:
        isimce = isimce[:10] + "..."
    any_strings_of_list = ["Mr.Ates","Atesbey","**++py++**",isimce]
    xrt = random.choice(any_strings_of_list)
    print(Style.BRIGHT + Fore.LIGHTYELLOW_EX + xrt, Style.BRIGHT + Fore.LIGHTGREEN_EX +"çıktı kazandın" if xrt == isimce else Style.BRIGHT + Fore.MAGENTA + "çıktı kaybettin" + Style.RESET_ALL)
    if input(Fore.CYAN + "Tekrar oynamak ister misin? (E/H)").upper() != "E":
        print(Fore.CYAN + "Oyun bitti, teşekkürler!")
        sys.exit()