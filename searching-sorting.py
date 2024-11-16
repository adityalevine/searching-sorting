import psutil
import timeit

execution_time = timeit.timeit()

process = psutil.Process(psutil.Process().pid)
memory_usage = process.memory_info().rss / 1024 ** 2

# process = psutil.Process(os.getpid())
# memory_usage = process.memory_info().rss / 1024 ** 2

# Fungsi searching (Linear Search)
def search(data, target):
  n = len(data)
  for i in range(n):
    if data[i] == target: 
      return True
  return False


def main():
  # Inisialisasi data
  data = []
  while True:
    # Menampilkan menu pilihan
    print("\nMenu Pilihan:")
    print("1. Input Angka")
    print("2. Sorting")
    print("3. Searching")
    print("4. Exit")

    # Meminta pilihan pengguna
    pilihan = input("Masukkan pilihan: ")
    # Memproses pilihan pengguna
    if pilihan == "1":
      # Input angka
      n = int(input("Masukkan jumlah angka: "))
      for i in range(n):
        angka = int(input("Masukkan angka ke-" + str(i+1) + ": "))
        data.append(angka)
    elif pilihan == "2":
        data.sort()
        print("Data yang sudah diurutkan:", data)
        print(f"Waktu Eksekusi: {execution_time:.6f} seconds")
        print(f"Memory usage: {memory_usage:.2f} kB")
      # ... (implementasi algoritma sorting lainnya)
    elif pilihan == "3":
      # Searching
      target = int(input("Masukkan angka yang dicari: "))
      # Cari angka dalam data
      found = False
      found = search(data, target)
      if found:
        print("Angka", target, "ditemukan")
        print(f"Waktu Eksekusi: {execution_time:.6f} seconds")
        print(f"Memory usage: {memory_usage:.2f} kB")
      else:
        print("Angka", target, "tidak ditemukan")
    elif pilihan == "4":
      # Exit
      break
    elif pilihan == " ":
      return
    else:
      print("Pilihan tidak valid!")
# Memulai program
main()