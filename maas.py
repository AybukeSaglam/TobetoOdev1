# 2-Maaşı ve zam oranı girilen işçinin zamlı maaşını hesaplayarak ekranda gösteriniz.

maas = int(input("Lütfen maaşınızı giriniz: "))
zam = int(input("Lütfen zam oranını yüzde olarak giriniz: "))

maas = maas + (maas*zam)/100

print("Zamlı maaşınız: " + str(maas))