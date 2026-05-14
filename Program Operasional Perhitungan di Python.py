# ============================================
#    PROGRAM OPERASIONAL PERHITUNGAN
# ============================================

print("=" * 40)
print("   KALKULATOR OPERASIONAL PERHITUNGAN")
print("=" * 40)

# Input angka dari user
a = float(input("\nMasukkan angka pertama  : "))
b = float(input("Masukkan angka kedua    : "))

print("\n" + "-" * 40)
print("         HASIL PERHITUNGAN")
print("-" * 40)

# Operasi Dasar
print(f"\n➕ Penjumlahan      : {a} + {b} = {a + b}")
print(f"➖ Pengurangan      : {a} - {b} = {a - b}")
print(f"✖️  Perkalian        : {a} x {b} = {a * b}")

# Pembagian (cek pembagi tidak nol)
if b != 0:
    print(f"➗ Pembagian        : {a} / {b} = {a / b:.2f}")
    print(f"📐 Pembagian Bulat  : {a} // {b} = {a // b}")
    print(f"🔢 Sisa Bagi (Mod)  : {a} % {b} = {a % b}")
else:
    print("➗ Pembagian        : Tidak bisa dibagi dengan 0!")

# Operasi Pangkat
print(f"🔺 Perpangkatan     : {a} ** {b} = {a ** b}")

# Operasi Perbandingan
print("\n" + "-" * 40)
print("       OPERASI PERBANDINGAN")
print("-" * 40)
print(f"  {a} > {b}  : {a > b}")
print(f"  {a} < {b}  : {a < b}")
print(f"  {a} >= {b} : {a >= b}")
print(f"  {a} <= {b} : {a <= b}")
print(f"  {a} == {b} : {a == b}")
print(f"  {a} != {b} : {a != b}")

print("\n" + "=" * 40)
print("        PROGRAM SELESAI")
print("=" * 40)