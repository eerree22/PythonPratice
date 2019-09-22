#Function
def MyFunction_1():
    print("111")
    print("222")


MyFunction_1()

print("333")


#帶變數的Function
def MyFunction_2(Last_name, First_Name):
    print(f"Hello {Last_name}{First_Name}!!")


MyFunction_2("陳", "水扁")
MyFunction_2("馬", "英九")


#帶變數的Function+回傳
def MyFunction_3(name):
    return f"Hi {name}!!"


return_value = MyFunction_3("Howard")
print(return_value)


def Add(x, y):
    return x + y


print(Add(x=12, y=564))  #參數可以這樣寫，稱為key word參數


#function with 非必填參數  *非必填參數一定要放在必填參數的後面
def Subtraction(x, z, y=1):
    return x + z - y


print(Subtraction(5, 3))  #=5+3-1
print(Subtraction(5, 4, 5))  #=5+4-5


#使用集合當參數的function
def Multiplier(*GY):  #星號+參數名 = 集合參數
    total = 1
    for number in GY:
        total *= number
    return total


print(Multiplier(2, 3, 4, 5))


#使用dictionary當參數的function
def Save_UserData(**user):  #2個星號的參數 = dictionary
    print(user)
    print("id=" + user["id"])
    print("name=" + user["name"])


Save_UserData(id="1", name="Howard", age=28)

#實用操作筆記
#1 將整行上下移動 => alt + 上 or 下
#2 複製整行 => shift + alt + 下
#3 註解整行 => ctrl + /


#fizz_buzz algo
# if input 可以被3整除 =>return fizz
# if input 可以被5整除 =>return buzz
# if input 可以被3跟5整除 =>return fizzbuzz
# else return input
def fizz_buzz(i):
    if i % 3 == 0 and i % 5 == 0:
        return "fizz buzz"

    if i % 3 == 0:
        return "fizz"

    if i % 5 == 0:
        return "buzz"

    return i


fizz_buzz(21)
