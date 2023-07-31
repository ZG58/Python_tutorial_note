class Animal:

    @staticmethod
    def eat():
        print("吃---")

    @staticmethod
    def drink():
        print("喝---")

    @staticmethod
    def run():
        print("跑---")

    @staticmethod
    def sleep():
        print("睡---")


class Dog(Animal):

    def bark(self):
        print("汪汪叫")


class XiaoTianQuan(Dog):

    def fly(self):
        print("我会飞")

    def bark(self):
        print("叫得跟神一样...")


xtq = XiaoTianQuan()

# 如果子类中，重写了父类的方法
# 在使用子类对象调用方法时，会调用子类中重写的方法
xtq.bark()
xtq.run()
