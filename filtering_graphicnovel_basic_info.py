import csv

graphicnovel_basic_info = []
sigongsa_basic_info = []
graphicnovel_basic_info_file = 'graphicnovel_all_basic_info.csv'
sigongsa_basic_info_file = 'sigongsa_all_basic_info.csv'

try:
    with open(graphicnovel_basic_info_file, mode='r', newline='', encoding='utf-8') as file:
        reader = csv.reader(file)
        for row in reader:
            graphicnovel_basic_info.append(row)

    print("list loaded")
    header = graphicnovel_basic_info[0]
    data_rows = graphicnovel_basic_info[1:]

except FileNotFoundError:
    print(f"{graphicnovel_basic_info_file} not found")  

try:
    with open(sigongsa_basic_info_file, mode='r', newline='', encoding='utf-8') as file:
        reader = csv.reader(file)
        for row in reader:
            sigongsa_basic_info.append(row)

    print("list loaded")
    header = sigongsa_basic_info[0]
    data_rows = sigongsa_basic_info[1:]

except FileNotFoundError:
    print(f"{sigongsa_basic_info_file} not found")  

graphic_novel_title = []
sigongsa_title = []
graphic_novel_itemid = []
sigongsa_itemid = [] 

for row in graphicnovel_basic_info:
    graphic_novel_title.append(row[1])
    graphic_novel_itemid.append(row[0])

for row in sigongsa_basic_info:
    sigongsa_title.append(row[1])
    sigongsa_itemid.append(row[0])

left_title = list(set(sigongsa_title) - set(graphic_novel_title))
# left_itemid = list(set(sigongsa_itemid) - set(graphic_novel_itemid))

def exclude_title(list, exclude_title):
    for exclude in exclude_title:
        for item in list:
            if exclude in item:
                list.remove(item)
    return list

def exclude_title_safe(data_list, exclude_list):
    exclude_set = set(exclude_list)
    return [
        item for item in data_list
        if not any(exclude in item for exclude in exclude_set)
    ]

excluding_title = ['간츠', '이토준지','이토 준지', '로어 올림푸스', '스킵 비트', '로보트', '코코', '천년귀검', '폭풍열차', '프랑켄슈타인', '백귀야행', '번개 기동대', '소리사의', '굴뚝새', '천공의', '간츠','세상이 가르쳐 준 비밀', '논짱과 아카리', '도로헤도로', '묵공', '마법사의 아들 코리', '스킵 비트', '불쾌한 구멍', '로보트 킹', '시오리와', '김형배', '소림사의 바람', 'Feel So Good', '마법사의 아들 코리', '대다크', '바탈리온', '복제인간', 'I 아이', '워킹맘', '요괴헌터 히에다의 제자들', '소이치의 저주 일기', '소용돌이 합본판', '붉은 눈', '머리 없는 조각상', '고유성 SF 단편선 시리즈 - 전10권', '토미에', '이볼 EVOL', '미미의 괴담 완전판', '신음하는 배수관', '선셋 로즈', '지옥별 레미나', '우주 패트롤', '고유성 SF 스페셜 에디션 세트 - 전23권', '전자인간 337', '뒷골목', '곳간이 있는 집','보위', '탈주병이 있는 집', '파검', '궤담', '장태산 무협 시리즈 세트', '150cm', '블랙 패러독스','마의 파편', '토미에', '150cm 라이프', '궤담', '묘비 마을','우리 부모님을 어떻게 할까요?','트루데 부인', '사자의 상사병', '센서'] 

result = exclude_title_safe(left_title, excluding_title)
print(result)
print(len(result))