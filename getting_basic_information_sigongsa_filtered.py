import requests
from bs4 import BeautifulSoup
import time
import company_config
import csv

print("page scrapping start")

element_per_page = 50
page_count = 1

attributes = ['itemid', 'title']
file_name = 'sigongsa_all_basic_info_filtered.csv'

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

        excluding_title = ['간츠', '이토준지','이토 준지', '로어 올림푸스', '스킵 비트', '로보트', '코코', '천년귀검', '폭풍열차', '프랑켄슈타인', '백귀야행', '번개 기동대', '소리사의', '굴뚝새', '천공의', '간츠','세상이 가르쳐 준 비밀', '논짱과 아카리', '도로헤도로', '묵공', '마법사의 아들 코리', '스킵 비트', '불쾌한 구멍', '로보트 킹', '시오리와', '김형배', '소림사의 바람', 'Feel So Good', '마법사의 아들 코리', '대다크', '바탈리온', '복제인간', 'I 아이', '워킹맘', '요괴헌터 히에다의 제자들', '소이치의 저주 일기', '소용돌이 합본판', '붉은 눈', '머리 없는 조각상', '고유성 SF 단편선 시리즈 - 전10권', '토미에', '이볼 EVOL', '미미의 괴담 완전판', '신음하는 배수관', '선셋 로즈', '지옥별 레미나', '우주 패트롤', '고유성 SF 스페셜 에디션 세트 - 전23권', '전자인간 337', '뒷골목', '곳간이 있는 집','보위', '탈주병이 있는 집', '파검', '궤담', '장태산 무협 시리즈 세트', '150cm', '블랙 패러독스','마의 파편', '토미에', '150cm 라이프', '궤담', '묘비 마을','우리 부모님을 어떻게 할까요?','트루데 부인', '사자의 상사병', '센서'] 

        excluding_set = set(excluding_title)

        if book_boxes:
            print(f"found {len(book_boxes)} book boxes")
            
            for i in range(len(book_boxes)):
                current_title = book_boxes[i].select_one(".bo3").text.strip()
                is_excluded = any(exclude_word in current_title for exclude_word in excluding_set)
                if is_excluded:
                    continue
                else: 
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