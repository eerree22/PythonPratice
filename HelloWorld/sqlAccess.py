#使用pyodbc連結sqlServer，pyodbc需要先安裝，說明書: https://github.com/mkleehammer/pyodbc/wiki
import pyodbc

class sqlAccess:
    #建構子，connectionString=連接字串(string)
    #連接字串格式參考: https://github.com/mkleehammer/pyodbc/wiki/Connecting-to-SQL-Server-from-Windows
    def __init__(self,connectionString):
        self.conn = pyodbc.connect(connectionString)
        self.cursor = self.conn.cursor()
    
    #解構子
    def __del__(self):
        self.cursor.close()
        self.conn.close()

    #讀資料，return cursor物件
    def read(self,sqlStatement):
        print("Read")
        self.cursor.execute(sqlStatement)
        return self.cursor

    #執行sqlStatement，透過executemany一次執行複數的params  (e.g. 一次新增複數資料)
    def executeStatement(self,sqlStatement,params):
        try:
            self.conn.autocommit = True
            self.cursor.executemany(sqlStatement, params)
        except pyodbc.DatabaseError as err:
            self.conn.rollback()
        else:
            self.conn.commit()
        finally:
            self.conn.autocommit = True
    
    #呼叫預存程序，Name=預存程序名稱
    def callStoredProcedures(self,Name):
        self.cursor.execute("{CALL " + Name +"}")
        self.cursor.commit()

    #呼叫具有input參數的預存程序
    def callStoredProceduresWithInput(self,Name,params):
        self.cursor.execute("{CALL " + Name +"}",params)
        self.cursor.commit()





#以下測試此class功能，使用本機SQL Server 2017 EXPRESS，Northwind資料庫
myConnectionString='DRIVER={ODBC Driver 17 for SQL Server};SERVER=localhost\\SQLEXPRESS;DATABASE=Northwind;Trusted_Connection=yes;'

#呼叫class建構子
mysqlAccess=sqlAccess(myConnectionString)

#讀Customers資料
myCursor=mysqlAccess.read('Select * From Customers')

#可以用description查看回傳的欄位
print(myCursor.description)

#用迴圈跑過Cursor內所有回傳的資料
for row in myCursor:
    myCustomerID = row.CustomerID #透過row.欄位名稱 存取該欄位資料
    myCompanyName = row[1] #或用row[欄位的index]
    print(f'CustomerID = {myCustomerID}, GG = {myCompanyName}')

#TestTable => AAA[int],BBB[nvarchar(50)],CCC[datetime]
#測試新增3行資料
insertStatement="INSERT INTO TestTable ([AAA],[BBB],[CCC]) VALUES (?,?,?)"
insertData=[ (1, "A","2019-12-1"), (2, "B","2019-12-24") , (3, "C","2019-12-25")]
mysqlAccess.executeStatement(insertStatement,insertData)

#測試修改，將AAA小於2的CCC改成2019-12-10
updateStatement="UPDATE TestTable SET CCC=? WHERE AAA < ?"
updateParams=[("2019-12-10",2)]
mysqlAccess.executeStatement(updateStatement,updateParams)

#測試刪除，將AAA=1的資料刪除
updateStatement="DELETE FROM TestTable WHERE AAA = ?"
updateParams=[(1,)] #這個list在只有一個參數時候面還是要加逗點，否則執行會出錯
mysqlAccess.executeStatement(updateStatement,updateParams)

#測試呼叫具有input參數的預存程序
params = (6, "GG","2019-11-11")
mysqlAccess.callStoredProceduresWithInput("TestTable_Insert (?,?,?)",params)
