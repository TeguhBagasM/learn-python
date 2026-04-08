umur = int(input("Masukkan umur Anda: "))
punya_sim = input("Apakah Anda memiliki SIM? (ya/tidak): ")

if umur >= 17 and punya_sim.lower() == "ya":
    print("Anda memenuhi syarat untuk mengemudi.")
else:
    print("Anda tidak memenuhi syarat untuk mengemudi.")