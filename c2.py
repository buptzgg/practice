# encoding='utf-8'
import requests
import re
url = 'https://item.taobao.com/item.htm?ft=t&spm=a211oj.20087502.7241908900.ditem0.26562a7bQm4jqK&id=625800201188&scm=1007.12144.167873.11865844_0_0&pvid=655be9dc-8166-4bb9-ba31-e36c66c0ad7d&utparam=%7B%22x_hestia_source%22%3A%22tm_fen_floor%22%2C%22x_object_type%22%3A%22item%22%2C%22x_hestia_subsource%22%3A%22default%22%2C%22x_mt%22%3A0%2C%22x_src%22%3A%22tm_fen_floor%22%2C%22x_pos%22%3A1%2C%22wh_pid%22%3A214753%2C%22x_pvid%22%3A%22655be9dc-8166-4bb9-ba31-e36c66c0ad7d%22%2C%22scm%22%3A%221007.12144.167873.11865844_0_0%22%2C%22x_object_id%22%3A625800201188%2C%22tpp_buckets%22%3A%222144%230%23167873%230%22%7D'
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36 Edg/87.0.664.60"}
r = requests.get(url=url,headers=headers)
R = r.text
# print(R)


day = 7
def day_sunday():
    return 'Sunday'

def day_monday():
    return 'Monday'

def day_tuesday():
    return 'Tuesday'

def day_other():
    return 'without'

switch = {
    0:day_sunday,
    1:day_monday,
    2:day_tuesday
}

day_name = switch.get(day,day_other)()
print(day_name)


#列表推导式
a = [1,2,3,4,5,6,7,8]
b = [i*i for i in a if i>5]
print(b)

#用字典编写列表推导式
students = {
    'house':12,
    'desk':25,
    'chair':18
}

teacher = [key for key,values in students.items()]
print(teacher)

class bookcollection:
    def __init__(self):
        self.data = ['《往事》','《围城》','《朝花夕拾》']
        self.cur = 0

    def __iter__(self):
        return self
    def __next__(self):
        if self.cur >= len(self.data):
            raise StopIteration()
        r = self.data[self.cur]
        self.cur +=1
        return r

books = bookcollection()
for book in books:
    print(book)

#生成器
n = [i for i in range(0,10001)]
# print(n)

def generator(max):
    n = 0
    while n <=max:
        n +=1
        yield n #生成器的内部没有保存如何的数据，只保存了算法，yield返回n的值，第二次执行循环时继续上次的n值执行
        # print(n)

g = generator(10000)
# print(g)
for x in g:
    pass
    # print(x)

a = []
print(not a)
print(a is None)


class test():
    def __len__(self):
        print('bool called')
    def __bool__(self):
        print('len called')
        return True

# print(len(test()))
print(bool(test()))