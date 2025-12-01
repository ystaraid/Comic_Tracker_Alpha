import csv

# 파일 이름과 리스트 변수 정의
sigongsa_all_basic_info_filtered_file = 'sigongsa_all_basic_info_filtered.csv'
sigongsa_all_basic_info_filtered = []

attributes = ['itemid', 'title']
file_name = 'sigongsa_all_single_book_basic_info_filtered.csv'

# 2. sigongsa_all_basic_info_filtered.csv 파일 로드 (누락된 부분 추가)
try:
    with open(sigongsa_all_basic_info_filtered_file, mode='r', newline='', encoding='utf-8') as file:
        reader = csv.reader(file)
        for row in reader:
            sigongsa_all_basic_info_filtered.append(row)
    print("sigongsa_all_basic_info_filtered loaded")
except FileNotFoundError:
    print(f"{sigongsa_all_basic_info_filtered_file} not found")  

excluding_title = ['세트', '묶음', '박스', '이슈', '원샷', '백과사전', '무비 가이드', '고담 시티 투어'] 
excluding_set = set(excluding_title)

sigongsa_all_basic_info_filtered_title = []
sigongsa_all_basic_info_filtered_itemid = []
for row in sigongsa_all_basic_info_filtered:
    if len(row) > 1:
        current_title = row[1]
        is_excluded = any(exclude_word in current_title for exclude_word in excluding_set)
        if is_excluded:
            continue
        else: 
            sigongsa_all_basic_info_filtered_itemid.append(row[0])
            sigongsa_all_basic_info_filtered_title.append(row[1])

with open(file_name, mode='w', newline='', encoding='utf-8') as file:
    writer = csv.DictWriter(file, fieldnames=attributes)
    writer.writeheader()
    for row_tuple in zip(sigongsa_all_basic_info_filtered_itemid, sigongsa_all_basic_info_filtered_title):
        row_dict = dict(zip(attributes, row_tuple))
        writer.writerow(row_dict)

print(f"{file_name} created.")

