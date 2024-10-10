# 데이터프레임 만들기
import pandas as pd 

data = {'이름' : ['Kim', 'Park', 'Lee', 'Ho'],
        '국어' : [90, 58, 88, 100],
        '영어' : [100, 60, 80, 70],
        '수학' : [55, 65, 76, 88] }

# 데이터프레임 출력
print("1> ---------------------------------")
df = pd.DataFrame(data) 
print(df, end='\n\n')

# '이름' 열 추출
print("2> ---------------------------------")
sr_name = df['이름']
print(sr_name, end='\n\n')

# 'Park'데이터 추출
print("3> ---------------------------------")
park_data = df.loc[1]
park_data = df.loc[df['이름'] == 'Park']
print(park_data, end='\n\n')

# 'Ho' 수학 점수 88 > 90 수정
print("4> ---------------------------------")
df.loc[df['이름'] == 'Ho', '수학'] = 90
print(df, end='\n\n')

# 'Oh'의 데이터 추가
print("5> ---------------------------------")
df.loc[3] = ['Oh', 100, 70, 80]
print(df, end='\n\n')

# 'Lee' 데이터 삭제 (열 2)
print("6> ---------------------------------")
df.drop([2], axis=0)
print(df, end='\n\n')
