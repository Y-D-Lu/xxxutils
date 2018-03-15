import re
from lxml import etree, html
import requests
import time
head = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                  "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36",
}


def get(link):
    # the anti-crawling strategy of the website is so aggressive so a delay is essential
    time.sleep(1)
    print(link)
    return requests.get(link, headers=head)


def run(sh,page=1,order=0,classify=0):
    # get magnet links from alicili.pw
    r = get('http://alicili.pw/list/' + sh + '/' + str(page) + '-' + str(order) + '-' + str(classify) + '/')
    if r.status_code == 200:
        sel = etree.HTML(r.text)
        s = html.fromstring(r.text)
        # the total numbers of the result
        tot = (sel.xpath('/html/body/div[1]/div[2]/div/div[2]/a[1]/text()')[0].split('(')[1].split(")")[0])
        # get total pages of the result
        pages = (sel.xpath('/html/body/div[1]/div[2]/div/div[4]/span/text()')[0])
        # get the num of pages
        count = int(re.sub("\D", "", pages))
        # get names of the result
        name = (s.xpath('/html/body/div[1]/div[2]/div/dl/dt/a'))
        # get sizes of the result
        size = (sel.xpath('/html/body/div[1]/div[2]/div/dl/dd[1]/span[2]/b/text()'))
        # get magnet links for further use
        link = (sel.xpath('/html/body/div[1]/div[2]/div/dl/dd[1]/span[6]/a/@href'))
        # get numbers of files in a item
        num = (sel.xpath('/html/body/div[1]/div[2]/div/dl/dd[1]/span[3]/b/text()'))

        for i in range(size.__len__()):
            print(name[i].text_content())
            print("size : " + size[i])
            print("file_num : " + num[i])
            print(link[i])
        print("\nthere's " + str(count) + " pages and page " + str(page) + " is showed here\n")
        print("Showed "+str(size.__len__())+" of "+tot)
    # if it does not work correctly, print the error code
    else:
        print(r.status_code)
    print("finish")


if __name__ == "__main__":
    sh = input('Input the keyword')
    if sh == '':
        run('磁力')
    else:
        run(sh)
