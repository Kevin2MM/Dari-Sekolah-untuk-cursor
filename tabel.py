import os
import sys
import csv

class Siswa:
    def __init__(self, id, nama, nilai1, nilai2, nilai3):
        self.id = id
        self.nama = nama
        self.nilai1 = nilai1
        self.nilai2 = nilai2
        self.nilai3 = nilai3

def getData():
    global siswa
    #read data from file & transfer to object array
    with open('data.csv', mode='r') as file:
        reader = csv.reader(file)
        for row in reader:
            siswa.append(Siswa(row[0],row[1],row[2],row[3],row[4]))

def cariSiswa(id):
    global siswa
    ketemu = False
    for i, data in enumerate(siswa):
        if data.id == id:
            ketemu = True
            break

    return ketemu, i
            
def clear():
    # Use 'cls' for Windows (os.name is 'nt') and 'clear' for Linux/macOS
    os.system('cls' if os.name == 'nt' else 'clear')

def moveTo(x,y):
    # \033[ is the escape initiator; H moves to the absolute position
    sys.stdout.write(f"\033[{y};{x}H")
    sys.stdout.flush()
    
def hitungRata(n1,n2,n3):
    rata=(n1+n2+n3)/3
    return rata

def changeRow():
    global row
    row+=1

def lines():
    print("============================================================")
    
#clear the screen
clear()
#create new siswa as array
siswa=[]
pos = 0
#read data from
getData()
#initialize parameters
row=1
col=[0, 5, 20, 30, 40, 50]

#print header
moveTo(0,row)
lines()
changeRow()
moveTo(col[0],row)
print("No")
moveTo(col[1],row)
print("Nama")
moveTo(col[2],row)
print("Nilai 1")
moveTo(col[3],row)
print("Nilai 2")
moveTo(col[4],row)
print("Nilai 3")
moveTo(col[5],row)
print("Rata-rata")
changeRow()
moveTo(0,row)
lines()
changeRow()


#input table content
while True:

    moveTo(col[0],row)
    id = input()

    if id == '':
        break

    ketemu, pos = cariSiswa(id)
    if ketemu:
        moveTo(col[0], row)
        print(siswa[pos].id)
        moveTo(col[1],row)
        print(siswa[pos].nama)
        moveTo(col[2],row)
        print(siswa[pos].nilai1)
        moveTo(col[3],row)
        print(siswa[pos].nilai2)
        moveTo(col[4],row)
        print(siswa[pos].nilai3)
        moveTo(col[5],row)
        print(f"{hitungRata(int(siswa[pos].nilai1),int(siswa[pos].nilai2),int(siswa[pos].nilai3)):.1f}")
            
        
    else:
        moveTo(col[0], row)
        print('Data Tidak ditemukan.Tekan Enter....')
        input()
        moveTo(col[0], row)
        print('                                                   ')
        continue
          
    changeRow()
  
#print closing lines
moveTo(col[0],row)
lines()