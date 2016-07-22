

# main 函数
import html_downloader
import html_output
import html_parser
import url_manager


class SpiderMain(object):
    def __init__(self):
        self.urls = url_manager.UrlManager()
        self.downloader = html_downloader.HtmlDownloader()
        self.parser = html_parser.HtmlParser()
        self.outputer = html_output.HtmlOutput()


    # 爬虫的调度程序
    def craw(self, root_url):
        count = 1
        self.urls.add_new_url(root_url)                 # 入口url 加入管理器

        while self.urls.has_new_url():
            try:
                new_url = self.urls.get_new_url()  # 获取个新的
                print('craw %d :%s' % (count, new_url))
                html_count = self.downloader.download(new_url)  # 下载这个页面数据
                new_urls, new_data = self.parser.parse(new_url, html_count)  # 解析这个页面数据
                self.urls.add_new_urls(new_urls)  # url 添加到url管理器
                self.outputer.collect_data(new_data)  # 收集数据

                if count == 250:
                    break
                count = count + 1

            except:
                print("craw failed")

        self.outputer.output_html()                # 输出


if __name__ == "__main__":
    root_url = 'http://baike.baidu.com/view/21087.htm'
    obj_spider = SpiderMain()
    obj_spider.craw(root_url)
