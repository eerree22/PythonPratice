#宣告類別
class Point:
    default_color = "Red"  #class attribute，由所有這個class的實體共享

    __privateGGYY = "GY"  #雙底線開頭=private

    def __init__(self, x, y):  #建構子: __init__
        self.x = x  #instance attribute 實體各自擁有
        self.y = y  #instance attribute

    @classmethod
    def zero(cls):
        return cls(0, 0)  #class method，用處還不太懂

    def drew(self):
        print(f"x={self.x},y={self.y}")

    def __str__(self):
        return "GGYY"  #magic method =>繼承自class類別的function，都會用雙底線包起來
        #詳見https://rszalski.github.io/magicmethods/

    #雙底線開頭的方法=私有方法
    def __SecretMethod(self):
        return "秘密"


Point.default_color = "shit"  #修改class attribute，下面兩個實體的default_color都會被改到

point = Point(1, 2)
point.drew()
print(point.x)
print(point.default_color)

point2 = Point(1, 2)
print(point2.default_color)

print(point2)
