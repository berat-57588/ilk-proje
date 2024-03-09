print("\033[1;32;40m")
#print("╔"+"═"*20+"╗")

import hesaplamalar.not_hesabi
import hesaplamalar.toplama
import hesaplamalar.cikarma
print("╔═════════════════════╗")
print("║\033[1;31;40m   HESAP MAKİNESİ  \033[1;32;40m  ║")
print("║                     ║")
print("║  1-Toplama          ║")
print("║  2-Çıkarma          ║")
print("║  3-Not hesabı       ║")
print("║  4-                 ║")
print("║  5-                 ║")
print("║  6-                 ║")
print("║  7-                 ║")
print("║  8-                 ║")
print("║  9-                 ║")
print("║    Seçimiz nedir?   ║")
print("╚═════════════════════╝")
# 201 ╔ # 205 ═ # 187 ╗ # 186 ║ # 200 ╚ # 188 ╝
seçim = input ("Bir rakam girin: ")
if seçim == "1":
   print("\nToplamayı seçtiniz!\n")
   hesaplamalar.toplama.toplayici()
elif seçim == "2":
    print("\nÇıkarmayı seçtiniz!\n")
    hesaplamalar.cikarma.cikarici()
elif seçim == "3":
    print("\nNot hesaplamayı seçtiniz!\n")
    hesaplamalar.not_hesabi.harfnotu()
else:
    print("lütfen geçerli bir rakam giriniz.")