import pymysql

#创建MySQL对象
class mysql:
    def __init__(self,host,user,password,database):
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        #变量conn初始化为none 确保连接数据库之前不使用conn变量
        self.conn = None

    def connect(self):
        self.conn = pymysql.connect(host=self.host, user=self.user, password=self.password,database=self.database)

    def add(self, id, name, sum, price, data):
        cursor = self.conn.cursor()
        query = "insert into commodity values(%s,%s,%s,%s,%s)"
        cursor.execute(query,(id,name,sum,price,data))
        self.conn.commit()

    def update(self, name, sum, price,data,id):
        cursor = self.conn.cursor()
        query = "update commodity set name=%s,sum=%s,price=%s,data=%s where id=%s"
        cursor.execute(query,(name,sum,price,data,id))
        self.conn.commit()

    def delete(self,id):
        cursor = self.conn.cursor()
        query = "delete from commodity where id = %s"
        cursor.execute(query,(id))
        self.conn.commit()

#inquire处理查询结果、打印数据
    def inquire(self, query):
        cursor = self.conn.cursor()
        cursor.execute(query)
        results = cursor.fetchall()
        return results

    def show_single(self,id):
        cursor = self.conn.cursor()
        query = "select * from commodity where id =%s"
        cursor.execute(query,(id))
        result = cursor.fetchone()
        return result

    def show_all(self):
        query = "select * from commodity"
        result = self.inquire(query)
        return result

    def checkC(self,id):
        cursor = self.conn.cursor()
        #返回指定条件下满足查询条件的数据行数（即统计数量），而不是返回所有匹配的行
        query = "select count(*) from commodity where id = %s"
        cursor.execute(query,(id))
        result = cursor.fetchone()
        return result

    def checkSingle(self,id):
        cursor = self.conn.cursor()
        #返回所有匹配查询条件的行及其所有列的值
        query = "select * from commodity where id = %s"
        cursor.execute(query, (id))
        result = cursor.fetchone()
        return result

    def checkT(self):
        cursor = self.conn.cursor()
        query = "select * from commodity"
        cursor.execute(query)
        result = cursor.fetchall()
        return result

    def quit(self):
        if self.conn is not None:
            self.conn.close()

class commodity:
    def __init__(self, id, name, sum ,price, data):
        self.id = id
        self.name = name
        self.sum = sum
        self.price = price
        self.data = data

class manager:
    def __init__(self,mysql):
        self.mysql = mysql

    def add_com(self):
        id = input("请输入商品编号:")
        name = input("请输入商品名称:")
        sum = input("请输入商品数量:")
        price = input("请输入商品价格:")
        data = input("请输入商品备注:")
        result = self.mysql.checkC(id)
        if result[0] == 0:
            self.mysql.add(id,name,sum,price,data)
            print("添加商品成功！")
        else:
            print("此商品已经存在！")
        #coms = self.show_all()
        #com = commodity(id,name,sum,price,data)
        # if any(c.id == com.id for c in coms):
        #     print("此商品已经存在！")
        # else:
        #     self.mysql.add(id, name, sum, price,data)
        #     print("添加商品成功！")

    def update_com(self):
        id = input("请输入想要修改的商品编号:")
        name = input("请输入新的商品名称:")
        sum = input("请输入新的商品数量:")
        price = input("请输入新的商品价格:")
        data = input("请输入新的商品备注:")

        if self.mysql.checkC(id)[0] > 0:
            self.mysql.update(name,sum,price,data,id)
            print("修改商品成功！")
        else:
            print("此商品不存在！")
        #com = commodity(id,name,sum,price,data)
        #coms = self.show_all()

        # if not any(c.id == id for c in coms):
        #     print("此商品不存在！")
        # else:
        #     self.mysql.update(name,sum,price,data,id)
        #     print("修改商品成功！")

    def delete_com(self):
        id = input("请输入要删除的商品编号:")

        if self.mysql.checkC(id)[0] > 0:
            self.mysql.delete(id)
            print("删除商品成功！")
        else:
            print("此商品不存在！")
        #coms = self.show_all()

        # if not any(c.id == id for c in coms):
        #     print("此商品不存在！")
        # else:
        #     self.mysql.delete(id)
        #     print("删除商品成功！")
    def show_single(self):
        id = input("请输入要查找的商品编号:")
        result = self.mysql.checkSingle(id)

        if result is None:
            print("查找的商品不存在！")
        else:
            print(f"商品编号:{result[0]} 商品名称:{result[1]} 商品数量:{result[2]} 商品价格:{result[3]} 商品信息:{result[4]}")


    def show_all(self):
        result = self.mysql.checkT()
        # coms = [commodity(result[0],result[1],result[2],result[3],result[4]) for result in results]
        # return coms
        if len(result) == 0:
            print("商品信息为空！")
        else:
            print("-----------------商品信息-------------------")
            for i in result:
                print(f"商品编号:{i[0]} 商品名称:{i[1]} 商品数量:{i[2]} 商品价格:{i[3]} 商品信息:{i[4]}")

#创建mysql对象
mysql = mysql(host='localhost',user='root',password='wqwy041803160322',database='commodity')
#连接数据库
mysql.connect()

manager =  manager(mysql)

while True:
    print("-------------欢迎使用商品管理系统--------------")
    print("------1.添加商品----------")
    print("------2.修改商品----------")
    print("------3.删除商品----------")
    print("------4.查看单个商品-------")
    print("------5.查看所有商品-------")
    print("------6.退出系统----------")
    choice = input("请输入要进行的操作:")

    if choice == '1':
        manager.add_com()
    elif choice == '2':
        manager.update_com()
    elif choice == '3':
        manager.delete_com()
    elif choice == '4':
        manager.show_single()
    elif choice == '5':
        manager.show_all()
    elif choice == '6':
        break
    else:
        print("没有此操作数！")

mysql.quit()