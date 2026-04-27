import sys
import os
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
siswa = []
getData()

while True:
    moveTo(col[0],row)
    kode = input()
    if kode == '':
        break
    
    ditemukan = False
    for data in siswa:
        if kode == data.id:
            ditemukan = True
             
            moveTo(col[1],row)
            print(data.nama)  
            
            moveTo(col[2],row)
            print(data.nilai1)
            
            moveTo(col[3],row)
            print(data.nilai2)
            
            moveTo(col[4],row)
            print(data.nilai3)
            
            moveTo(col[5],row)
            print(f"{hitungRata(int(data.nilai1), int(data.nilai2), int(data.nilai3)):.1f}")
            break
        
        
    if not ditemukan:
        moveTo(col[0], row)
        print('    ')
        moveTo(col[0], row)
        continue
        
    changeRow()
    

#print closing lines
moveTo(col[0],row)
lines()

