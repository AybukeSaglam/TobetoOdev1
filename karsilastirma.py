# 3-Kullanıcının girdiği üç sayı arasında en büyük olanı bulan ve sonucu yazdıran bir program yazınız.

sayi1 = int(input("lütfen 1. sayıyı giriniz: "))
sayi2 = int(input("lütfen 2. sayıyı giriniz: "))
sayi3 = int(input("lütfen 3. sayıyı giriniz: "))


if sayi1 > sayi2 :
    if sayi1 > sayi3 :
        print("1. sayı en büyüktür.")
    
elif sayi2 > sayi3 :
    print("2. sayı en büyüktür.") 

elif sayi3 > sayi2 :
    print ("3. sayı en büyüktür.")

else:
    print("Lütfen birbirinden farklı sayılar giriniz.")

