import os
from google.cloud import bigquery
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = '/Users/kay/Downloads/vaccinated-indonesia-f903e135261c.json'


# Perform a query.
def query_dataset():
    client = bigquery.Client()
    bigquery_job=client.query("""
SELECT date, country_code, cumulative_persons_fully_vaccinated
FROM `bigquery-public-data.covid19_open_data.covid19_open_data` 
where date = '2022-06-01'
and country_code = 'ID'
and cumulative_persons_fully_vaccinated IS NOT NULL
group by date, country_code, cumulative_persons_fully_vaccinated
LIMIT 50
"""
    )
    results = bigquery_job.result()
    for i in results:
        print(i.cumulative_persons_fully_vaccinated)

if __name__=="__main__":
    query_dataset()