import pyterrier as pt
import pandas as pd
import json

df = pd.read_csv('../data/us_con.csv')
df = df[:500].astype(str)
df = df.fillna('')

# PyTerrierを初期化
if not pt.started():
    pt.init()
# インデックスの作成
index_path = "./terrier_index" 
indexer = pt.DFIndexer(index_path, overwrite=True, blocks=True)

index_ref = indexer.index(df['product_title'], docno=df.index.astype(str).tolist())
index = pt.IndexFactory.of(index_ref)
print(index.getCollectionStatistics())

# assert 2 == index.getCollectionStatistics().getNumberOfFields()
# # BM25Fを使用して検索

query = "5"
bm25 = pt.BatchRetrieve(index, wmodel="BM25")#, controls={'w.0': 1.0, 'w.1': 1.0, 'c.0': 0.4, 'c.1': 0.4})

result = bm25.search(query)

# 検索結果の表示
print("BM25Fスコア:")
print(result)
