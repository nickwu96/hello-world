import requests
import xlwt
from bs4 import BeautifulSoup
import datetime

# 这是一个自动抓取当当网近7日畅销书的爬虫程序，抓取后自动保存为以当前日期时间命名的excel中

def time():
    now_time = datetime.datetime.now().strftime('%G-%m-%d_%H%M%S')
    return now_time

def write_to_excel(books):  # 写入数据至excel中
    # 创建一个workbook 设置编码
    workbook = xlwt.Workbook(encoding='utf-8')
    # 创建一个worksheet
    worksheet = workbook.add_sheet('Dangdang_Top_Books')
    label = ['序号', '书名', '评论数', '推荐', '作者', '出版日期', '出版商', '现价格', '原价格', '折扣']

    # 首先生成第一行表头
    for i in range(10):
        worksheet.write(0, i, label[i])

    # 输出其他数据
    for i in range(len(books)):
        for j in range(len(books[i])):
            try:
                worksheet.write(i + 1, j, books[i][j])
            except:
                pass

    workbook.save('{}.xls'.format(time()))
    return None


def website_analysis(url):
    books = []
    req = requests.get(url=url)
    soup = BeautifulSoup(req.text, 'html.parser')

    for i in soup.find_all('li'):
        if i.find(class_='list_num'):
            num = i.find('div', class_='list_num').string[:-1]
            book_name = i.find('div', class_='name').a.attrs['title']
            remarks = i.find('div', class_='star').a.string
            recommend = i.find('span', class_='tuijian').string
            for j in i.find_all('div', class_='publisher_info'):
                if j.contents[0].name == 'span':
                    publish_time = j.span.string
                    publisher = j.contents[2].string
                else:
                    author = j.a.attrs['title']
            price_new = i.find('span', class_='price_n').string  # 现价格
            price_old = i.find('span', class_='price_r').string  # 原价格
            price_discount = i.find('span', class_='price_s').string  # 折扣
            books.append([num, book_name, remarks, recommend, author, publish_time, publisher, price_new, price_old,
                          price_discount])
    return books


if __name__ == '__main__':
    books = []
    for i in range(25):
        print('正在读取第{}页'.format(i + 1))
        books += website_analysis(
            url='http://bang.dangdang.com/books/bestsellers/01.00.00.00.00.00-recent7-0-0-1-{}'.format(i + 1))
    write_to_excel(books)
