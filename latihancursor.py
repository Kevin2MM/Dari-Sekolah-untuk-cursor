import sys
import os
import csv

class Siswa:
    def __init__(self, id, nama, kelas, nilai1, nilai2, nilai3):
        self.id = id
        self.nama = nama
        self.kelas = kelas
        self.nilai1 = nilai1
        self.nilai2 = nilai2
        self.nilai3 = nilai3

def clear():
    # Use 'cls' for Windows (os.name is 'nt') and 'clear' for Linux/macOS
    os.system('cls' if os.name == 'nt' else 'clear')

def getData():
    global siswa
    #read data from file & transfer to object array
    with open('data2.csv', mode='r') as file:
        reader = csv.reader(file)
        for row in reader:
            siswa.append(Siswa(row[0],row[1],row[2],float(row[3]),float(row[4]),float(row[5])))



def cariSiswa(id):
  
    global siswa
    ketemu = False
    for i, data in enumerate(siswa):
        if data.id == id:
           
            ketemu = True
            break

    return ketemu, i

            
def moveTo(x,y):
    # \033[ is the escape initiator; H moves to the absolute position
    sys.stdout.write(f"\033[{y};{x}H")
    sys.stdout.flush()
    
def hitungRata(n1,n2,n3):
    rata=(n1+n2+n3)/3
    return rata

def changeRow():
    global row
    row += 1

def lines():
    print("============================================================")
    

#create new siswa as array
siswa=[]
pos = 0
#read data from
getData()    
#clear the screen
clear()
#initialize parameters
row=1
col=[0, 5, 20, 30, 40, 50]
# Print Tabel
moveTo(0,row)
lines()
changeRow()

#Tabel NIS, Nama, Kelas
moveTo(col[0],row)
print("Nilai Tes Kemampuan Akademik")
changeRow()
lines()
changeRow()

moveTo(col[0],row)
startRow = row
print("NIS")


changeRow()
moveTo(col[0],row)
print("Nama")
changeRow()

moveTo(col[0],row)
print("Kelas")

changeRow()
lines()
changeRow()

# Tabel No, Mapel, Nilai
moveTo(col[0],row)
print("NO")
moveTo(col[1],row)
print("Mapel")
moveTo(col[4],row)
print('Nilai')

changeRow()
moveTo(0,row)
lines()
changeRow()

moveTo(col[0],row)
print('1')
moveTo(col[1],row)
print('Bahasa indonesia')
changeRow()
moveTo(col[0],row)
print('2')
moveTo(col[1],row)
print('Bahasa inggris')
changeRow()
moveTo(col[0],row)
print('3')
moveTo(col[1],row)
print('Matematika')

changeRow()
lines()
changeRow()

# Tabel Menampilkan Rata dan Nilai Akhir
rataRow = row
moveTo(col[1],row)
print('Rata: ')
changeRow()
akhirRow = row
moveTo(col[1], row)
print('Nilai Akhir: ')
changeRow()
lines()

#input table content
while True:

    moveTo(col[2], startRow)
    id = input()
    ketemu, pos = cariSiswa(id)
    if id == '':
        break

    if ketemu:
        moveTo(col[2], startRow + 1)
        print(siswa[pos].nama)
        moveTo(col[2], startRow + 2)
        print(siswa[pos].kelas)
        moveTo(col[4], startRow + 6)
        print(siswa[pos].nilai1)
        moveTo(col[4], startRow + 7)
        print(siswa[pos].nilai2)
        moveTo(col[4], startRow + 8)
        print(siswa[pos].nilai3)
        rata = hitungRata(siswa[pos].nilai1, siswa[pos].nilai2, siswa[pos].nilai3)
        moveTo(col[4], rataRow)
        print(f'{rata:.1f}')
        moveTo(col[4], akhirRow)
        if rata >= 90:
            print('A')
        elif rata >= 75:
            print('B')
        elif rata >= 65:
            print('C')
        elif rata >= 50:
            print('D')
        elif rata <= 49:
            print('E')
        else:
            print('Nilai Tidak Valid')
        break
            
        
    else:
        moveTo(col[2], startRow)
        input('Data Tidak Ditemukan.Tekan Enter...')
        moveTo(col[2], startRow)
        print('                                                   ')
        continue
          
    changeRow()
  
#print closing lines
moveTo(col[0],row)
lines()
