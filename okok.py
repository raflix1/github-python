kualitas = str(input("masukkan kualitas jeruk = "))
jumlah = float(input("masukkan jumlah jeruk dalam kg = "))

if (kualitas == "baik") :
    total = 10000 * jumlah
    print("total harha = ", total)
elif (kualitas == "sedang") :
    total = 20000 * jumlah
    print("total harga = ", total)
elif (kualitas == "super"):
    total = 30000 * jumlah
    print("total harga = ", total)