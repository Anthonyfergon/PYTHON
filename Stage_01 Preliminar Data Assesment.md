In summary here are the 20 pandas functions that can be used to accomplish most of yourdata tasks:
1. pd.read_csv()
2. df.describe()
3. df.info()
4. df.plot()
5. df.iloc()
6. df.loc()
7. df.assign()
8. df.query()
9. df.sort_values()
10. df.sample()
11. df.isnull()
12. df.fillna()
13. df.dropna()
14. df.drop()
15. pd.pivot_table()
16. df.groupby()
17. df.transpose()
18. df.merge()
19. df.rename()

### IMPORT LIBRARIES 


```python
import os
import pandas as pd
```

### DEFINE THE WORKING DIRECTORY


```python
wd_path = os.path.abspath(
    'C:\\Users\\Asus VivoBook\\Dropbox\\My PC (DESKTOP-GN5CQHE)\\Desktop\\Documentos\\The Vault\\Python\\PyWD'
    )
```


```python
# Check if the WD exists
if not os.path.exists(wd_path):
    # create the directory if it doesn't exist
    os.makedirs(wd_path)
```


```python
# Get the WD
os.getcwd()
```




    'C:\\Users\\Asus VivoBook\\AnthonyCRENG28\\Definitive_Guide'




```python
# Additionally Options:
# You can change the WD path as follows:
os.chdir("C:\\Users\\DELL\\Documents\\")
os.getcwd()
```

### READ FILES


```python
# CSV
df_csv = pd.read_csv('C:\\Users\\Asus VivoBook\\Dropbox\\My PC (DESKTOP-GN5CQHE)\\Desktop\\Documentos\\The Vault\\Python\\PyWD\\csv_01.csv')
```

### Dimensiones


```python
df_csv.ndim
```




    2



### Size


```python
df_csv.size
```




    388164



### Headers


```python
df_csv.columns
```




    Index(['CustomerKey', 'FirstName', 'LastName', 'FullName', 'BirthDate',
           'MaritalStatus', 'Gender', 'YearlyIncome', 'TotalChildren',
           'NumberChildrenAtHome', 'Education', 'Occupation', 'HouseOwnerFlag',
           'NumberCarsOwned', 'AddressLine1', 'DateFirstPurchase',
           'CommuteDistance', 'CustomerCity', 'CustomerStateCode', 'CustomerState',
           'CustomerCountry'],
          dtype='object')



### Head - Tail


