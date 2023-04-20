import os

with open(file="commodity.txt", encoding="utf-8") as x:
    info = x.readlines()
    tempInfo = []
    newInfo = []
    list_data = []
    for i in info:
        tempInfo.append(i.strip())
    for i in tempInfo:
        temp_list = i.split()
        newInfo.append(temp_list)

    keys = ["商品名称", "数量", "价格", "备注"]
    for i in newInfo:
        d1 = dict(zip(keys, i))
        list_data.append(d1)

class manager():

    def show_choice(self):
        print("-------------欢迎使用商品管理系统--------------")
        print("------1.添加商品----------")
        print("------2.修改商品----------")
        print("------3.删除商品----------")
        print("------4.查看单个商品-------")
        print("------5.查看所有商品-------")
        print("------6.退出系统----------")

    def add_commodity(self):
        while True:
            name = input("请输入商品名称：")

            flag=0

            for i in range(len(list_data)):
                if list_data[i]["商品名称"]==name:
                    print("此商品已经存在！")
                    flag += 1
                    break
                else:
                    pass
            if flag==0:
                break
            else:
                f1=input("是否重新输入商品信息？(1)是 (2)否 请输入：")
                if f1 == "1":
                    pass
                else:
                    return list_data
        sum = input("请输入商品数量：")
        price = input("请输入商品价格：")
        remark = input("请输入商品备注：")

        com_dict={}
        com_dict["商品名称"]=name
        com_dict["数量"] = sum
        com_dict["价格"] = price
        com_dict["备注"] = remark
        list_data.append(com_dict)
        print("添加商品成功")

        return list_data

    def update_com(self):
        while True:
            name = input("请输入想要修改的商品名称：")
            flag=0;

            for i in range(len(list_data)):
                if name == list_data[i]["商品名称"]:
                    print("1.商品名称")
                    print("2.数量")
                    print("3.价格")
                    print("4.备注")

                    ch=input("请输入想要修改的内容对应的选项：")

                    if ch =="1":
                        while True:
                            new_name = input("请输入新的商品名称：")
                            f1=0
                            for j in range(len(list_data)):
                                if list_data[j]["商品名称"]==new_name:
                                    print("此商品已经存在！")
                                    f1+=1
                                    break
                                else:
                                    list_data[i]["商品名称"]=new_name
                            if f1==0:
                                break
                            else:
                                f2=input("是否要重新输入商品名称? (1)是 (2)否 请输入：")
                                if f2=="1":
                                    pass
                                else:
                                    return list_data

                    elif ch == "2":
                        new_sum = input("请输入商品数量：")
                        list_data[i]["数量"]=new_sum
                    elif ch == "3":
                        new_price = input("请输入商品价格：")
                        list_data[i]["价格"] = new_price
                    elif ch == "4":
                        new_remark = input("请输入商品备注：")
                        list_data[i]["备注"] = new_remark
                    else:
                        break

                    flag+=1
                    print("商品修改成功")

                    break

                else:
                    pass

            if flag == 0:
                f1 = input("商品不存在，是否重新输入? (1)是 (2)否 请输入：")

                if f1 == "1":
                    pass
                else:
                    break

            else:
                break

        return list_data

    def delete_com(self):
        while True:
            name = input("请输入要删除的商品名称：")
            flag=0
            for i in range(len(list_data)):
                if name == list_data[i]["商品名称"]:
                    list_data.pop(i)
                    flag+=1
                    print("删除成功！")
                    break
                else:
                    pass
            if flag==0:
                f1=input("商品不存在，是否重新输入? (1)是 (2)否 请输入：")
                if f1=="1":
                    pass
                else:
                    break
            else:
                break
        return list_data

    def show_single(self):
        if list_data == []:
            print("商品信息不能为空，添加一个吧！")
            return

        find=input("请输入查找商品的名称：")
        flag=0
        for dict_data in list_data:
            if find == dict_data["商品名称"]:
                flag+=1
                com_dict=dict_data
                break
            else:
                continue
        if flag == 0:
            print("查找的商品不存在！")
        else:
            for key in com_dict.keys():
                print(key.ljust(10, ' '), end='')
            print()
            print("*"* 70)

            for value in com_dict.values():
                print(value.ljust(10, ' '), end='')
            print()
            print("*"*70)
            print('\r\r')

    def show_all(self):
        if list_data == []:
            print("商品信息不能为空，添加一个吧！")
            return

        key_data = list_data[0].keys()
        for key in key_data:
            print(key.ljust(10, ' '), end='')
        print()

        print("*" * 70)

        for dict_data in list_data:
            for value in dict_data.values():
                print(value.ljust(8, '　'), end='')
            print()

        print("*" * 70)
        print('\r\r')

if __name__ == '__main__':
    while True:
        man = manager()
        man.show_choice()
        ch = input("请选择想要进行的操作：")

        if ch=="1":
            commodityInfo=man.add_commodity()
        elif ch=="2":
            commodityInfo=man.update_com()
        elif ch == "3":
            commodityInfo = man.delete_com()
        elif ch=="4":
            man.show_single()
        elif ch=="5":
            man.show_all()
        elif ch=="6":
            break
        else:
             print("没有此操作序号，请重新输入！")

        if ch in ("1", "2", "3"):
            with open(file="commodity1.txt", encoding="utf-8", mode="w+") as g:
                for i in commodityInfo:
                    com_info = i.values()
                    com_info = ' '.join(com_info)
                    com_info = com_info + "\n"
                    g.write(com_info)
        else:
            with open(file="commodity.txt", encoding="utf-8") as w:
                with open(file="commodity1.txt", encoding="utf-8", mode="w+") as q:
                    old_commodity_info = w.readlines()
                    q.writelines(old_commodity_info)

        os.remove("commodity.txt")
        os.rename("commodity1.txt", "commodity.txt")