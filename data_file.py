import os
import csv

class Siswa:
    def __init__(self, id, nama, nilai1, nilai2, nilai3):
        self.id = id
        self.nama = nama
        self.nilai1 = nilai1
        self.nilai2 = nilai2
        self.nilai3 = nilai3

def clear():
    # Use 'cls' for Windows (os.name is 'nt') and 'clear' for Linux/macOS
    os.system('cls' if os.name == 'nt' else 'clear')

def getData():
    global siswa
    #read data from file & transfer to object array
    with open('data.csv', mode='r') as file:
        reader = csv.reader(file)
        for row in reader:
            siswa.append(Siswa(row[0],row[1],row[2],row[3],row[4]))


clear()
#create new siswa as array
siswa=[]

#read data from
getData()
        
for data in siswa:
    print(data.id,data.nama,data.nilai1,data.nilai2,data.nilai3)