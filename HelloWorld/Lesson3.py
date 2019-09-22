#流程控制

10 == "10"

# ord回傳unicode字碼
ord("A")
ord("a")
ord("b")

氣溫 = 36
if 氣溫 > 30 and 氣溫 <= 35:
    print("喝水喝水500cc")
elif 氣溫 > 35:
    print("停止動作")
else:
    print("繼續動作")

age = 21
message = "成年" if age >= 18 else "未成年"  #將if else 寫在指派中
print(message)

if age >= 18 and age < 65:
    print("成年人")

if 18 <= age < 65:  #between也可以這樣寫，跟22行的意思相同
    print("成年人")

# and or not  邏輯運算子
高 = True
富 = True
帥 = True

if (高 or 富) and not 帥:  #高或富，但不要帥的not
    print("ok")
else:
    print("not ok")

# for迴圈
for number in range(3):  # 0開始，到3停  (不包含3)
    print("第" + str(number) + "次")

for number in range(1, 4):  # 1開始，到4停  (不包含4)
    print("第" + str(number) + "次")

for number in range(1, 10, 2):  # 1開始，每次+2，到10停  (不包含10)
    print("第" + str(number) + "次")

# for...else
for letter in "abcdefg":
    if letter == "d":
        break
    print(letter)
else:
    print("中間沒break掉才會執行到這")

for letter in "abcdefg":
    if letter == "d":
        continue
    print(letter)
else:
    print("中間沒break掉才會執行到這")

#巢狀迴圈
for length in range(4):
    for width in range(4):
        print(f"{length},{width},{length*width}")

#可遞迴
type(range(5))
type(range(5)[0])

for i in range(3):
    print(i)

for i in "range(3)":
    print(i)

for i in ["ggg", "yyy", "kkk"]:
    print(i)

# while loop
count = 10
while count > 0:
    print(count)
    count = count - 1

command = ""
while command.lower() != "quit":  #重複執行直到user input "quit" 才跳出while
    command = input(">")
    print(command)

while True:  # 重複執行直到user input "quit" 才跳出while
    command = input(">")
    print(command)
    if command.lower() == "quit":
        break  #跟上面的功能相同，但這個寫法一定要break否則會產生無窮迴圈

count = 0
for evenNumber in range(1, 11):
    if evenNumber % 2 == 0:
        count += 1
        print(evenNumber)
else:
    print(f"有{count}個偶數")