```python
df_csv.head(3)
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>CustomerKey</th>
      <th>FirstName</th>
      <th>LastName</th>
      <th>FullName</th>
      <th>BirthDate</th>
      <th>MaritalStatus</th>
      <th>Gender</th>
      <th>YearlyIncome</th>
      <th>TotalChildren</th>
      <th>NumberChildrenAtHome</th>
      <th>...</th>
      <th>Occupation</th>
      <th>HouseOwnerFlag</th>
      <th>NumberCarsOwned</th>
      <th>AddressLine1</th>
      <th>DateFirstPurchase</th>
      <th>CommuteDistance</th>
      <th>CustomerCity</th>
      <th>CustomerStateCode</th>
      <th>CustomerState</th>
      <th>CustomerCountry</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>11000</td>
      <td>Jon</td>
      <td>Yang</td>
      <td>Yang, Jon</td>
      <td>1966-04-08</td>
      <td>M</td>
      <td>M</td>
      <td>90000</td>
      <td>2</td>
      <td>0</td>
      <td>...</td>
      <td>Professional</td>
      <td>1</td>
      <td>0</td>
      <td>3761 N. 14th St</td>
      <td>2005-07-22</td>
      <td>1-2 Miles</td>
      <td>Rockhampton</td>
      <td>QLD</td>
      <td>Queensland</td>
      <td>Australia</td>
    </tr>
    <tr>
      <th>1</th>
      <td>11001</td>
      <td>Eugene</td>
      <td>Huang</td>
      <td>Huang, Eugene</td>
      <td>1965-05-14</td>
      <td>S</td>
      <td>M</td>
      <td>60000</td>
      <td>3</td>
      <td>3</td>
      <td>...</td>
      <td>Professional</td>
      <td>0</td>
      <td>1</td>
      <td>2243 W St.</td>
      <td>2005-07-18</td>
      <td>0-1 Miles</td>
      <td>Seaford</td>
      <td>VIC</td>
      <td>Victoria</td>
      <td>Australia</td>
    </tr>
    <tr>
      <th>2</th>
      <td>11002</td>
      <td>Ruben</td>
      <td>Torres</td>
      <td>Torres, Ruben</td>
      <td>1965-08-12</td>
      <td>M</td>
      <td>M</td>
      <td>60000</td>
      <td>3</td>
      <td>3</td>
      <td>...</td>
      <td>Professional</td>
      <td>1</td>
      <td>1</td>
      <td>5844 Linden Land</td>
      <td>2005-07-10</td>
      <td>2-5 Miles</td>
      <td>Hobart</td>
      <td>TAS</td>
      <td>Tasmania</td>
      <td>Australia</td>
    </tr>
  </tbody>
</table>
<p>3 rows × 21 columns</p>
</div>




```python
df_csv.tail(3)
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>CustomerKey</th>
      <th>FirstName</th>
      <th>LastName</th>
      <th>FullName</th>
      <th>BirthDate</th>
      <th>MaritalStatus</th>
      <th>Gender</th>
      <th>YearlyIncome</th>
      <th>TotalChildren</th>
      <th>NumberChildrenAtHome</th>
      <th>...</th>
      <th>Occupation</th>
      <th>HouseOwnerFlag</th>
      <th>NumberCarsOwned</th>
      <th>AddressLine1</th>
      <th>DateFirstPurchase</th>
      <th>CommuteDistance</th>
      <th>CustomerCity</th>
      <th>CustomerStateCode</th>
      <th>CustomerState</th>
      <th>CustomerCountry</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>18481</th>
      <td>29481</td>
      <td>Ivan</td>
      <td>Suri</td>
      <td>Suri, Ivan</td>
      <td>1960-01-05</td>
      <td>S</td>
      <td>M</td>
      <td>30000</td>
      <td>3</td>
      <td>0</td>
      <td>...</td>
      <td>Clerical</td>
      <td>0</td>
      <td>0</td>
      <td>Knaackstr 4</td>
      <td>2006-02-13</td>
      <td>0-1 Miles</td>
      <td>Hof</td>
      <td>BY</td>
      <td>Bayern</td>
      <td>Germany</td>
    </tr>
    <tr>
      <th>18482</th>
      <td>29482</td>
      <td>Clayton</td>
      <td>Zhang</td>
      <td>Zhang, Clayton</td>
      <td>1959-03-05</td>
      <td>M</td>
      <td>M</td>
      <td>30000</td>
      <td>3</td>
      <td>0</td>
      <td>...</td>
      <td>Clerical</td>
      <td>1</td>
      <td>0</td>
      <td>1080, quai de Grenelle</td>
      <td>2007-03-22</td>
      <td>0-1 Miles</td>
      <td>Saint Ouen</td>
      <td>17</td>
      <td>Charente-Maritime</td>
      <td>France</td>
    </tr>
    <tr>
      <th>18483</th>
      <td>29483</td>
      <td>Jésus</td>
      <td>Navarro</td>
      <td>Navarro, Jésus</td>
      <td>1959-12-08</td>
      <td>M</td>
      <td>M</td>
      <td>30000</td>
      <td>0</td>
      <td>0</td>
      <td>...</td>
      <td>Clerical</td>
      <td>1</td>
      <td>0</td>
      <td>244, rue de la Centenaire</td>
      <td>2007-03-13</td>
      <td>0-1 Miles</td>
      <td>Paris La Defense</td>
      <td>92</td>
      <td>Hauts de Seine</td>
      <td>France</td>
    </tr>
  </tbody>
