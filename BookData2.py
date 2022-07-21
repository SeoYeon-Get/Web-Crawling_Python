import bs4
import urllib.request

## 함수 선언부
def getBookInfo(book_tag) : #태그 찾고 데이터 추출하는 부분
    names = book_tag.find("div", {"class": "goods_name"}) 
    bookName = names.find("a").text 
    auths = book_tag.find("span", {"class": "goods_auth"})
    bookAuth = auths.find("a").text
    bookPub = book_tag.find("span", {"class": "goods_pub"}).text
    bookDate = book_tag.find("span", {"class": "goods_date"}).text
    bookPrice = book_tag.find("em", {"class": "yes_b"}).text
    return [bookName, bookAuth, bookPub, bookDate, bookPrice]

## 전역 변수부
url = "http://www.yes24.com/24/Category/Display/001001046001?ParamSortTp=05&PageNumber="
pageNumber = 1

## 메인 코드부
while True :
    try :
        bookUrl = url + str(pageNumber) # 페이지 넘어감
        pageNumber += 1

        htmlObject = urllib.request.urlopen(bookUrl)
        webPage = htmlObject.read()
        bsObject = bs4.BeautifulSoup(webPage, 'html.parser')
        tag = bsObject.find('ul', {'class': 'clearfix'})
        all_books = tag.findAll('div', {'class': 'goods_info'}) #html 코드에서 goods_info 클래스 태그를 찾아 all_books 리스트에 append

        for book in all_books: #리스트에서 도서 한권씩 정보 추출 -> getBookInfo함수 호출.
            print(getBookInfo(book))

    except :
        break
