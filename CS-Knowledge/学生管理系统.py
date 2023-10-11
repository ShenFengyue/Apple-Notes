#数据库sqlite
#import pypyodbc
#存放学生信息
#student = list()

import sqlite3
#展示菜单
def showMenu():
    print("1.增加学生信息")
    print("2.删除学生信息")
    print("3.修改学生信息")
    print("4.显示学生信息")
    print("0.退出系统")
    select = eval(input("操作："))
    return select
#添加学生信息
def addStudent():
    print("-----增加学生信息-----")
    sno=input("学号:")
    name = input("姓名:")
    sex = input("性别:")
    age = int(input("年龄:"))
    phone = input("电话:")
    conn = sqlite3.connect("student.db")
    cur = conn.cursor()
    cur.execute("insert into info (sno,name,sex,age,phone)values (?,?,?,?,?)",(sno,name,sex,age,phone))
    conn.commit()
    cur.close()
    conn.close()
    print("添加成功!")
    showStudent()
#展示学生信息
def showStudent():
    #连接数据库,进行查询操作
    conn = sqlite3.connect("student.db")
    cur = conn.cursor()
    cur.execute("select * from info")
    data = cur.fetchall()  #cur.fetchall
    if len(data) > 0 :
        print("-----------学生信息------------")
        print("学号\t\t姓名\t\t性别\t\t年龄\t\t电话")
        for i in range(len(data)):
            print(data[i][0],'\t\t',data[i][1],'\t\t',data[i][2],'\t\t',data[i][3],'\t\t',data[i][4])
        print("------------------------------")
    else:
        print("----------信息表为空-----------")
    cur.close()
    conn.close()
#删除学生信息
def delStudent():
        print("---正在进行删除操作---")
        print("-----当前学生信息------")
        showStudent()
        num = input("请输入要删除的学生学号:")
        #连接数据库,进行删除操作
        conn = sqlite3.connect("student.db")
        cur = conn.cursor()
        cur.execute("delete from info where sno = ?",(num))
        conn.commit()
        cur.close()
        conn.close()
        print("删除成功!")
        showStudent()
#修改学生信息
def reviseStudent():
    print("-----正在进行修改操作-----")
    showStudent()
    num = input("请输入要修改的学生学号:")
    print("1-修改姓名\n2-修改性别\n3-修改年龄\n4-修改电话")
    revisenum = eval(input("请输入要修改的信息序号:"))
    newstr = input("请输入新的信息:")
    #连接数据库进行更新操作
    conn = sqlite3.connect("student.db")
    cur = conn.cursor()
    if revisenum == 1:
        cur.execute("update info set name = ? where sno = ?",(newstr,num))
        conn.commit()
        cur.close()
        conn.close()
        print("修改成功!")
        showStudent()
    elif revisenum == 2:
        cur.execute("update info set sex = ? where sno = ?", (newstr, num))
        conn.commit()
        cur.close()
        conn.close()
        print("修改成功!")
        showStudent()
    elif revisenum == 3:
        cur.execute("update info set age = ? where sno = ?", (int(newstr), num))
        conn.commit()
        cur.close()
        conn.close()
        print("修改成功!")
        showStudent()
    elif revisenum == 4:
        cur.execute("update info set phone = ? where sno = ?", (newstr, num))
        conn.commit()
        cur.close()
        conn.close()
        print("修改成功!")
        showStudent()
    else:
        #如果revisenum输入有误,就修改失败
        print("修改失败!请输入正确的修改信息!")

#主要运行函数
def main():
##    #连接数据库,如果数据库不存在,默认在当前路径下创建
##    #str="Driver={Microsoft Access Driver(*.mdb,*.accdb)};DBQ=E:\\db1.accdb"
##    #conn = pypyodbc.win_connect_mdb(str)
    conn=sqlite3.connect("student.db")   #Python连接SQLite数据库
    #获取游标
    cur = conn.cursor()   
    #创建表
    cur.execute("""
                create table info(
                    sno char(10) primary key,
                    name char(20),
                    sex char(20),
                    age integer,
                    phone char(20)
                )
                """)
    #提交事物
    conn.commit()
    #关闭游标
    cur.close()
    #关闭连接
    conn.close()
        
    #显示菜单
    while True:
        select = showMenu()
        if select == 1:
            addStudent()
        elif select == 2:
            delStudent()
        elif select == 3:
            reviseStudent()
        elif select == 4:
            showStudent()
        elif select == 0:
            #退出系统
            break
        else:
            print("输入有误！请重新操作！")
            continue
        
if __name__ == '__main__':
    main()
