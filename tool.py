import math

rawData = [63, 79, 71, 59, 66, 55, 70, 72, 68, 75, 65, 46, 60, 69, 71, 67, 
           81, 55, 63, 84, 78, 52, 73, 80, 67, 84, 64, 68, 62, 72, 65, 60, 
           77, 68, 60, 65, 71, 74, 68, 57, 43, 57, 92, 49, 82, 93, 47, 83, 
           53, 93]

data = sorted(rawData)
jumlahData = len(data)
print("Urutannya : \n",', '.join(map(str, data)))
print ('Jumlah Datanya :',len(data))

# Mencari Frekuensi
def frekuensi(myData):
    freq={}
    for i in data :
        freq[i]= freq.get(i,0)+1
    return freq
#
frequency_dict = frekuensi(data)
print('Frekuensinya :')
for key, value in frequency_dict.items():
    print(f'{key} : {value}')
print('Jumlah Data : ', len(frequency_dict))

# Logaritma 
n =len(data)
logN = round(math.log10(n),4)
print('Logaritma : ', logN)

# Banyak Kelas
jumlahKelas = 1 + (3.3 * logN)
print ('Banyak Kelas :', jumlahKelas)

jumlahKelas= round(jumlahKelas)
print('Banyak Kelas (Round) :',jumlahKelas)

# Nilai Min & Max 
minData = min(data)
maxData = max(data)
print('Min :',minData )
print('Max :',maxData )

# Range 
rangeData = maxData - minData
print('Range :',rangeData)

# Mean
meanData = sum(data)/len(data)
print('Mean :',meanData)

#Panjang/Lebar Kelas 
panjangKelas = rangeData/jumlahKelas
print('Panjang Kelas :',panjangKelas)
panjangKelas = round(panjangKelas)
print('Panjang Kelas (Round):',panjangKelas)
