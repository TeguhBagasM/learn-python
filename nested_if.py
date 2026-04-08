username = input("Masukkan username: ")
password = input("Masukkan password: ")

if username == "admin":
    if password == "123456":
        print("Login berhasil!")
    else:
        print("Login gagal! Password salah.")
else:
    print("Username tidak ditemukan.")