</table>
<p>3 rows × 21 columns</p>
</div>



### Info Metadata


```python
df_csv.info()
```

    <class 'pandas.core.frame.DataFrame'>
    RangeIndex: 18484 entries, 0 to 18483
    Data columns (total 21 columns):
     #   Column                Non-Null Count  Dtype 
    ---  ------                --------------  ----- 
     0   CustomerKey           18484 non-null  int64 
     1   FirstName             18484 non-null  object
     2   LastName              18484 non-null  object
     3   FullName              18484 non-null  object
     4   BirthDate             18484 non-null  object
     5   MaritalStatus         18484 non-null  object
     6   Gender                18484 non-null  object
     7   YearlyIncome          18484 non-null  int64 
     8   TotalChildren         18484 non-null  int64 
     9   NumberChildrenAtHome  18484 non-null  int64 
     10  Education             18484 non-null  object
     11  Occupation            18484 non-null  object
     12  HouseOwnerFlag        18484 non-null  int64 
     13  NumberCarsOwned       18484 non-null  int64 
     14  AddressLine1          18484 non-null  object
     15  DateFirstPurchase     18484 non-null  object
     16  CommuteDistance       18484 non-null  object
     17  CustomerCity          18484 non-null  object
     18  CustomerStateCode     18484 non-null  object
     19  CustomerState         18484 non-null  object
     20  CustomerCountry       18484 non-null  object
    dtypes: int64(6), object(15)
    memory usage: 3.0+ MB
    

### Type


```python
type(df_csv)
```




    pandas.core.frame.DataFrame



### Info


```python
df_csv.info
```




    <bound method DataFrame.info of        CustomerKey  FirstName LastName            FullName   BirthDate  \
    0            11000        Jon     Yang           Yang, Jon  1966-04-08   
    1            11001     Eugene    Huang       Huang, Eugene  1965-05-14   
    2            11002      Ruben   Torres       Torres, Ruben  1965-08-12   
    3            11003    Christy      Zhu        Zhu, Christy  1968-02-15   
    4            11004  Elizabeth  Johnson  Johnson, Elizabeth  1968-08-08   
    ...            ...        ...      ...                 ...         ...   
    18479        29479      Tommy     Tang         Tang, Tommy  1958-07-04   
    18480        29480       Nina     Raji          Raji, Nina  1960-11-10   
    18481        29481       Ivan     Suri          Suri, Ivan  1960-01-05   
    18482        29482    Clayton    Zhang      Zhang, Clayton  1959-03-05   
    18483        29483      Jésus  Navarro      Navarro, Jésus  1959-12-08   
    
          MaritalStatus Gender  YearlyIncome  TotalChildren  NumberChildrenAtHome  \
    0                 M      M         90000              2                     0   
    1                 S      M         60000              3                     3   
    2                 M      M         60000              3                     3   
    3                 S      F         70000              0                     0   
    4                 S      F         80000              5                     5   
    ...             ...    ...           ...            ...                   ...   
    18479             M      M         30000              1                     0   
    18480             S      F         30000              3                     0   
    18481             S      M         30000              3                     0   
    18482             M      M         30000              3                     0   
    18483             M      M         30000              0                     0   
    
           ...    Occupation HouseOwnerFlag  NumberCarsOwned  \
    0      ...  Professional              1                0   
    1      ...  Professional              0                1   
    2      ...  Professional              1                1   
    3      ...  Professional              0                1   
    4      ...  Professional              1                4   
    ...    ...           ...            ...              ...   
    18479  ...      Clerical              1                0   
    18480  ...      Clerical              1                0   
    18481  ...      Clerical              0                0   
    18482  ...      Clerical              1                0   
    18483  ...      Clerical              1                0   
    
                        AddressLine1 DateFirstPurchase CommuteDistance  \
    0                3761 N. 14th St        2005-07-22       1-2 Miles   
    1                     2243 W St.        2005-07-18       0-1 Miles   
    2               5844 Linden Land        2005-07-10       2-5 Miles   
    3               1825 Village Pl.        2005-07-01      5-10 Miles   
    4            7553 Harness Circle        2005-07-26       1-2 Miles   
    ...                          ...               ...             ...   
    18479          111, rue Maillard        2007-03-08       0-1 Miles   
    18480          9 Katherine Drive        2008-01-18       0-1 Miles   
    18481                Knaackstr 4        2006-02-13       0-1 Miles   
    18482     1080, quai de Grenelle        2007-03-22       0-1 Miles   
    18483  244, rue de la Centenaire        2007-03-13       0-1 Miles   
    
               CustomerCity CustomerStateCode      CustomerState CustomerCountry  
    0           Rockhampton               QLD         Queensland       Australia  
    1               Seaford               VIC           Victoria       Australia  
    2                Hobart               TAS           Tasmania       Australia  
    3            North Ryde               NSW    New South Wales       Australia  
    4            Wollongong               NSW    New South Wales       Australia  
    ...                 ...               ...                ...             ...  
    18479        Versailles                78            Yveline          France  
    18480            London               ENG            England  United Kingdom  
    18481               Hof                BY             Bayern         Germany  
    18482        Saint Ouen                17  Charente-Maritime          France  
    18483  Paris La Defense                92     Hauts de Seine          France  
    
    [18484 rows x 21 columns]>



