import requests
from bs4 import BeautifulSoup
import time
import company_config
import csv

print("page scrapping start")

element_per_page = 100
page_count = 1

attributes = ['itemid', 'title']
file_name = 'graphicnovel_all_basic_info.csv'

TARGET_URL = f"https://www.aladin.co.kr/shop/common/wseriesitem.aspx?ViewRowsCount={element_per_page}&ViewType=Detail&SortOrder=5&page={page_count}&Stockstatus=1&PublishDay=84&SRID=4046&CustReviewRankStart=&CustReviewRankEnd=&CustReviewCountStart=&CustReviewCountEnd=&PriceFilterMin=&PriceFilterMax=&SearchOption="


headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}

itemid = []
title = []

while True: 
    try:
        TARGET_URL = f"https://www.aladin.co.kr/shop/common/wseriesitem.aspx?ViewRowsCount={element_per_page}&ViewType=Detail&SortOrder=5&page={page_count}&Stockstatus=1&PublishDay=84&SRID=4046&CustReviewRankStart=&CustReviewRankEnd=&CustReviewCountStart=&CustReviewCountEnd=&PriceFilterMin=&PriceFilterMax=&SearchOption="
        response = requests.get(TARGET_URL, headers=headers)
        response.raise_for_status() 

        print(f"page{page_count} connection success")

        soup = BeautifulSoup(response.text, "html.parser")

        book_boxes = soup.select(".ss_book_box") 

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

itemid.reverse()
title.reverse()

with open(file_name, mode='w', newline='', encoding='utf-8') as file:
    writer = csv.DictWriter(file, fieldnames=attributes)
    writer.writeheader()
    for row_tuple in zip(itemid, title):
        row_dict = dict(zip(attributes, row_tuple))
        writer.writerow(row_dict)

print(f"{file_name} created.")

