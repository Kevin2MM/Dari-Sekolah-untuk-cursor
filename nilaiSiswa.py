import sys
import os

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
for i in range(1,4):
    moveTo(col[0],row)
    print(i)
    moveTo(col[1],row)
    nama=input()
    moveTo(col[2],row)
    nilai1=float(input())
    moveTo(col[3],row)
    nilai2=float(input())
    moveTo(col[4],row)
    nilai3=float(input())
    moveTo(col[5],row)
    print(f"{hitungRata(nilai1,nilai2,nilai3):.1f}")
    changeRow()

#print closing lines
moveTo(col[0],row)
lines()

