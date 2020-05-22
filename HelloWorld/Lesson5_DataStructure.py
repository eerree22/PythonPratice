#內建的資料儲存結構

abc=["a","b","c"]
print(abc)

matrix=[[0,0,0],[1,1,1],[2,2,2]]

zeros=[0]*5
print(zeros)

combine=abc+zeros
print(combine)

numbers=list(range(20))  
print(numbers)
print(numbers[::2]) #印出所有偶數
print(numbers[-1])  #反向印出list所有內容

#list unpacking
ontwothree=[1,2,3]
one,two,three=ontwothree    #左邊指派的變數對應右邊list的內容
print(one,two)

first,*other,last=numbers #如果list很大可以用*符號的變數來放
print(first,last)
print(other)


chars=list("fuck")
print(chars)
print(len(chars))
print(chars[0])
print(chars[0:3]) #print from index 0~2
print(chars[:3])#also print from indexx 0~2  start from zero is default
print(chars[0:])#also print from indexx 0~3  len of list is default if 沒寫


