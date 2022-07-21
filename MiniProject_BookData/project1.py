import bs4
import urllib.request
import xlsxwriter
import time
import datetime
import random
## 함수 선언부
def getBookInfo(book_tag) : #도서 데이터 추출 : 엣지 브라우저의 [개발자 도구]를 사용하여 크롤링할 페이지의 정보를 추출함.
    names = book_tag.find("div", {"class": "goods_name"})
    bookName = names.find("a").text
    auths = book_tag.find("span", {"class": "goods_auth"})
    bookAuth = auths.find("a").text
    bookPub = book_tag.find("span", {"class": "goods_pub"}).text
    bookDate = book_tag.find("span", {"class": "goods_date"}).text
    bookPrice = book_tag.find("em", {"class": "yes_b"}).text
    return [bookName, bookAuth, bookPub, bookDate, bookPrice]

## 전역 변수 부분
url = "http://www.yes24.com/24/Category/More/001001003?ElemNo=104&ElemSeq=7&PageNumber="
folderName = 'C:/yes24/'
wsName = 'IT 서적 순위'
header = ['순위', '책이름', '저자', '출판사', '출간일', '가격']

## 메인 코드부
while True :
    print()
    print("--------------------")
    now = datetime.datetime.now() #현재 시간 정보 now 변수에 저장
    print('Yes24.com IT 서적 순위 크롤링  --> ', now.strftime('%Y-%m-%d %H:%M:%S'), ) #원하는 포맷으로 출력.
    filename = folderName + 'yes24_' + now.strftime('(%Y년%m월%d일%H시%M분%S초)')+'.xlsx' #지정한 폴더명에 yes24_연월일시분초.xlsx 로 저장됨

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
                print(rowNum, info_list)
                rowNum += 1

        except :
            break

    print(filename, '으로 저장됨.')
    print("--------------------")
    time.sleep(60) # 1일에 해당하는 초(60초*60분*24시), 정보를 하루 간격으로 크롤링하도록 작성.
