from faker import Faker
import pandas as pd
import random

# kr_KR말고도 원하는 언어 설정가능
fake = Faker("ko_KR")


data =[]
for _ in range(10):
    # 가짜 이름 생성
    fake_name = fake.name()
    # 가짜 성별 생성
    fake_gender = fake.random_element(elements=('Male', 'Female'))
    # 가짜 주소 생성
    fake_religion = fake.random_element(elements=("기독교", "불교" , "천주교"))
    # 가짜 전화번호 생성
    fake_nationality = fake.random_element(elements=("이스라엘", "한국", "중국", "미국"))
    # 가짜 이메일 생성
    fake_Age = random.randrange(10,30)
    
    data.append([fake_name, fake_gender,fake_religion,fake_nationality,fake_Age])


df = pd.DataFrame(data, columns=['Name', 'Gender', 'religion','nationality','Age'])

# 데이터프레임을 엑셀 파일로 저장
excel_filename = "fake_user.xlsx"
df.to_excel(excel_filename, index=False)


# ["이름","니이", "종교", "국적"]



