# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
from IPython import get_ipython

# %% [markdown]
# # Data Loading, Storage, 

# %%
import numpy as np
import pandas as pd
np.random.seed(12345)
import matplotlib.pyplot as plt
plt.rc('figure', figsize=(10, 6))
np.set_printoptions(precision=4, suppress=True)

# %% [markdown]
# ## Reading and Writing Data in Text Format

# %%
get_ipython().system('cat examples/ex1.csv')


# %%
df = pd.read_csv('examples/ex1.csv')
df


# %%
pd.read_table('examples/ex1.csv', sep=',')


# %%
get_ipython().system('cat examples/ex2.csv')


# %%
pd.read_csv('examples/ex2.csv', header=None)
pd.read_csv('examples/ex2.csv', names=['a', 'b', 'c', 'd', 'message'])


# %%
names = ['a', 'b', 'c', 'd', 'message']
pd.read_csv('examples/ex2.csv', names=names, index_col='message')


# %%
get_ipython().system('cat examples/csv_mindex.csv')
parsed = pd.read_csv('examples/csv_mindex.csv',
                     index_col=['key1', 'key2'])
parsed


# %%
list(open('examples/ex3.txt'))


# %%
result = pd.read_table('examples/ex3.txt', sep='\s+')
result


# %%
get_ipython().system('cat examples/ex4.csv')
pd.read_csv('examples/ex4.csv', skiprows=[0, 2, 3])


# %%
get_ipython().system('cat examples/ex5.csv')
result = pd.read_csv('examples/ex5.csv')
result
pd.isnull(result)


# %%
result = pd.read_csv('examples/ex5.csv', na_values=['NULL'])
result


# %%
sentinels = {'message': ['foo', 'NA'], 'something': ['two']}
pd.read_csv('examples/ex5.csv', na_values=sentinels)

# %% [markdown]
# ### Reading Text Files in Pieces

# %%
pd.options.display.max_rows = 10


# %%
result = pd.read_csv('examples/ex6.csv')
result


# %%
pd.read_csv('examples/ex6.csv', nrows=5)


# %%
chunker = pd.read_csv('examples/ex6.csv', chunksize=1000)
chunker


# %%
chunker = pd.read_csv('examples/ex6.csv', chunksize=1000)

tot = pd.Series([])
for piece in chunker:
    tot = tot.add(piece['key'].value_counts(), fill_value=0)

tot = tot.sort_values(ascending=False)


# %%
tot[:10]

# %% [markdown]
# ### Writing Data to Text Format

# %%
data = pd.read_csv('examples/ex5.csv')
data


# %%
data.to_csv('examples/out.csv')
get_ipython().system('cat examples/out.csv')


# %%
import sys
data.to_csv(sys.stdout, sep='|')


# %%
data.to_csv(sys.stdout, na_rep='NULL')


# %%
data.to_csv(sys.stdout, index=False, header=False)


# %%
data.to_csv(sys.stdout, index=False, columns=['a', 'b', 'c'])


# %%
dates = pd.date_range('1/1/2000', periods=7)
ts = pd.Series(np.arange(7), index=dates)
ts.to_csv('examples/tseries.csv')
get_ipython().system('cat examples/tseries.csv')

# %% [markdown]
# ### Working with Delimited Formats

# %%
get_ipython().system('cat examples/ex7.csv')


# %%
import csv
f = open('examples/ex7.csv')

reader = csv.reader(f)


# %%
for line in reader:
    print(line)


# %%
with open('examples/ex7.csv') as f:
    lines = list(csv.reader(f))


# %%
header, values = lines[0], lines[1:]


# %%
data_dict = {h: v for h, v in zip(header, zip(*values))}
data_dict

# %% [markdown]
# class my_dialect(csv.Dialect):
#     lineterminator = '\n'
#     delimiter = ';'
#     quotechar = '"'
#     quoting = csv.QUOTE_MINIMAL
# %% [markdown]
# reader = csv.reader(f, dialect=my_dialect)
# %% [markdown]
# reader = csv.reader(f, delimiter='|')
# %% [markdown]
# with open('mydata.csv', 'w') as f:
#     writer = csv.writer(f, dialect=my_dialect)
#     writer.writerow(('one', 'two', 'three'))
#     writer.writerow(('1', '2', '3'))
#     writer.writerow(('4', '5', '6'))
#     writer.writerow(('7', '8', '9'))
# %% [markdown]
# ### JSON Data

# %%
obj = """
{"name": "Wes",
 "places_lived": ["United States", "Spain", "Germany"],
 "pet": null,
 "siblings": [{"name": "Scott", "age": 30, "pets": ["Zeus", "Zuko"]},
              {"name": "Katie", "age": 38,
               "pets": ["Sixes", "Stache", "Cisco"]}]
}
"""


# %%
import json
result = json.loads(obj)
result


# %%
asjson = json.dumps(result)


# %%
siblings = pd.DataFrame(result['siblings'], columns=['name', 'age'])
siblings


# %%
get_ipython().system('cat examples/example.json')


# %%
data = pd.read_json('examples/example.json')
data


# %%
print(data.to_json())
print(data.to_json(orient='records'))

# %% [markdown]
# ### XML and HTML: Web Scraping
# %% [markdown]
# conda install lxml
# pip install beautifulsoup4 html5lib