### Describe


```python
df_csv.describe
```




    <bound method NDFrame.describe of        CustomerKey  FirstName LastName            FullName   BirthDate  \
    0            11000        Jon     Yang           Yang, Jon  1966-04-08   
    1            11001     Eugene    Huang       Huang, Eugene  1965-05-14   
    2            11002      Ruben   Torres       Torres, Ruben  1965-08-12   
    3            11003    Christy      Zhu        Zhu, Christy  1968-02-15   
    4            11004  Elizabeth  Johnson  Johnson, Elizabeth  1968-08-08   
    ...            ...        ...      ...                 ...         ...   
    18479        29479      Tommy     Tang         Tang, Tommy  1958-07-04   
    18480        29480       Nina     Raji          Raji, Nina  1960-11-10   
    18481        29481       Ivan     Suri          Suri, Ivan  1960-01-05   
    18482        29482    Clayton    Zhang      Zhang, Clayton  1959-03-05   
    18483        29483      Jésus  Navarro      Navarro, Jésus  1959-12-08   
    
          MaritalStatus Gender  YearlyIncome  TotalChildren  NumberChildrenAtHome  \
    0                 M      M         90000              2                     0   
    1                 S      M         60000              3                     3   
    2                 M      M         60000              3                     3   
    3                 S      F         70000              0                     0   
    4                 S      F         80000              5                     5   
    ...             ...    ...           ...            ...                   ...   
    18479             M      M         30000              1                     0   
    18480             S      F         30000              3                     0   
    18481             S      M         30000              3                     0   
    18482             M      M         30000              3                     0   
    18483             M      M         30000              0                     0   
    
           ...    Occupation HouseOwnerFlag  NumberCarsOwned  \
    0      ...  Professional              1                0   
    1      ...  Professional              0                1   
    2      ...  Professional              1                1   
    3      ...  Professional              0                1   
    4      ...  Professional              1                4   
    ...    ...           ...            ...              ...   
    18479  ...      Clerical              1                0   
    18480  ...      Clerical              1                0   
    18481  ...      Clerical              0                0   
    18482  ...      Clerical              1                0   
    18483  ...      Clerical              1                0   
    
                        AddressLine1 DateFirstPurchase CommuteDistance  \
    0                3761 N. 14th St        2005-07-22       1-2 Miles   
    1                     2243 W St.        2005-07-18       0-1 Miles   
    2               5844 Linden Land        2005-07-10       2-5 Miles   
    3               1825 Village Pl.        2005-07-01      5-10 Miles   
    4            7553 Harness Circle        2005-07-26       1-2 Miles   
    ...                          ...               ...             ...   
    18479          111, rue Maillard        2007-03-08       0-1 Miles   
    18480          9 Katherine Drive        2008-01-18       0-1 Miles   
    18481                Knaackstr 4        2006-02-13       0-1 Miles   
    18482     1080, quai de Grenelle        2007-03-22       0-1 Miles   
    18483  244, rue de la Centenaire        2007-03-13       0-1 Miles   
    
               CustomerCity CustomerStateCode      CustomerState CustomerCountry  
    0           Rockhampton               QLD         Queensland       Australia  
    1               Seaford               VIC           Victoria       Australia  
    2                Hobart               TAS           Tasmania       Australia  
    3            North Ryde               NSW    New South Wales       Australia  
    4            Wollongong               NSW    New South Wales       Australia  
    ...                 ...               ...                ...             ...  
    18479        Versailles                78            Yveline          France  
    18480            London               ENG            England  United Kingdom  
    18481               Hof                BY             Bayern         Germany  
    18482        Saint Ouen                17  Charente-Maritime          France  
    18483  Paris La Defense                92     Hauts de Seine          France  
    
    [18484 rows x 21 columns]>



