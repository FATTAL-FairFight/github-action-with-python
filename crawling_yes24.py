import requests
from bs4 import BeautifulSoup


def parsing_beautifulsoup(url):
    """
    뷰티풀 수프로 파싱하는 함수
    :param url: paring할 URL. 여기선 YES24 Link
    :return: BeautifulSoup soup Object
    """

    data = requests.get(url)

    html = data.text
    return BeautifulSoup(html, 'html.parser')


def extract_book_data(soup):
    """
    BeautifulSoup Object에서 book data를 추출하는 함수
    :param soup: BeautifulSoup soup Object
    :return: contents(str)
    """
    upload_contents = ''
    new_books = soup.select(".goodsTxtInfo")  # 클래스 이름이나 요소 구조를 다시 확인하세요.
    url_prefix = "http://www.yes24.com"

    for new_book in new_books:
        # 새로운 HTML 구조에 맞게 요소 선택자를 수정
        book_name = new_book.select("a")[0].text.strip()  # 책 제목을 올바르게 가져옵니다.
        url_suffix = new_book.select("a")[0].attrs['href']  # href 속성을 정확하게 선택합니다.
        url = url_prefix + url_suffix
        price = new_book.select(".priceB")[0].text.strip()  # 가격 정보를 올바르게 가져옵니다.

        content = f"<a href={url}>" + book_name + "</a>" + ", " + price + "<br/>\n"
        upload_contents += content

    return upload_contents

