import os
import pymysql

conn = pymysql.connect(host='localhost',user='root',password='wqwy041803160322',db='commodity')

cursor=conn.cursor()

#创建商品类
class commodity:
    def __init__(self, id, name, sum ,price, data):
        self.id = id
        self.name = name
        self.sum = sum
        self.price = price
        self.data = data

class manager():
    def __init__(self,conn):
        self.conn = conn

    def add_com(self, commodity):
        cursor = self.conn.cursor()
        cursor.execute('select count(*) from commodity where id = %s', commodity.id)
        #fetchone()函数它的返回值是单个的元组,也就是一行记录,如果没有结果,那就会返回null
        result = cursor.fetchone()

        if result[0] == 0:
            cursor.execute('insert into commodity values (%s,%s,%s,%s,%s)',(commodity.id,commodity.name,commodity.sum,commodity.price,commodity.data))
            self.conn.commit()
            print("添加商品成功！")
        else:
            print("此商品已经存在！")
        cursor.close()

    def update_com(self,commodity):
        cursor = self.conn.cursor()
        cursor.execute('select count(*) from commodity where id = %s', commodity.id)
        result = cursor.fetchone()

        if result[0] > 0:
            cursor.execute('update commodity set name=%s,sum=%s,price=%s,data=%s where id=%s',(commodity.name, commodity.sum, commodity.price, commodity.data, commodity.id))
            self.conn.commit()
            print("更新商品成功！")

        else:
            print("此商品不存在！")
        cursor.close()

    def delete_com(self,id):
        cursor = self.conn.cursor()
        cursor.execute('select count(*) from commodity where id = %s', id)
        result = cursor.fetchone()

        if result[0] > 0:
            cursor.execute('delete from commodity where id=%s', id)
            self.conn.commit()
            print("删除商品成功！")
        else:
            print("此商品不存在，无法删除！")
        cursor.close()

    def show_single(self,id):
        cursor = self.conn.cursor()
        cursor.execute('select * from commodity where id = %s', id)
        result = cursor.fetchone()

        if result is None:
            print("查找的商品不存在！")
        else:
            print(f"商品编号:{result[0]} 商品名称:{result[1]} 商品数量:{result[2]} 商品价格:{result[3]} 商品信息:{result[4]}")
        cursor.close()

    def show_all(self):
        cursor = self.conn.cursor()
        cursor.execute('select * from commodity')
        result = cursor.fetchall()
        if len(result) == 0:
            print("商品信息为空！")
        else:
            print("-----------------商品信息-------------------")
            for i in result:
                print(f"商品编号:{i[0]} 商品名称:{i[1]} 商品数量:{i[2]} 商品价格:{i[3]} 商品信息:{i[4]}")
        cursor.close()

manager =  manager(conn)
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
        id = input("请输入商品编号:")
        name = input("请输入商品名称:")
        sum = input("请输入商品数量:")
        price = input("请输入商品价格:")
        data = input("请输入商品备注:")
        commodity = commodity(id, name, sum, price, data)
        manager.add_com(commodity)
    elif choice == '2':
        id = input("请输入想要修改的商品编号:")
        name = input("请输入新的商品名称:")
        sum = input("请输入新的商品数量:")
        price = input("请输入新的商品价格:")
        data = input("请输入新的商品备注:")
        commodity = commodity(id,name, sum, price, data)
        manager.update_com(commodity)
    elif choice == '3':
        id = input("请输入要删除的商品编号:")
        manager.delete_com(id)
    elif choice == '4':
        name = input("请输入要查看的商品编号:")
        manager.show_single(name)
    elif choice == '5':
        manager.show_all()
    elif choice == '6':
        break
