import bs4
import urllib.request
import xlsxwriter
import time
import datetime
import random
## 함수 선언부
def getBookInfo(book_tag) :
    names = book_tag.find("div", {"class": "goods_name"})
    bookName = names.find("a").text
    auths = book_tag.find("span", {"class": "goods_auth"})
    bookAuth = auths.find("a").text
    bookPub = book_tag.find("span", {"class": "goods_pub"}).text
    bookDate = book_tag.find("span", {"class": "goods_date"}).text
    bookPrice = book_tag.find("em", {"class": "yes_b"}).text
    return [bookName, bookAuth, bookPub, bookDate, bookPrice]

## 전역 변수부
url = "http://www.yes24.com/24/Category/More/001001003?ElemNo=104&ElemSeq=7&PageNumber="
folderName = 'C:/yes24/'
wsName = 'IT 서적 순위'
header = ['순위', '책이름', '저자', '출판사', '출간일', '가격']

## 메인 코드부
while True :
    print()
    print("--------------------")
    now = datetime.datetime.now()
    print('Yes24.com IT 서적 순위 크롤링  --> ', now.strftime('%Y-%m-%d %H:%M:%S'), )
    filename = folderName + 'yes24_' + now.strftime('(%Y년%m월%d일%H시%M분%S초)')+'.xlsx'

    workbook = xlsxwriter.Workbook(filename)
    worksheet = workbook.add_worksheet(wsName)
    cell_format1 = workbook.add_format()
    cell_format1.set_bold()
    cell_format1.set_font_color(random.choice(['red','green', 'blue', 'gray', 'magenta', 'cyan']))
    cell_format1.set_font_size(15)
    cell_format1.set_align('center')
    cell_format1.set_align('vcenter')
    cell_format1.set_bg_color('yellow')
    cell_format1.set_border(1)

    worksheet.set_column('A:F', 20)  # 약 0.34
    for i in range(len(header)) :
        worksheet.write(0, i, header[i], cell_format1)

    cell_format2 = workbook.add_format()
    cell_format2.set_border(1)

    pageNumber = 1
    rowNum = 1
    while True :
        try :
            bookUrl = url + str(pageNumber)
            pageNumber += 1

            htmlObject = urllib.request.urlopen(bookUrl)
            webPage = htmlObject.read()
            bsObject = bs4.BeautifulSoup(webPage, 'html.parser')
            tag = bsObject.find('ul', {'class': 'clearfix'})
            all_books = tag.findAll('div', {'class': 'goods_info'})

            for book in all_books:
                info_list = getBookInfo(book)
                worksheet.write(rowNum, 0, rowNum,  cell_format2)
                for i in range(len(info_list)) :
                    worksheet.write(rowNum, i+1, info_list[i], cell_format2)
                rowNum += 1

        except :
            break

    workbook.close()
    print(filename, '으로 저장됨.')
    print("--------------------")
    time.sleep(60*60*24) # 1일에 해당하는 초(60초*60분*24시)
