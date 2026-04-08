Data = [1, 12, 3, 9, 4, 5, 8]

# mengakses list
Subdata = Data[:-1]
Subdata2 = Data[-1]

# print(Subdata)
# print(Subdata2)

# memotong list
Subdata3 = Data[2:5]
Subdata4 = Data[:4]

# menambah list
Data2 = [100, 200, 300, 400, 500, 600, 700, 800]

# menambah list
menambah_list = Data + Data2

# merubah list
# print("Data sebelum diubah:", Data)
Data[0] = 10
# print("Data setelah diubah:", Data)

# mencopy list ke variable baru
a = Data[:]
a[0] = 12
# print("Data asli:", Data)

# merubah list dengan method slicing
Data[1:4] = [20, 30, 40]
# print("Data setelah diubah dengan slicing:", Data)
# list di dalam list
Data3 = [Data, Data2]
# print("Data3:", Data3)

# mengakses list di dalam list
y = Data3[1][3]
# print("Data ke-3 dari Data2:", y)
# print(Data3)

# methods untuk list
Data.append(90)
print("Data setelah append:", Data)

# function untuk list
panjang_data = len(Data)

print(Data)
print("Panjang Data:", panjang_data)