
import sys

maxlength=[]
linese=[]


n=int(input("please enter n"))
for i in range(n): #input 
    line=sys.stdin.readline()
    linese.append(line.split())


for i in range(n):
    linese[i][0]=int(linese[i][0])
    linese[i][1]=int(linese[i][1])
    maxlength.append(int(0))


for i in range(n):
    for j in range(n):
        if i!=j and linese[i][0]<=linese[j][0] and linese[i][1]>=linese[j][0] and linese[i][1]<=linese[j][1]:
            linese[i][1]=linese[j][1]
        if i!=j and linese[j][0]<=linese[i][0] and linese[i][0]<=linese[j][1] and linese[j][1]<=linese[1][1]:
            linese[i][0]=linese[j][0]
        if i!=j and linese[j][0]<=linese[i][0] and linese[j][1]>=linese[i][1]:
            linese[i][0]=linese[j][0]
            linese[i][1]=linese[j][1]
    maxlength[i]=linese[i][1]-linese[i][0]


print(max(maxlength))
            