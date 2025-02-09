import csv
import json

import pandas as pd

model = "gpt-4o-mini"
keywords_path = "data/keywords.csv"
categories_path = f"data/categories_from_{model}.csv"

keywords_df = pd.read_csv(keywords_path).drop(columns=['alts'])
categories = pd.read_csv(categories_path).columns.to_list()

############################################################
# Loading data from saved file

batch_result = []
result_file_name = "data/batch_job_results_gpt-4o-mini.jsonl"
with open(result_file_name, 'r') as file:
    for line in file:
        json_object = json.loads(line.strip())
        batch_result.append(json_object)

############################################################
# Reading only the first batch results
print('\n### Reading the batch results')
for res in batch_result[:5]:
    # Getting index from task id
    task_id = res['custom_id']
    index = task_id.split('-')[-1]
    result = res['response']['body']['choices'][0]['message']['content']
    categories_yn = json.loads(result)['categories_yn']
    print(categories_yn)
print('\n------------------------')

############################################################
# Result To CSV
classified_keywords = []

# Processing header row
header = keywords_df.columns.tolist() + categories
classified_keywords.append(header)

# Processing data rows
for index, keyword_line in keywords_df.iterrows():
    result = batch_result[index]['response']['body']['choices'][0]['message']['content']
    categories_yn = json.loads(result)['categories_yn']
    updated_line = keyword_line.tolist() + categories_yn
    classified_keywords.append(updated_line)

print('\n### Reading the classified keywords result')
for line in classified_keywords[:5]:
    print(line)

# 결과를 CSV 파일로 저장
classified_keywords_file_name = "data/classified_keywords_gpt-4o-mini.csv"

with open(classified_keywords_file_name, 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(classified_keywords)

print(f"\nCreated a file: data/classified_keywords_{model}.csv")
