import pandas as pd
from bs4 import BeautifulSoup
import os
from cst import db
import sqlite3

def df_from_didl_soup(soup):
    resource_metadata = soup.find('srw_dc:dcx')

    to_obtain = [('title', 'dc:title', {}),
                 ('PPN', 'dc:identifier', {'xsi:type': "dcx:PPN"}),
                 ('publication_date', 'dc:date', {}),
                 ('publisher', 'dc:publisher', {}),
                 ('record_id', 'dcx:recordIdentifier', {}),
                 ('collection_id', 'dcterms:isPartOf', {'xsi:type': "dcx:collectionIdentifier"}),
                 ('language', 'dc:language', {})
                 ]
    return {item: resource_metadata.find(element_name, attrs=attributes).text
                         for (item, element_name, attributes) in to_obtain}

def ingest_from_directory(dir_path, replace = False):
    all_metadata = []
    for fn in os.listdir(dir_path):
        if not os.path.isfile(os.path.join(dir_path, fn)) or not fn.endswith('.xml'):
            print(f'Skip {fn}')
            continue
        with open(os.path.join(dir_path, fn), "r", encoding="utf8") as f:
            didl_soup = BeautifulSoup("".join(f.readlines()), "xml")
            all_metadata.append(df_from_didl_soup(didl_soup))
    df = pd.DataFrame(all_metadata)
    to_db(df,'document', replace = replace)
    #with db.get_db() as con:
    #    df.to_sql("document",con, if_exists='replace' if replace else 'append')




def to_db(df, table_name, db = 'instance/cst.sqlite', replace = False):
    with sqlite3.connect(db) as con:
        df.to_sql(table_name, con, if_exists='replace' if replace else 'append')
    print(f"Pushed {len(df)} entries to table {table_name}.")




if __name__ == '__main__':

    df = ingest_from_directory('dataprocessing/harvested_data/metadata', replace=True)
