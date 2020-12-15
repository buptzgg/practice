# encoding='utf-8'
import requests
import re

# 断点调式
class Spider():
    url = 'https://www.huya.com/g/2336'
    root_pattern = re.compile('<li class="game-live-item"[\s\S]*?</li>')
    name_pattern = re.compile(' <i class="nick" title=[\s\S]*?>([\s\S]*?)</i>')
    number_pattern = re.compile('<i class="js-num">([\s\S]*?)</i>')

    def __fetch_contant(self): # 两个__表示私有方法
        r = requests.get(Spider.url)
        R = r.text
        return R

    def __analysiss(self,htmls):
        root_html = re.findall(Spider.root_pattern, htmls)
        anchors = []
        for html in root_html:
            name_html = re.findall(Spider.name_pattern, str(html))
            number_html = re.findall(Spider.number_pattern, str(html))
            anchor = {'name':name_html,'number':number_html}
            anchors.append(anchor)
        return anchors



    def __refine(self,anchers):
        I = lambda anchor:{'name':anchor['name'][0].strip()
                           ,'number':anchor['number'][0]}

        return map(I,anchers)


    def __sort(self,anchors):
        anchors = sorted(anchors,key=self.__sort_seed,reverse=True)
        return anchors

    def __sort_seed(self,anchor):
        n = re.findall('\d*',anchor['number'])
        number = float(n[0])
        if '万' in anchor['number']:
            number *=10000
        return number

    def __show(self,anchors):
        for rank in range(0,len(anchors)):
            print('主播' + ':' + anchors[rank]['name'] + '——————————' + '人气' + ':' + anchors[rank]['number'] +'————————'  + '排名' + ':' + str(rank+1))



    def go(self):
        R = self.__fetch_contant()
        anchors = self.__analysiss(R)
        anchors = list(self.__refine(anchors))
        anchors = self.__sort(anchors)
        self.__show(anchors)


spider = Spider()
spider.go()
