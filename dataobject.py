class Siswa:
    def __init__(self, nama, kelas):
        self.nama = nama
        self.kelas = kelas

siswa1=Siswa("Adi","X RPL")
siswa2=Siswa("Budi","XI RPL")
siswa=[Siswa("Cici","X KS"),Siswa("Didi","XI MP")]

print(siswa1.nama)
print(siswa1.kelas)
print(siswa2.nama)
print(siswa2.kelas)

for x in siswa:
    print(x.nama," - ", x.kelas)
    #print(x.kelas)