### Describe - Statistical Analysis


```python
df_csv.describe(include=['object'])
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>FirstName</th>
      <th>LastName</th>
      <th>FullName</th>
      <th>BirthDate</th>
      <th>MaritalStatus</th>
      <th>Gender</th>
      <th>Education</th>
      <th>Occupation</th>
      <th>AddressLine1</th>
      <th>DateFirstPurchase</th>
      <th>CommuteDistance</th>
      <th>CustomerCity</th>
      <th>CustomerStateCode</th>
      <th>CustomerState</th>
      <th>CustomerCountry</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>count</th>
      <td>18484</td>
      <td>18484</td>
      <td>18484</td>
      <td>18484</td>
      <td>18484</td>
      <td>18484</td>
      <td>18484</td>
      <td>18484</td>
      <td>18484</td>
      <td>18484</td>
      <td>18484</td>
      <td>18484</td>
      <td>18484</td>
      <td>18484</td>
      <td>18484</td>
    </tr>
    <tr>
      <th>unique</th>
      <td>670</td>
      <td>375</td>
      <td>18400</td>
      <td>8252</td>
      <td>2</td>
      <td>2</td>
      <td>5</td>
      <td>5</td>
      <td>12802</td>
      <td>1124</td>
      <td>5</td>
      <td>269</td>
      <td>53</td>
      <td>53</td>
      <td>6</td>
    </tr>
    <tr>
      <th>top</th>
      <td>Katherine</td>
      <td>Diaz</td>
      <td>Pal, Mohamed</td>
      <td>1967-05-14</td>
      <td>M</td>
      <td>M</td>
      <td>Bachelors</td>
      <td>Professional</td>
      <td>Attaché de Presse</td>
      <td>2008-06-14</td>
      <td>0-1 Miles</td>
      <td>London</td>
      <td>CA</td>
      <td>California</td>
      <td>United States</td>
    </tr>
    <tr>
      <th>freq</th>
      <td>97</td>
      <td>209</td>
      <td>3</td>
      <td>12</td>
      <td>10011</td>
      <td>9351</td>
      <td>5356</td>
      <td>5520</td>
      <td>17</td>
      <td>56</td>
      <td>6310</td>
      <td>420</td>
      <td>4444</td>
      <td>4444</td>
      <td>7819</td>
    </tr>
  </tbody>
</table>
</div>




```python
df_csv.describe(include='all')
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>CustomerKey</th>
      <th>FirstName</th>
      <th>LastName</th>
      <th>FullName</th>
      <th>BirthDate</th>
      <th>MaritalStatus</th>
      <th>Gender</th>
      <th>YearlyIncome</th>
      <th>TotalChildren</th>
      <th>NumberChildrenAtHome</th>
      <th>...</th>
      <th>Occupation</th>
      <th>HouseOwnerFlag</th>
      <th>NumberCarsOwned</th>
      <th>AddressLine1</th>
      <th>DateFirstPurchase</th>
      <th>CommuteDistance</th>
      <th>CustomerCity</th>
      <th>CustomerStateCode</th>
      <th>CustomerState</th>
      <th>CustomerCountry</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>count</th>
      <td>18484.000000</td>
      <td>18484</td>
      <td>18484</td>
      <td>18484</td>
      <td>18484</td>
      <td>18484</td>
      <td>18484</td>
      <td>18484.000000</td>
      <td>18484.000000</td>
      <td>18484.000000</td>
      <td>...</td>
      <td>18484</td>
      <td>18484.000000</td>
      <td>18484.000000</td>
      <td>18484</td>
      <td>18484</td>
      <td>18484</td>
      <td>18484</td>
      <td>18484</td>
      <td>18484</td>
      <td>18484</td>
    </tr>
    <tr>
      <th>unique</th>
      <td>NaN</td>
      <td>670</td>
      <td>375</td>
      <td>18400</td>
      <td>8252</td>
      <td>2</td>
      <td>2</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>...</td>
      <td>5</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>12802</td>
      <td>1124</td>
      <td>5</td>
      <td>269</td>
      <td>53</td>
      <td>53</td>
      <td>6</td>
    </tr>
    <tr>
      <th>top</th>
      <td>NaN</td>
      <td>Katherine</td>
      <td>Diaz</td>
      <td>Pal, Mohamed</td>
      <td>1967-05-14</td>
      <td>M</td>
      <td>M</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>...</td>
      <td>Professional</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>Attaché de Presse</td>
      <td>2008-06-14</td>
      <td>0-1 Miles</td>
      <td>London</td>
      <td>CA</td>
      <td>California</td>
      <td>United States</td>
    </tr>
    <tr>
      <th>freq</th>
      <td>NaN</td>
      <td>97</td>
      <td>209</td>
      <td>3</td>
      <td>12</td>
      <td>10011</td>
      <td>9351</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>...</td>
      <td>5520</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>17</td>
      <td>56</td>
      <td>6310</td>
      <td>420</td>
      <td>4444</td>
      <td>4444</td>
      <td>7819</td>
    </tr>
    <tr>
      <th>mean</th>
      <td>20241.500000</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>57305.777970</td>
      <td>1.844352</td>
      <td>1.004058</td>
      <td>...</td>
      <td>NaN</td>
      <td>0.676369</td>
      <td>1.502705</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>std</th>
      <td>5336.015523</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>32285.841703</td>
      <td>1.612408</td>
      <td>1.522660</td>
      <td>...</td>
      <td>NaN</td>
      <td>0.467874</td>
      <td>1.138394</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>min</th>
      <td>11000.000000</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>10000.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>...</td>
      <td>NaN</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>25%</th>
      <td>15620.750000</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>30000.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>...</td>
      <td>NaN</td>
      <td>0.000000</td>
      <td>1.000000</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>50%</th>
      <td>20241.500000</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>60000.000000</td>
      <td>2.000000</td>
      <td>0.000000</td>
      <td>...</td>
      <td>NaN</td>
      <td>1.000000</td>
      <td>2.000000</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>75%</th>
      <td>24862.250000</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>70000.000000</td>
      <td>3.000000</td>
      <td>2.000000</td>
      <td>...</td>
      <td>NaN</td>
      <td>1.000000</td>
      <td>2.000000</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>max</th>
      <td>29483.000000</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>170000.000000</td>
      <td>5.000000</td>
      <td>5.000000</td>
      <td>...</td>
      <td>NaN</td>
      <td>1.000000</td>
      <td>4.000000</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
  </tbody>