# %%
tables = pd.read_html('examples/fdic_failed_bank_list.html')
len(tables)
failures = tables[0]
failures.head()


# %%
close_timestamps = pd.to_datetime(failures['Closing Date'])
close_timestamps.dt.year.value_counts()

# %% [markdown]
# #### Parsing XML with lxml.objectify
# %% [markdown]
# <INDICATOR>
#   <INDICATOR_SEQ>373889</INDICATOR_SEQ>
#   <PARENT_SEQ></PARENT_SEQ>
#   <AGENCY_NAME>Metro-North Railroad</AGENCY_NAME>
#   <INDICATOR_NAME>Escalator Availability</INDICATOR_NAME>
#   <DESCRIPTION>Percent of the time that escalators are operational
#   systemwide. The availability rate is based on physical observations performed
#   the morning of regular business days only. This is a new indicator the agency
#   began reporting in 2009.</DESCRIPTION>
#   <PERIOD_YEAR>2011</PERIOD_YEAR>
#   <PERIOD_MONTH>12</PERIOD_MONTH>
#   <CATEGORY>Service Indicators</CATEGORY>
#   <FREQUENCY>M</FREQUENCY>
#   <DESIRED_CHANGE>U</DESIRED_CHANGE>
#   <INDICATOR_UNIT>%</INDICATOR_UNIT>
#   <DECIMAL_PLACES>1</DECIMAL_PLACES>
#   <YTD_TARGET>97.00</YTD_TARGET>
#   <YTD_ACTUAL></YTD_ACTUAL>
#   <MONTHLY_TARGET>97.00</MONTHLY_TARGET>
#   <MONTHLY_ACTUAL></MONTHLY_ACTUAL>
# </INDICATOR>

# %%
from lxml import objectify

path = 'datasets/mta_perf/Performance_MNR.xml'
parsed = objectify.parse(open(path))
root = parsed.getroot()


# %%
data = []

skip_fields = ['PARENT_SEQ', 'INDICATOR_SEQ',
               'DESIRED_CHANGE', 'DECIMAL_PLACES']

for elt in root.INDICATOR:
    el_data = {}
    for child in elt.getchildren():
        if child.tag in skip_fields:
            continue
        el_data[child.tag] = child.pyval
    data.append(el_data)


# %%
perf = pd.DataFrame(data)
perf.head()


# %%
from io import StringIO
tag = '<a href="http://www.google.com">Google</a>'
root = objectify.parse(StringIO(tag)).getroot()


# %%
root
root.get('href')
root.text

# %% [markdown]
# ## Binary Data Formats

# %%
frame = pd.read_csv('examples/ex1.csv')
frame
frame.to_pickle('examples/frame_pickle')


# %%
pd.read_pickle('examples/frame_pickle')


# %%
get_ipython().system('rm examples/frame_pickle')

# %% [markdown]
# ### Using HDF5 Format

# %%
frame = pd.DataFrame({'a': np.random.randn(100)})
store = pd.HDFStore('mydata.h5')
store['obj1'] = frame
store['obj1_col'] = frame['a']
store


# %%
store['obj1']


# %%
store.put('obj2', frame, format='table')
store.select('obj2', where=['index >= 10 and index <= 15'])
store.close()


# %%
frame.to_hdf('mydata.h5', 'obj3', format='table')
pd.read_hdf('mydata.h5', 'obj3', where=['index < 5'])


# %%
os.remove('mydata.h5')

# %% [markdown]
# ### Reading Microsoft Excel Files

# %%
xlsx = pd.ExcelFile('examples/ex1.xlsx')


# %%
pd.read_excel(xlsx, 'Sheet1')


# %%
frame = pd.read_excel('examples/ex1.xlsx', 'Sheet1')
frame


# %%
writer = pd.ExcelWriter('examples/ex2.xlsx')
frame.to_excel(writer, 'Sheet1')
writer.save()


# %%
frame.to_excel('examples/ex2.xlsx')


# %%
get_ipython().system('rm examples/ex2.xlsx')

# %% [markdown]
# ## Interacting with Web APIs

# %%
import requests
url = 'https://api.github.com/repos/pandas-dev/pandas/issues'
resp = requests.get(url)
resp


# %%
data = resp.json()
data[0]['title']


# %%
issues = pd.DataFrame(data, columns=['number', 'title',
                                     'labels', 'state'])
issues

# %% [markdown]
# ## Interacting with Databases

# %%
import sqlite3
query = """
CREATE TABLE test
(a VARCHAR(20), b VARCHAR(20),
 c REAL,        d INTEGER
);"""
con = sqlite3.connect('mydata.sqlite')
con.execute(query)
con.commit()


# %%
data = [('Atlanta', 'Georgia', 1.25, 6),
        ('Tallahassee', 'Florida', 2.6, 3),
        ('Sacramento', 'California', 1.7, 5)]
stmt = "INSERT INTO test VALUES(?, ?, ?, ?)"
con.executemany(stmt, data)
con.commit()


# %%
cursor = con.execute('select * from test')
rows = cursor.fetchall()
rows


# %%
cursor.description
pd.DataFrame(rows, columns=[x[0] for x in cursor.description])


# %%
import sqlalchemy as sqla
db = sqla.create_engine('sqlite:///mydata.sqlite')
pd.read_sql('select * from test', db)


# %%
get_ipython().system('rm mydata.sqlite')

# %% [markdown]
# ## Conclusion
