# 5-Kullanıcıdan alınan bir sayının palindrom olup olmadığını bulan bir program yazınız.

sayi1 = input("Lütfen pozitif bir tam sayı giriniz: ")
sayi2 = sayi1[::-1]
if sayi1 == sayi2  :
    print("Girdiğiniz sayı  bir palindrom sayısıdır.")

else :
     print("Girdiğiniz sayı  bir palindrom sayısı değildir.")
