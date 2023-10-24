# 4-Dairenin alanını ve çevresini hesaplayan python kodunu yazınız.(Dairenin yarıçapını kullanıcıdan alınız)

yariCap = float(input("Lütfen dairenin yarıçapını metre cnsinden giriniz: "))

pi = 3.14

daireCevre = 2*pi*yariCap

print("Dairenin çevresi: " + str(daireCevre))

daireAlan = pi*yariCap**2

print("Dairenin alanı: " + str(daireAlan))

