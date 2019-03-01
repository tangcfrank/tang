def hanio(n,x,y,z):
    if n == 1:
        print(x,'---------->',z)
    else:
        hanio(n-1,x,z,y)#将n-1个从X移动到Y,中间z属于借助柱子
        print(x,'---------->',z) #将剩下1个从X移动到Z
        hanio(n-1,y,x,z)#将n-1个从Y移动到Z
num = int(input('输入汉诺塔的层数：'))
result = hanio(num,'X','Y','Z')