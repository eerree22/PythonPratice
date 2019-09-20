print("ghskjdghjd")
10 > 3

temp = 30
if temp > 30:
    print("GG")
else:
    print("YY")

Teranry = "X" if temp > 30 else "Y"
print(Teranry)

老師 = "呂執中"

老師[0]
老師[-1]
老師[0:2]
老師[1:]

長字串 = """
   第一行
   隨便打
   隨意換行
"""
len(長字串)  #len=回傳集合的item數量，在這邊=字串的長度

print(長字串)

course = "network \"management\" "  #字串中加入雙引號
print(course)

firstname = "HAO-WEI"
lastname = "CHANG"
name = f"{firstname} {lastname}"
#print(name)

print(name.lower())  #變小寫  upper()變大寫
print(name.title())  #每個單字第一個字大寫

x = "   how are you?   "
print(x)
print(x.strip())  #將字串左右的空白消去
print(x.rstrip())  #將字串右邊的空白消去
print(x.lstrip())  #將字串左邊的空白消去
print(x.find("how"))  #尋找指定字最早出現的index
print(x.replace("o", "G"))  #取代 左舊右新
print("GG" in x)  #查GG是否存在x中
print("GG" not in x)  #查GG是否不存在x中

print(10 / 3)   #除法帶小數點
print(10 // 3)  #除法去掉小數點

print(2**15) #2的15次方

round(2.5) #4捨6入
abs(-99)  #取絕對值

import math  #引用數學函式庫
math.ceil(-3.3)  #return不小於x的最小整數

S="123"
type(S) #查看型別

int(S) #轉型成int
type(S)