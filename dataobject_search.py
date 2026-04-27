class Siswa:
    def __init__(self, nama, kelas):
        self.nama = nama
        self.kelas = kelas

siswa=[Siswa("Adi","X"),
       Siswa("Budi","XI"),
       Siswa("Cici","XI"),
       Siswa("Didi","X"),
       Siswa("Fifi","X")]

ketemu=0
cari=input("Nama siswa dicari: ")
for x in siswa:
    if x.nama==cari:
        print(x.nama)
        ketemu=1
        break
if not ketemu:
    print("Data tidak ditemukan")