</table>
<p>11 rows × 21 columns</p>
</div>



### Value_Counts


```python
df_csv.value_counts()
```




    CustomerKey  FirstName  LastName   FullName            BirthDate   MaritalStatus  Gender  YearlyIncome  TotalChildren  NumberChildrenAtHome  Education            Occupation      HouseOwnerFlag  NumberCarsOwned  AddressLine1               DateFirstPurchase  CommuteDistance  CustomerCity      CustomerStateCode  CustomerState    CustomerCountry
    11000        Jon        Yang       Yang, Jon           1966-04-08  M              M       90000         2              0                     Bachelors            Professional    1               0                3761 N. 14th St            2005-07-22         1-2 Miles        Rockhampton       QLD                Queensland       Australia          1
    23419        Shawna     Xu         Xu, Shawna          1967-05-05  S              F       70000         5              5                     Bachelors            Professional    1               3                238 Montego                2008-05-01         10+ Miles        Coffs Harbour     NSW                New South Wales  Australia          1
    23327        Madison    Moore      Moore, Madison      1980-06-03  S              F       30000         0              0                     Partial College      Skilled Manual  0               2                841 Meadowbrook            2008-04-05         1-2 Miles        Daly City         CA                 California       United States      1
    23326        Tiffany    Ye         Ye, Tiffany         1980-07-22  S              F       40000         0              0                     Partial High School  Clerical        0               2                9069 Muir Road             2008-02-19         5-10 Miles       Bellflower        CA                 California       United States      1
    23325        Tiffany    Zimmerman  Zimmerman, Tiffany  1951-02-22  M              F       20000         2              1                     Partial High School  Clerical        1               2                4701 Mt. Dell Drive        2007-01-26         5-10 Miles       Geelong           VIC                Victoria         Australia          1
                                                                                                                                                                                                                                                                                                                                                              ..
    17160        Louis      Andersen   Andersen, Louis     1950-01-04  M              M       60000         2              1                     Partial College      Professional    1               2                1061 Delta Fair Blvd.      2008-05-15         10+ Miles        Bremerton         WA                 Washington       United States      1
    17159        Kellie     Ruiz       Ruiz, Kellie        1950-10-04  S              F       60000         2              1                     Partial College      Professional    1               2                9905 North 29th St.        2007-12-07         2-5 Miles        Bellingham        WA                 Washington       United States      1
    17158        Mitchell   Nara       Nara, Mitchell      1950-05-16  M              M       60000         2              1                     Partial College      Professional    1               2                21 Redhead Way             2007-09-23         10+ Miles        Bellingham        WA                 Washington       United States      1
    17157        Wyatt      Johnson    Johnson, Wyatt      1949-12-17  M              M       70000         5              1                     Partial College      Professional    1               2                5297 Algiers Drive         2008-05-01         10+ Miles        Woodland Hills    CA                 California       United States      1
    29483        Jésus      Navarro    Navarro, Jésus      1959-12-08  M              M       30000         0              0                     Bachelors            Clerical        1               0                244, rue de la Centenaire  2007-03-13         0-1 Miles        Paris La Defense  92                 Hauts de Seine   France             1
    Length: 18484, dtype: int64



