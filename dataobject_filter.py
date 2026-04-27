class Siswa:
    def __init__(self, nama, kelas):
        self.nama = nama
        self.kelas = kelas

siswa=[Siswa("Adi","X"),Siswa("Budi","XI"),Siswa("Cici","XI"),Siswa("Didi","X"),Siswa("Fifi","X")]

for x in siswa:
    if x.kelas=="X":
        print(x.nama)
