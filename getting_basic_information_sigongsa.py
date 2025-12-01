import requests
from bs4 import BeautifulSoup
import time
import company_config
import csv

print("page scrapping start")

element_per_page = 50
page_count = 1

attributes = ['itemid', 'title']
file_name = 'sigongsa_all_basic_info.csv'

TARGET_URL = f"https://www.aladin.co.kr/search/wsearchresult.aspx?SearchTarget=Book&KeyRecentPublish=0&PublisherSearch=%EC%8B%9C%EA%B3%B5%EC%82%AC%28%EB%A7%8C%ED%99%94%29%408484&OutStock=0&ViewType=Detail&SortOrder=5&CustReviewCount=0&CustReviewRank=0&KeyWord=&CategorySearch=&chkKeyTitle=&chkKeyAuthor=&chkKeyPublisher=&chkKeyISBN=&chkKeyTag=&chkKeyTOC=&chkKeySubject=&ViewRowCount={element_per_page}&SuggestKeyWord=&page={page_count}"


headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}

itemid = []
title = []

for i in range (23):
    try:
        TARGET_URL = f"https://www.aladin.co.kr/search/wsearchresult.aspx?SearchTarget=Book&KeyRecentPublish=0&PublisherSearch=%EC%8B%9C%EA%B3%B5%EC%82%AC%28%EB%A7%8C%ED%99%94%29%408484&OutStock=0&ViewType=Detail&SortOrder=5&CustReviewCount=0&CustReviewRank=0&KeyWord=&CategorySearch=&chkKeyTitle=&chkKeyAuthor=&chkKeyPublisher=&chkKeyISBN=&chkKeyTag=&chkKeyTOC=&chkKeySubject=&ViewRowCount={element_per_page}&SuggestKeyWord=&page={page_count}"
        response = requests.get(TARGET_URL, headers=headers)
        response.raise_for_status() 

        print(f"page{page_count} connection success")

        soup = BeautifulSoup(response.text, "html.parser")

        book_boxes = soup.select(".ss_book_box") 
        book_boxes.remove(book_boxes[-1])

        if book_boxes:
            print(f"found {len(book_boxes)} book boxes")
            
            for i in range(len(book_boxes)):
                itemid.append(str(book_boxes[i].get('itemid')))
                title.append(book_boxes[i].select_one(".bo3").text.strip())
        
        else:
            print("'.ss_book_box' 요소를 찾을 수 없습니다.")
            print("사이트 구조가 변경되었거나 선택자가 잘못되었을 수 있습니다.")

        if len(book_boxes) != element_per_page:
            break
        
        page_count += 1

    except requests.exceptions.RequestException as e:
        print(f"사이트 접속 중 에러 발생: {e}")
    except Exception as e:
        print(f"데이터 처리 중 에러 발생: {e}")

title.reverse()
itemid.reverse()

with open(file_name, mode='w', newline='', encoding='utf-8') as file:
    writer = csv.DictWriter(file, fieldnames=attributes)
    writer.writeheader()
    for row_tuple in zip(itemid, title):
        row_dict = dict(zip(attributes, row_tuple))
        writer.writerow(row_dict)

print(f"{file_name} created.")