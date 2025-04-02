import pandas as pd
import requests as re
import pyodbc
from sqlalchemy import create_engine
import json
import logging

logging.basicConfig(filename="app.log",level=logging.INFO,format='%(asctime)s - %(levelname)s - %(message)s')
with open('json\\secrets.json') as f:
    secrets = json.load(f)

def create_csv():
    conn_srt = f'mssql+pyodbc://{secrets['USERNAME']}:{secrets['PASSWORD']}@{secrets['SERVER']}/{secrets['DATABASE']}?driver=ODBC+Driver+17+for+SQL+Server'
    engine = create_engine(conn_srt)
    logging.info("reading data from Customer...") 
    query = "select * from Customer" 
    df = pd.read_sql_query(query,engine) 
    logging.info("Loading data into leads.csv file...") 
    df.to_csv('csv\\leads.csv',index=False)


def hubspot_upsert():
    url = secrets['URL']
    headers = {'Authorization':f'Bearer {secrets['TOKEN']}'}
    with open('json\\mapping.json') as f:
        mappstring = f.read()
        payload = {'importRequest':mappstring}
    with open('csv\\leads.csv') as f:
        files = [('files',f)]
        pst = re.post(url,data=payload,files=files,headers=headers)
    print(pst.status_code)


if __name__ == '__main__':
    create_csv()
    hubspot_upsert()