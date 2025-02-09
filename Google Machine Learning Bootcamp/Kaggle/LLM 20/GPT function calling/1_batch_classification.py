import json
import os
import time
from datetime import datetime

import dotenv
import pandas as pd
from openai import OpenAI

# model = "gpt-4o"
model = "gpt-4o-mini"
keywords_path = "data/keywords.csv"
categories_path = f"data/categories_from_{model}.csv"
keywords_df = pd.read_csv(keywords_path)
categories = pd.read_csv(categories_path).columns.to_list()

# print(keywords_df['keyword'][:5])
# print(categories[:5])

############################################################
system_prompt = '''The goal is to determine if a keyword belongs to a category. Given a keyword and category list, 
the following JSON object is output: `{ categories_yn: string[] // Array of whether it belongs to each category or not 
}` Note that the `categories_yn` array element can only be `y` or `n`, and that the array size must be 20.'''

############################################################
# Creating an array of json tasks

tasks = []

for index, line in keywords_df.iterrows():
    keyword = line['keyword']

    task = {
        "custom_id": f'{index}',
        "method": "POST",
        "url": "/v1/chat/completions",
        "body": {
            "model": model,
            "temperature": 0.1,
            "response_format": {
                "type": "json_object"
            },
            "messages": [
                {
                    "role": "system",
                    "content": system_prompt
                },
                {
                    "role": "user",
                    "content": f'keyword: {keyword}, categories: {categories}'
                }
            ],
        }
    }
    # print(task)
    tasks.append(task)

############################################################
# Create an OpenAI client

dotenv.load_dotenv()
client = OpenAI()

############################################################
# Creating a batch tasks file

batch_tasks_file_name = "data/batch_tasks.jsonl"
with open(batch_tasks_file_name, 'w') as file:
    for task in tasks:
        file.write(json.dumps(task) + '\n')

############################################################
# Uploading the batch tasks file

batch_file = client.files.create(
    file=open(batch_tasks_file_name, "rb"),
    purpose="batch"
)
print(batch_file)

############################################################
# Creating the batch job

batch_job = client.batches.create(
    input_file_id=batch_file.id,
    endpoint="/v1/chat/completions",
    completion_window="24h"
)
print(batch_job)

############################################################
# Checking the batch status

batch_job_id = batch_job.id

while batch_job.output_file_id is None and batch_job.errors is None:
    batch_job = client.batches.retrieve(batch_job_id)
    print(f'## output_file_id: {batch_job.output_file_id}, errors: {batch_job.errors}')

    if batch_job.output_file_id is None and batch_job.errors is None:
        print("---- Current Time:", datetime.now())
        # Sleep for 1 minute (60 seconds)
        time.sleep(60)

############################################################
# Retrieving results

result_file_id = batch_job.output_file_id # 예시: 'file-87wNVt8YwigtVZJ24EGIoLWI'

if result_file_id:
    result = client.files.content(result_file_id).content
    result_file_name = f"data/batch_job_results_{model}.jsonl"

    with open(result_file_name, 'wb') as file:
        file.write(result)

    print(f"\nCreated a file: data/batch_job_results_{model}.csv")
