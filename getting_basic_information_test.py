import requests
from bs4 import BeautifulSoup
import time
import company_config

print("page scrapping start")

element_per_page = 25
page_count = 4

TARGET_URL = f"https://www.aladin.co.kr/search/wsearchresult.aspx?SearchTarget=Book&KeyRecentPublish=0&PublisherSearch=%EC%8B%9C%EA%B3%B5%EC%82%AC%28%EB%A7%8C%ED%99%94%29%408484&OutStock=0&ViewType=Detail&SortOrder=5&CustReviewCount=0&CustReviewRank=0&KeyWord=&CategorySearch=&chkKeyTitle=&chkKeyAuthor=&chkKeyPublisher=&chkKeyISBN=&chkKeyTag=&chkKeyTOC=&chkKeySubject=&ViewRowCount={element_per_page}&SuggestKeyWord=&page={page_count}"


headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}


try:
    while True:

        response = requests.get(TARGET_URL, headers=headers)
        response.raise_for_status() 

        print(f"page{page_count} connection success")

        soup = BeautifulSoup(response.text, "html.parser")

        book_boxes = soup.select(".ss_book_box") 

        if book_boxes:
            print(f"\n found {len(book_boxes)-1} book boxes")
            
            for i in range(len(book_boxes)-1):
                print(f"\n book {i + 1}")
                print(str(book_boxes[i].get('itemid')))
                print(book_boxes[i].select_one(".bo3").text.strip())
                print(company_config.by_title(book_boxes[i].select_one(".bo3").text.strip()))
                time.sleep(5)
        
        else:
            print("'.ss_book_box' 요소를 찾을 수 없습니다.")
            print("사이트 구조가 변경되었거나 선택자가 잘못되었을 수 있습니다.")
        
        page_count += 1

except requests.exceptions.RequestException as e:
    print(f"사이트 접속 중 에러 발생: {e}")
except Exception as e:
    print(f"데이터 처리 중 에러 발생: {e}")

