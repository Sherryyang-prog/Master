"""
首页
   1.注册
       输入信息
          校验是否有信息
             校验账号密码是否符合规定
       注册
   2.登录
       2.1 校验是否注册过
       2.2 登录成功
           2.2.1 选课界面
               1 增加课程
                   append
               2 删除课程
                   remove
               3 修改课程
                   修改课程
               4 退出

   3.退出
"""

def print_1():
    print('*************************************************')
    print('*************************************************')
    print('**************欢迎使用中公教育教辅系统***************')
    print('*************************************************')
    print('*************************************************')

def Zhuce():
    print('※※※※※※欢迎使用中公教育教辅系统注册系统※※※※※※※')
    while True:
        Number = input("※请输入你想要注册的账号※\n※请注意账号必须由姓名英文或者数字进行注册，不能由中文编写※\n")
        x = Number.encode('utf-8')
        if x.isalnum() == True:
            print("※账号输入正确※")
            while True:
                Password = input("※请输入你账号想要的密码※\n※请注意密码的长度不能超过10位※")
                if (len(Password)) <= 10:
                    print("注册成功")
                    lst_name.setdefault(Number,Password)
                    break
                else:
                    print("请重新输入你需要的密码")
            break
        else:
            print("请重新输入账号")
            break

def Denglu_1():
    print("※※※※※※欢迎使用中公教育教辅系统登录系统※※※※※※※")
    i = 0
    while i < 3:
        name = input("请输入你的用户名")
        password = input("请输入你的密码")
        if name in lst_name and lst_name[name]==password:
            print("输入密码正确，账户已登陆")
            print("登陆成功")
            print("※※※※※※欢迎使用中公教育教辅系统选课系统※※※※※※※")
            Class = ["数学", "语文", "英语"]
            print("目前学院有以下选修课,1:python,2:UI,3:Java,4:前后端,5:数学,6:语文,7：英语")
            print('------------------------------------------')
            print('你目前已经选修了', Class, "请问你想要进行什么操作？")
            print('------------------------------------------')
            while True:
                Class_1 = input("1:添加课程 2：删除课程 3：修改课程 4：退出")
                if Class_1 == ("1"):
                    Class_ke = input("请输入你想要添加的课程")
                    if Class_ke not in Class:
                        Class.append(Class_ke)
                        print("你目前已选修", Class)
                    else:
                        print("你已经选修了这门课程，请重新选择，当前你已选修", Class + Class_ke)

                if Class_1 == ("2"):
                    Class_del_ke = input("请输入你想要删除的课程")
                    if Class_del_ke not in Class:
                        print("你没有选修这门课")
                    else:
                        Class.remove(Class_del_ke)
                        print("删除成功，你的选修课变为了", Class)

                if Class_1 == ("3"):
                    Class_Xiu_ke = input("请输入你想要修改的课程")
                    Class_Xiuhou_ke = input('请输入你想要修改后的课程')
                    Class[Class.index(Class_Xiu_ke)] = Class_Xiuhou_ke
                    print('修改成功，你的选修课变为了', Class)

                if Class_1 == ("4"):
                    print('欢迎下次光临')
                    break
            break


        elif name not in lst_name or lst_name[name]!=password:
            print("输入密码错误，请重新输入")
            i += 1
    else:
         print("你的账户已经被锁定，请30分钟后再试")

def Tuichu():
    print("欢迎下次光临")


print_1()
lst_name = {"yangxuerui": "123456", "wangyuyin": "88888888", "hemai": "23333333"}

while True:
    Denglu = input("请选择你要实现的功能 1、注册 2、登录 3、退出")
    if Denglu == str(1):
        Zhuce()

    if Denglu == str(2):
        Denglu_1()

    if Denglu == str(3):
        Tuichu()
        break

