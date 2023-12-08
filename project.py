
#Usecase-1 Load all three csv datasets in Pandas Data frames and display first 5 records

[ ]
ls
account_circle
sample_data/
[ ]
from google.colab import files
[ ]
data = files.upload()
account_circle

[ ]
import pandas as pd
[ ]
df_customers = pd.read_csv('customers.csv')
df_customers.head()
account_circle

[ ]
df_products = pd.read_csv('products.csv')
df_products.head()
account_circle

[ ]
transactions_list = ['txnno','txndate','custno','amount','productno','spendby']
df_transactions = pd.read_csv('transactions.csv',names=transactions_list)
df_transactions.head()
account_circle

Usecase-2 Display only those customers from CSV_s1, who purchased more than 3 products

[ ]
df_1 = pd.merge(df_customers,df_transactions,left_on="'custno'" , right_on='custno')
df_1.head(2)
account_circle

[ ]
df_2 = df_1.groupby('custno').count()
df_2.head(10)
account_circle

[ ]
df_2[df_2["'custno'"] > 3]
account_circle

[ ]
dataf = df_2 [ df_2['txnno'] > 3]
finaldata = pd.DataFrame(dataf)
finaldata
account_circle

[ ]
df_1 = pd.merge(df_customers,df_transactions,left_on="'custno'" , right_on='custno' ) # merge customer and transaction df
df_2 = df_1.groupby('custno').count() # group all records related to same custno in same group and check count
df_3 = df_customers.set_index("'custno'") # set custno as index
df_3['Product_purchased'] = df_2['txnno'] # add purchase count (count of transactions ) column in customer df
df_3[df_3['Product_purchased']>3] # filter out records based on count
account_circle

[ ]
df_1.corr()
account_circle

Usecase-8 Load all three PSV (pipe separated values) dataset in Pandas Data frames and display first 5 records.

[ ]
customers_list = ['custno','firstname','lastname','gender','age','profession','contactNo',
'emailId','city','state','isActive','createdDate','UpdatedDate']
df_customers_psv = pd.read_csv('customers.txt',names=customers_list,delimiter='|')
df_customers_psv.head(2)
account_circle

[ ]
products_list = ['productno','productName','Description','isActive','createdDate','UpdatedDate']
transactions_list = ['txnno','txndate','custno','amount','productno','spendby']
df_products_psv = pd.read_csv('products.txt',names=products_list,delimiter='|')
df_transactions_psv = pd.read_csv('transactions.txt',names=transactions_list,delimiter='|')
[ ]
df_transactions_psv.head(2)
account_circle

[ ]
df_transactions_psv['spendby'].unique()
account_circle
array(['Card', 'Cash'], dtype=object)
[ ]
df_products_psv.head(2)
account_circle

[ ]
import seaborn as sns
# sns.countplot(data=df_transactions_psv,x='spendby')
import matplotlib.pyplot as plt
plt.scatter(df_transactions_psv['amount'],df_transactions_psv['spendby'])
account_circle

[ ]
df_transactions_psv.corr()
account_circle

Usecase-9 Load all three JSON datasets in Pandas Data frames and display first 5 records.

[ ]
df_customers_json = pd.read_json('customers.json',lines=True)
df_customers_json.head()
account_circle

[ ]
df_products_json = pd.read_json('products.json',lines=True)
df_products_json.head()
account_circle

[ ]
df_transactions_json = pd.read_json('transactions.json',lines=True)
df_transactions_json.head()
account_circle

Usecase-10 Load all three XML datasets in Pandas Data frames and display first 5 records.

[ ]
df_customers_xml = pd.read_xml('customers.xml')
df_customers_xml.head()
account_circle

Usecase-3 Display top 5 most demanded products from CSV_s1

[ ]
df_4 = pd.merge(df_products,df_transactions,left_on="'productno'",right_on='productno')
df_5 = df_4.groupby('productno').count()
df_6 = df_products.set_index("'productno'")
df_6['Product_Sold'] = df_5['custno']
df_6.sort_values(by='Product_Sold',ascending=False).head()
account_circle

Usecase-4 Display top 5 transactions amount from CSV_s1

[ ]
df_7 = df_transactions.sort_values('amount',ascending=False)
df_7['amount'].head()
account_circle
556    4996
305    4992
574    4981
531    4980
232    4966
Name: amount, dtype: int64
[ ]
df_7.info()
account_circle
<class 'pandas.core.frame.DataFrame'>
Int64Index: 1000 entries, 556 to 787
Data columns (total 6 columns):
 #   Column     Non-Null Count  Dtype 
---  ------     --------------  ----- 
 0   txnno      1000 non-null   int64 
 1   txndate    1000 non-null   object
 2   custno     1000 non-null   int64 
 3   amount     1000 non-null   int64 
 4   productno  1000 non-null   int64 
 5   spendby    1000 non-null   object
dtypes: int64(4), object(2)
memory usage: 54.7+ KB
Usecase-5 Display distinct professions from CSV_s1

[ ]
df_customers["'profession'"].unique()
account_circle
array(['B', 'S'], dtype=object)
[ ]
df_customers["'profession'"].value_counts()
account_circle
B    500
S    500
Name: 'profession', dtype: int64
Usecase-6 Display highest age in CSV_s1 customer’s dataset

[ ]
df_customers["'age'"].max()
account_circle
64
Usecase-7 Display custno, gender, age, profession, contactno, productno, productName, txndate, spendby, amount from CSV_s1 for custno = 923

[ ]
print('customers columns: ',df_customers.columns)
print('transactions columns: ',df_products.columns)
print('products columns: ',df_transactions.columns)
account_circle
customers columns:  Index([''custno'', ''firstname'', ''lastname'', ''gender'', ''age'',
       ''profession'', ''contactNo'', ''emailId'', ''city'', ''state'',
       ''isActive'', ''createdDate'', ''UpdatedDate''],
      dtype='object')
transactions columns:  Index([''productno'', ''productName'', ''Description'', ''isActive'',
       ''createdDate'', ''UpdatedDate''],
      dtype='object')
products columns:  Index(['txnno', 'txndate', 'custno', 'amount', 'productno', 'spendby'], dtype='object')
Usecase-7 Display custno, gender, age, profession, contactno, productno, productName, txndate, spendby, amount from CSV_s1 for custno = 923

[ ]
df_8 = pd.merge(df_products[["'productno'","'productName'"]],df_transactions,left_on="'productno'",right_on='productno')
df_9 = pd.merge(df_customers,df_8,left_on="'custno'" , right_on='custno')
df_10 = df_9[df_9['custno'] == 923]
df_10[['custno', "'gender'", "'age'", "'profession'", "'contactNo'", 'productno', "'productName'",'txndate', 'spendby', 'amount']]
account_circle














