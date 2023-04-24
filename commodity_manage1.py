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

    def update(self, id, name, sum, price,data):
        cursor = self.conn.cursor()
        query = "update  commodity update commodity set name=%s,sum=%s,price=%s,data=%s where id=%s"
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

    def show_all(self):
        query = "select * from commodity"
        result = self.inquire(query)
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

class manager():
    def __init__(self,mysql):
        self.mysql = mysql

    def add_com(self):
        id = input("请输入商品编号:")
        name = input("请输入商品名称:")
        sum = input("请输入商品数量:")
        price = input("请输入商品价格:")
        data = input("请输入商品备注:")

        coms = self.show_all()

        if any(c.id == commodity.id for c in coms):
            print("此商品已经存在！")
        else:
            self.mysql.add(id, name, sum, price,data)
            print("添加商品成功！")

    def update_com(self):
        id = input("请输入想要修改的商品编号:")
        name = input("请输入新的商品名称:")
        sum = input("请输入新的商品数量:")
        price = input("请输入新的商品价格:")
        data = input("请输入新的商品备注:")
        coms = self.show_all()

        if not any(c.id == commodity.id for c in coms):
            print("此商品不存在！")
        else:
            self.mysql.update(id,name,sum,price,data)
            print("修改商品成功！")

    def delete_com(self):
        id = input("请输入要删除的商品编号:")
        coms = self.show_all()

        if not any(c.id == commodity.id for c in coms):
            print("此商品不存在！")
        else:
            self.mysql.delete(id)
            print("删除商品成功！")

    def show_all(self):
        results = self.mysql.show_all()
        coms = [commodity(result[0],result[1],result[2],result[3],result[4]) for result in results]
        return coms

#创建mysql对象
mysql = mysql(host='localhost',user='host',password='wqwy041803160322',database='commodity')
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
    choice = input("请输入要进行的操作：")

    if choice == '1':
        manager.add_com()
    elif choice == '2':
        manager.update_com()
    elif choice == '3':
        manager.delete_com()
    elif choice == '4':
        id = input("请输入想要查看的商品编号:")
        coms = manager.show_all()

        if not any(c.id == id for c in coms):
            print("此商品不存在！")
        else:
            #next() 获取迭代器的下一个元素
            result = next(c for c in coms if c.id == id)
            print(f"商品编号:{result.id} 商品名称:{result.name} 商品数量:{result.sum} 商品价格:{result.price} 商品信息:{result.data}")
    elif choice == '5':
        coms = manager.show_all()
        for i in coms:
            print(f"商品编号:{i.id} 商品名称:{i.name} 商品数量:{i.sum} 商品价格:{i.price} 商品信息:{i.data}")
    elif choice == '6':
        break
    else:
        print("没有此操作数！")

mysql.quit()