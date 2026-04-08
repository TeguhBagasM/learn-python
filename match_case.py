hari = input("Masukkan hari: ").lower()

match hari:
    case "senin" | "selasa" | "rabu" | "kamis" | "jumat":
        print("hari kerja") 
    case "sabtu" | "minggu":
        print("hari libur")
    case _:
        print("hari tidak valid")