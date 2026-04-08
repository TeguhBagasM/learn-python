# angka = int(input("Masukkan sebuah angka: "))

# if angka > 0:
#     print("Angka yang Anda masukkan adalah positif.")
#     if angka < 0:
#         print("Angka yang Anda masukkan adalah negatif.")
#         if angka == 0:
#             print("Angka yang Anda masukkan adalah nol.")

# nilai = int(input("Masukkan nilai anda: "))

# if nilai >= 70:
#     print("Selamat, Anda lulus!")
# else:
#     print("Maaf, Anda tidak lulus.")

nilai = int(input("Masukkan nilai anda: "))
if nilai >= 90:
    print("Nilai Anda adalah A.")
elif nilai >= 80:
    print("Nilai Anda adalah B.")
elif nilai >= 70:
    print("Nilai Anda adalah C.")
elif nilai >= 60:
    print("Nilai Anda adalah D.")
else:
    print("Nilai Anda adalah E.")