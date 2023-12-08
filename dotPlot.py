import matplotlib.pyplot as plt
from collections import Counter

def stackedDotPlot(data):
    hitungData = Counter(data)

    plt.figure(figsize=(10, 5))
    for value, count in hitungData.items():
        plt.plot([value] * count, range(1, count + 1), 'ro', ms=8)

    plt.yticks([]) 
    plt.title('Dot Plot')
    plt.xlim(40,95)
    plt.ylim(0,20)
    for i in range(41, 95):
        plt.axvline(i, color='gray', linestyle='-', linewidth=1,ymax=0.009)

    plt.show()

rawData = [63, 79, 71, 59, 66, 55, 70, 72, 68, 75, 65, 46, 60, 69, 71, 67, 
           81, 55, 63, 84, 78, 52, 73, 80, 67, 84, 64, 68, 62, 72, 65, 60, 
           77, 68, 60, 65, 71, 74, 68, 57, 43, 57, 92, 49, 82, 93, 47, 83, 
           53, 93] 

sortedData = sorted(rawData)
data = sortedData
stackedDotPlot(data)
print("Jumlah Data : ",len(data))