### Correlation Analysis


```python
df_csv.corr
```




    <bound method DataFrame.corr of        CustomerKey  FirstName LastName            FullName   BirthDate  \
    0            11000        Jon     Yang           Yang, Jon  1966-04-08   
    1            11001     Eugene    Huang       Huang, Eugene  1965-05-14   
    2            11002      Ruben   Torres       Torres, Ruben  1965-08-12   
    3            11003    Christy      Zhu        Zhu, Christy  1968-02-15   
    4            11004  Elizabeth  Johnson  Johnson, Elizabeth  1968-08-08   
    ...            ...        ...      ...                 ...         ...   
    18479        29479      Tommy     Tang         Tang, Tommy  1958-07-04   
    18480        29480       Nina     Raji          Raji, Nina  1960-11-10   
    18481        29481       Ivan     Suri          Suri, Ivan  1960-01-05   
    18482        29482    Clayton    Zhang      Zhang, Clayton  1959-03-05   
    18483        29483      Jésus  Navarro      Navarro, Jésus  1959-12-08   
    
          MaritalStatus Gender  YearlyIncome  TotalChildren  NumberChildrenAtHome  \
    0                 M      M         90000              2                     0   
    1                 S      M         60000              3                     3   
    2                 M      M         60000              3                     3   
    3                 S      F         70000              0                     0   
    4                 S      F         80000              5                     5   
    ...             ...    ...           ...            ...                   ...   
    18479             M      M         30000              1                     0   
    18480             S      F         30000              3                     0   
    18481             S      M         30000              3                     0   
    18482             M      M         30000              3                     0   
    18483             M      M         30000              0                     0   
    
           ...    Occupation HouseOwnerFlag  NumberCarsOwned  \
    0      ...  Professional              1                0   
    1      ...  Professional              0                1   
    2      ...  Professional              1                1   
    3      ...  Professional              0                1   
    4      ...  Professional              1                4   
    ...    ...           ...            ...              ...   
    18479  ...      Clerical              1                0   
    18480  ...      Clerical              1                0   
    18481  ...      Clerical              0                0   
    18482  ...      Clerical              1                0   
    18483  ...      Clerical              1                0   
    
                        AddressLine1 DateFirstPurchase CommuteDistance  \
    0                3761 N. 14th St        2005-07-22       1-2 Miles   
    1                     2243 W St.        2005-07-18       0-1 Miles   
    2               5844 Linden Land        2005-07-10       2-5 Miles   
    3               1825 Village Pl.        2005-07-01      5-10 Miles   
    4            7553 Harness Circle        2005-07-26       1-2 Miles   
    ...                          ...               ...             ...   
    18479          111, rue Maillard        2007-03-08       0-1 Miles   
    18480          9 Katherine Drive        2008-01-18       0-1 Miles   
    18481                Knaackstr 4        2006-02-13       0-1 Miles   
    18482     1080, quai de Grenelle        2007-03-22       0-1 Miles   
    18483  244, rue de la Centenaire        2007-03-13       0-1 Miles   
    
               CustomerCity CustomerStateCode      CustomerState CustomerCountry  
    0           Rockhampton               QLD         Queensland       Australia  
    1               Seaford               VIC           Victoria       Australia  
    2                Hobart               TAS           Tasmania       Australia  
    3            North Ryde               NSW    New South Wales       Australia  
    4            Wollongong               NSW    New South Wales       Australia  
    ...                 ...               ...                ...             ...  
    18479        Versailles                78            Yveline          France  
    18480            London               ENG            England  United Kingdom  
    18481               Hof                BY             Bayern         Germany  
    18482        Saint Ouen                17  Charente-Maritime          France  
    18483  Paris La Defense                92     Hauts de Seine          France  
    
    [18484 rows x 21 columns]>



### Null Values


```python
df_csv_nulls = df_csv.isna().any()
print(df_csv_nulls)
```

    CustomerKey             False
    FirstName               False
    LastName                False
    FullName                False
    BirthDate               False
    MaritalStatus           False
    Gender                  False
    YearlyIncome            False
    TotalChildren           False
    NumberChildrenAtHome    False
    Education               False
    Occupation              False
    HouseOwnerFlag          False
    NumberCarsOwned         False
    AddressLine1            False
    DateFirstPurchase       False
    CommuteDistance         False
    CustomerCity            False
    CustomerStateCode       False
    CustomerState           False
    CustomerCountry         False
    dtype: bool
    

### WRITE FILE


```python

```
