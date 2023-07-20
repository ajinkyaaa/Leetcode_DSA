import pandas as pd
import db2
 
class DB2Connect:
    def __init__(self) -> None:
        pass
    

    def getConnection(self):
        conn = db2.connect("connection string")

        return conn
    
    def getResult(self):
        conn = self.getConnection()
        data = conn.query("select * from ABC as A where A.name = 'AJ'")
        df = pd.DataFrame(data)
        return df

# df["name"]
"""
df[df["name"] == "AJ"]
[
    {
        name:AJ,
        age:4
    }
    ,
       {
        name:ak,
        age:5
    } 
]

2 files merge into 1

file a
name   age    loc   
Aj      3       5
ak      5       7


file b
name    age    loc
ram     7       2

# 

"""

import fileinput

def mergeFiles(fileA,fileB):
    
    with file.open(fileA):
        arr = []
        for i in fileA:
            arr.append("data") 

        df1 = pd.DataFrame(arr)

    with file.open(fileB):
        arr = []
        for i in fileA:
            arr.append("data") 

        df2 = pd.DataFrame(arr)
    
    df3 = df1.union(df2)



