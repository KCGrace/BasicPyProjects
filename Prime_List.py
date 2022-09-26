x=input("請輸入介於 2~10000之間的整數:")
# x預設為str
list=[]
primelist=[]
#prime between 2 - 9999
n=int(x)
for i in range(2,n+1):
    for j in range(2,int(i**0.5)+1):
        if i%j ==0:
            break
    else:
        primelist.append(i)
print(primelist)
if int(x)>=2 and int(x)<=10000:
    #for i in range(1,len(x)-1):
    for i in list:
        if i in primelist:
            list.append(i)
print(list)
#else:
    #print("請重新輸入")
        #range(10)：產生從0到9的整數序列。
        #1:[0][1][2][3]...[len(x)-1]
        #2:[01][12][23][34][len(x)-2:len(x)-1]
        #3:[012][123][234][345]...[len(x)-3:len(x)-1]
        #len(x)-1:[0123..len(x)-1]
        #for j in range(1,len(x)-1):
            #list.append(x[j:i+j,i+1])
            #print(list)
#print(max.list())
