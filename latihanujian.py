import sys
import os
import csv

class Pegawai:
    def __init__(self, id, nama_depan, nama_belakang, golongan, gajiPokok):
        self.id = id
        self.nama_depan = nama_depan
        self.nama_belakang = nama_belakang
        self.golongan = golongan
        self.gajiPokok = gajiPokok

def clear():
    # Use 'cls' for Windows (os.name is 'nt') and 'clear' for Linux/macOS
    os.system('cls' if os.name == 'nt' else 'clear')

def getData():
    pegawai = []
    #read data from file & transfer to object array
    with open('pegawai.csv', mode='r') as file:
        reader = csv.reader(file)
        for row in reader:
            pegawai.append(Pegawai(row[0],row[1],row[2],row[3],int(row[4])))
    return pegawai
def cariPegawai(nama_belakang):
  
    global pegawai
    ketemu = False
    for i, data in enumerate(pegawai):
        if data.nama_belakang == nama_belakang:
           
            ketemu = True
            break

    return ketemu, i

            
def moveTo(x,y):
    # \033[ is the escape initiator; H moves to the absolute position
    sys.stdout.write(f"\033[{y};{x}H")
    sys.stdout.flush()
    

def changeRow():
    global row
    row += 1

def lines():
    print("============================================================")

def hitungGaji(gajiPokok, tunjangan, iuran):
    return gajiPokok + tunjangan - iuran

#create new siswa as array
pegawai = getData()
pos = 0
#read data from
  
#clear the screen
clear()
#initialize parameters
row=1
col=[0, 5, 20, 30, 40, 50]
# Print Tabel
moveTo(0,row)
lines()
changeRow()


lanjut = 'y'
while lanjut == 'y':
    # Membersihkan layar
    clear()
    # mereset ulang row
    row = 1
    
    moveTo(col[0], row)
    print('REKAP GAJI PEGAWAI')
    
    changeRow()
    lines()
    changeRow()
    
    # Tabel id nama depan nama belakang golongan gaji pokok tunjangan iuran organisasi
    moveTo(col[0], row)
    id_row = row
    print('ID Pegawai:')
    changeRow()
    
    moveTo(col[0], row)
    print('Nama Depan Pegawai:')
    changeRow()
    
    moveTo(col[0], row)
    print('Nama Belakang Pegawai:')
    changeRow()
    
    moveTo(col[0], row)
    print('Golongan:')
    changeRow()
    
    moveTo(col[0], row)
    print('Gaji Pokok:')
    changeRow()
    
    moveTo(col[0], row)
    print('Tunjangan:')
    changeRow()
    
    moveTo(col[0], row)
    print('Iuran Organisasi:')
    changeRow()
    
    lines()
    changeRow()
    
    # Input
    moveTo(col[3], id_row + 2)
    nama_belakang = input()
    
    ketemu, pos = cariPegawai(nama_belakang)
    
    if ketemu:
        moveTo(col[3], id_row)
        print(pegawai[pos].id)
        moveTo(col[3], id_row + 1)
        print(pegawai[pos].nama_depan)
        moveTo(col[3], id_row + 2)
        print(nama_belakang)
        moveTo(col[3], id_row + 3)
        print(pegawai[pos].golongan)
        moveTo(col[3], id_row + 4)
        print(pegawai[pos].gajiPokok)
        moveTo(col[3], id_row + 5)
        tunjangan = 0
        iuran = 0
        if pegawai[pos].golongan == 'I':
            tunjangan = pegawai[pos].gajiPokok * 0.15
            iuran = 200000
        elif pegawai[pos].golongan == 'II':
            tunjangan = pegawai[pos].gajiPokok * 0.10
            iuran = 150000
        else:
            tunjangan = pegawai[pos].gajiPokok * 0.05
            iuran = 100000
            
        print(tunjangan)
        moveTo(col[3], id_row + 6)
        print(iuran)
        
        moveTo(col[0], id_row + 8)
        print(f'Gaji Akhir: {hitungGaji(pegawai[pos].gajiPokok, tunjangan, iuran)}')
        moveTo(col[0], id_row + 9)
        lanjut = input('Apakah mau lanjut (y/n):')
    
    else:
        moveTo(col[3], id_row + 2)
        input('Data salah.Tekan Enter untuk coba lagi...')
        moveTo(col[3], id_row + 2)
        print('                                                ')
        continue