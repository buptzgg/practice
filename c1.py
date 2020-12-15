# encoding='utf-8'
import requests
import re
class taobao():
    url = 'https://item.taobao.com/item.htm?ft=t&spm=a211oj.20087502.7241908900.ditem0.26562a7bQm4jqK&id=625800201188&scm=1007.12144.167873.11865844_0_0&pvid=655be9dc-8166-4bb9-ba31-e36c66c0ad7d&utparam=%7B%22x_hestia_source%22%3A%22tm_fen_floor%22%2C%22x_object_type%22%3A%22item%22%2C%22x_hestia_subsource%22%3A%22default%22%2C%22x_mt%22%3A0%2C%22x_src%22%3A%22tm_fen_floor%22%2C%22x_pos%22%3A1%2C%22wh_pid%22%3A214753%2C%22x_pvid%22%3A%22655be9dc-8166-4bb9-ba31-e36c66c0ad7d%22%2C%22scm%22%3A%221007.12144.167873.11865844_0_0%22%2C%22x_object_id%22%3A625800201188%2C%22tpp_buckets%22%3A%222144%230%23167873%230%22%7D'
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36 Edg/87.0.664.60"}
    root_pattern = re.compile('<li id="[\s\S]*?" class="J_KgRate_ReviewItem kg-rate-ct-review-item" tabindex="0">[\s\S]*? </li>')

    def __contant(self):
        r = requests.get(url=taobao.url,headers=taobao.headers)
        R = r.text
        return R

    def __analy(self,R):
        root_html = re.findall(taobao.root_pattern,R)
        return root_html


    def go(self):
        R = self.__contant()
        result_analy = self.__analy(R)
        print(result_analy)



result = taobao()
result.go()
