# Membuat array (list) buah-buahan
buah = ["Apel", "Mangga", "Jeruk", "Pisang", "Anggur"]

print("=" * 40)
print("        PROGRAM ARRAY PYTHON")
print("=" * 40)

# Menampilkan seluruh array
print("\n📋 Data Array Buah:")
print(buah)

# Mengakses elemen berdasarkan index
print("\n🔍 Akses Elemen:")
print(f"Index ke-0 : {buah[0]}")
print(f"Index ke-2 : {buah[2]}")
print(f"Index ke-4 : {buah[4]}")

# Menambah elemen
buah.append("Semangka")
print(f"\n➕ Setelah append 'Semangka': {buah}")

# Menyisipkan elemen di posisi tertentu
buah.insert(2, "Melon")
print(f"➕ Setelah insert 'Melon' di index 2: {buah}")

# Menghapus elemen
buah.remove("Jeruk")
print(f"➖ Setelah remove 'Jeruk': {buah}")

# Menghapus berdasarkan index
buah.pop(0)
print(f"➖ Setelah pop index 0: {buah}")

# Panjang array
print(f"\n📏 Panjang array: {len(buah)}")

# Mengurutkan array
buah.sort()
print(f"🔤 Setelah diurutkan: {buah}")

# Membalik urutan
buah.reverse()
print(f"🔄 Setelah dibalik: {buah}")

# Looping array
print("\n🔁 Menampilkan dengan looping:")
for i, item in enumerate(buah):
    print(f"  Index {i}: {item}")

print("\n" + "=" * 40)
print("        PROGRAM SELESAI")
print("=" * 40)