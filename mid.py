# While input an ID of a star, crawl all movies' ID from for further use
from lxml import etree
import requests
import time

ID_list = []
head = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36"
}
# three websites, maybe unaccessible sometimes, fill the accessible ones here
avmoo = 'https://javmoo.net'
avsox = 'https://javfee.com'
avmemo = 'https://avxo.club'


def get(link):
    # do a delay to prevent from being baned
    time.sleep(1)
    return requests.get(avmoo + link, headers=head)


# default link of the star links to AIKA; page 1
def op(link='/cn/star/2t4/page/', page=1):
    print("Now crawling page " + str(page) + " ...")
    # get response
    r = get(link + str(page))
    # besure it's ok for the response
    if r.status_code == 200:
        sel = etree.HTML(r.text)
        # get the IDs of the movies
        IDs = sel.xpath('//*[@id="waterfall"]/div/a/div[2]/span/date[1]/text()')
        for i in range(IDs.__len__()):
            ID_list.append(IDs[i])
        # get nextpage to determine whether to stop
        next = sel.xpath('/html/body/div[5]/ul/li/a/@name')
        # if there's a nextpage, go on
        if 'nextpage' in next:
            page += 1
            op(link, page)
        # else that's the end of the page, all is done
        else:
            print("all is done")
            print("Total " + str(page) + " pages")


# 2t4 is the ID of AIKA
def run(sh='2t4'):
    link = '/cn/star/' + sh + '/page/'
    op(link)
    # after operation, print the list of ID to the screen
    print(ID_list)
    print("Finish!")
    # show how many movies the star played a role in
    print(ID_list.__len__())


if __name__ == "__main__":
    # input the ID of star manually, default star is 2t4(AIKA)
    sh = input('Input the num(default 2t4)')
    if sh == '':
        run()
    else:
        run(sh)
