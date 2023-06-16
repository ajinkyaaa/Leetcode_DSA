"""
cust1 (loanid) => name accnt
          Aj   123


cust2 (loanid) => name, accnt
                456


2nd dataframe, another dataframe = [{"name":"" , "accnt":456 ,"loanId":2 }]

"""

import pandas as pd


cust1 = {"name":"Aj" , "accnt":123 ,"loanId":2 }
cust2 = {"name":"Jv" ,"accnt":456 , "loanId":3 }



from collections import defaultdict
def merge(cust1,cust2):
    dic = defaultdict()
    dic[cust1["loanId"]] = cust1

    if cust2["loanId"] in dic:
        # iterate over each property and check if it exists, if yes then update if no then add
        for k in cust2.keys():
            if k in cust1:
                cust1[k] = cust2[k]
            else:
                cust1[k] = cust2[k]

    print(dic)
    return dic


merge(cust1,cust2)


json1 = [
    {"name":"Aj" , "accnt":123 ,"loanId":2 },
    {"name":"Jv" ,"accnt":456 , "loanId":3 }
]

json2 = []
df1 = pd.DataFrame(json1)
print(df1)

json2 = [{"name":"" , "accnt":456 ,"loanId":2 }]
df2 = pd.DataFrame(json2)
print(df2)

df3 = df1.merge(df2)
print(df3)

joinDf = pd.merge(df1,df2 ,on='loanId',how="left" )

print(joinDf)

print(joinDf.columns)

"""
for col in joinDf.columns:
    if "_x" in col:
        
"""

"""
  name  accnt  loanId    name2      accnt2    loandId2
0   Aj    123       2    ""         456       2
1   Jv    456       3 
"""