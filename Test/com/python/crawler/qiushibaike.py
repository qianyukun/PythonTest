# -*- coding:utf-8 -*-
import urllib
import urllib2
import bs4
import cookielib


class QSBK:
    def __init__(self):
        self.page_index = 1
        self.user_agent = 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Mobile Safari/537.36'
        self.headers = {'User-Agent': self.user_agent,
                        # "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
                        # "Accept-Encoding":"gzip, deflate, br",
                        # "Accept-Language":"zh-CN,zh;q=0.9,en;q=0.8",
                        # "Cache-Control":"max-age=1",
                        # "Connection":'keep-alive',
                        # "Host":"www.qiushibaike.com",
                        # "Upgrade-Insecure-Requests":"1",
                        }
        # self.cookie = None

    def getPage(self, page_index):
        url = 'http://www.qiushibaike.com/hot/'
        if page_index != 1:
            url = url + '?page=' + str(page_index)
        print url
        try:

            request = urllib2.Request(url, headers=self.headers)
            response = urllib2.urlopen(request)
            print request.headers
            print '---------------------'
            content = response.read().decode('utf-8')

            soup = bs4.BeautifulSoup(content, "html.parser")
            print soup.original_encoding

            print '-------------'
            for article in soup.find_all("article"):
                print 'next ---------'
                print 'step___1_______'

                article_username = article.find('a', "username")
                if article_username is not None:
                    print article_username
                    print article_username.contents
                else:
                    continue

                article_content = article.find('a', "text")
                if article_content is not None:
                    print article_content
                    print article_content.contents
                else:
                    continue

                article_fullArticle = article.find('span', "fullArtitle")
                if article_fullArticle is not None:
                    print article_fullArticle
                    print article_fullArticle.contents
                    continue

                print ' \n\n\n\n\n'

        except urllib2.URLError, e:
            if hasattr(e, "code"):
                print e.code
            if hasattr(e, "reason"):
                print e.reason
            return -1
        return 1

    def getNextPage(self):
        page = 1
        code = self.getPage(page)
        # while code:
        #     page += 1
        #     code = self.getPage(page)

    def start(self):
        self.getNextPage()


spider = QSBK()
spider.start()
