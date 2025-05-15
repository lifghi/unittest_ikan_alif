# main.py
from usecases.fish_usecase import FishUseCase
from infrastructure.in_memory_fish_repo import InMemoryFishRepository

def main():
    repo = InMemoryFishRepository()
    usecase = FishUseCase(repo)

    while True:
        print("\nMenu:")
        print("1. Tambah Ikan Baru")
        print("2. Liat Ikan Berdasarkan Id")
        print("3. Cari Ikan")
        print("4. Edit Ikan")
        print("5. Hapus Ikan")
        print("6. Keluar")
        
        choice = input("Pilih nomor ikan (1-6): ")
        
        if choice == "3":
            fishes = usecase.browse_fishes()
            if not fishes:
                print("Belum ada ikan.")
            else:
                print("Daftar Ikan:")
                for idx, f in enumerate(fishes):
                    print(f"[{idx}] Nama: {f.name}, Jenis: {f.jenis}, Perairan: {f.perairan}")
        
        elif choice == "2":
            try:
                index = int(input("Masukan Id Ikan: "))
                fish = usecase.read_fish(index)
                if fish:
                    print(f"Ikan Berdasarkan Id {index}:")
                    print(f"  Nama     : {fish.name}")
                    print(f"  Jenis    : {fish.jenis}")
                    print(f"  Perairan : {fish.perairan}")
                else:
                    print("Gada Ikannya.")
            except ValueError:
                print("Salah input. Masukan id ikan yang benar")
        
        elif choice == "1":
            name = input("Masukan nama ikan yang ingin ditambah: ")
            jenis = input("Masukan jenis ikan: ")
            perairan = input("Masukan perairan ikan: ")
            if usecase.add_fish(name, jenis, perairan):
                print(f"Ikan '{name}' Berhasil ditambah.")
            else:
                print(f"Ikan '{name}' Sudah ada.")
        
        elif choice == "4":
            try:
                index = int(input("Masukin Id ikannya buat ngedit info: "))
                new_name = input("Masukin nama ikan barunya: ")
                new_jenis = input("Masukin jenis ikan barunya: ")
                new_perairan = input("Masukin perairan ikan barunya: ")
                if usecase.edit_fish(index, new_name, new_jenis, new_perairan):
                    print(f"Ikan dari Id {index} di update ke '{new_name}'.")
                else:
                    print("Gagal mengupdate. Id nya salah mungkin.")
            except ValueError:
                print("Gabisa. Tolong masukin Id yang bener.")
        
        elif choice == "5":
            try:
                index = int(input("Masukin Id ikan yang mau dihapus: "))
                if usecase.delete_fish(index):
                    print(f"Ikan dari Id {index} sudah dihapus.")
                else:
                    print("Gagal hapus ikan. Id nya salah mungkin.")
            except ValueError:
                print("Gabisa. Tolong masukin Id yang bener.")
        
        elif choice == "6":
            print("Dadah!")
            break
        
        else:
            print("Gaada pilihannya, masukin yang bener.")

if __name__ == "__main__":
    main()
