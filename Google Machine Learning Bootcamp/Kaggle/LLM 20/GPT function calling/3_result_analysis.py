import pandas as pd
from matplotlib import pyplot as plt

# Load the data
model = "gpt-4o-mini"
result_file_name = f"data/classified_keywords_{model}.csv"
df = pd.read_csv(result_file_name, index_col=0)
print(df.head(3))

categories = df.columns

# 각 카테고리별로 'y'와 'n'의 개수 계산
category_counts = df[categories].apply(lambda x: x.value_counts()).T
print(category_counts)

# 그래프 크기 설정
plt.figure(figsize=(50, 30))

# 막대 그래프 그리기
category_counts.plot(kind='bar', stacked=True)

# 그래프 제목과 레이블 설정
plt.title('Category Distribution')
plt.xlabel('Categories')
plt.ylabel('Count')

# x축 레이블 회전
plt.xticks(rotation=45, ha='right')

# 범례 위치 조정
plt.legend(title='Value', bbox_to_anchor=(1.05, 1), loc='upper left')

# 그래프 레이아웃 조정
plt.tight_layout()

# 그래프 표시
plt.show()
