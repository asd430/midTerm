#一題花我8小時是正常的對吧
ip=input("找字串中最大質數-請輸入數字字串：")
#重組式
'''
ipl=list(ip)
n=len(ipl)
dx=0
for i in range (n):
    li=int(ipl[i])
    lx=li
    for j in range (n-i-1):
        lx=lx*10
    dx=dx+lx
print(dx)
'''

#質數判斷(A)

tf=False
ipi=int(ip)
if(ipi==2):
    tf=True
else:
    it=int(ipi/2)+2
    for a in range(2,it):
        if(ipi%a==0):
            tf=False
            break
        else:
            tf=True

#print(the end)
if(tf==True):
    print("最大質數為"+str(ipi))
else:
    print("No prime found")


