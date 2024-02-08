# _____________________________________________________________________
#                            PYTHON GUIDELINE
#               Prepared by AnthonyCRENG28, Rabbit industries.      
# _____________________________________________________________________

# Best practice, use an environment rather than install in the base env
# conda create -n my-env
# conda activate my-env
# If you want to install from conda-forge
# conda config --env --add channels conda-forge

# ------------------------------------------------------------------- #
#### PYTHON_LIBRARIES
# ------------------------------------------------------------------- #

# MACHINE_LEARNING
import pandas as pd                                    # tabular
pd.__version__
print(dir(pd))
help(pd.__loader__)

import numpy as np                                     # arrays
np.version.version
print(dir(np))
help(np.trace)

import scipy as sp                                     # statistics

import statsmodels as sm                               # statistics

import matplotlib as mpl 
import matplotlib.pyplot as plt                        # visualization
import seaborn as sns                                  # visualization
import sklearn as sk                                   # machine_learning

import sys
print(dir(sys))
help(sys.version)
help(sys.__loader__)

# DATETIME
import datetime as dt
from datetime import datetime, date, time, timedelta
import pytz as tz
from pytz import timezone

# DISTRIBUTED_ENV_CLUSTERS
import pyspark as spk
from pyspark import SparkContext
import pyarrow as pa

# MONGODB, MONGO ATLAS, MONGOSH (NO RELATIONAL DB)
import pymongo as mdb
from pymongo import MongoClient

# Miscellaneous
import pprintpp as pp                                      # format arbitrary structures
from pprint import pprint

print('python', sys.version)
print('pandas', pd.__version__)
print('numpy', np.__version__)
print('scipy', sp.__version__)
print('statsmodel', sm.__version__)
print('matplotlib', mpl.__version__)
print('seaborn', sns.__version__)
print('sklearn', skl.__version__)
print('datetime', dt.__version__)
print('pytz', tz.__version__)
print('pyspark', spk.__version__)
print('pyarrow', pa.__version__)
print('pymongo', mdb.__version__)
print('pprintpp', pp.__version__)

# ------------------------------------------------------------------- #
#### PRINT_FUNCTION
# ------------------------------------------------------------------- #

print('hello world')

print('hello', 'world', sep=None)

print('hello', 'world', sep=' ')

print('hello', 'world')

print('hello', 'world', sep='\n')

print('home', 'user', 'documents', sep='/')

print(*['jdoe is', 42, 'years old'])

print('line1\nline2\nline3')

value = print('hello world')
print(value)

# ------------------------------------------------------------------- #
#### ARITHMETIC_OPS
# ------------------------------------------------------------------- #

## != diff
## == equal
##  / div
## // floor div
## <  lower
## >  higher
## ** exponent
##  % modulus
## ? question_mark (apply after a var will display gral info about the object)}
    ## example: print? 
    ## Docstring:print(value, ..., sep=' ', end='\n', file=sys.stdout, flush=False)
## ?? show function´s source code  
    ## example: add_numbers??
    ## Signature: add_numbers(a, b)
    ## Source: def add_numbers(a, b):"""  Add two numbers together Returns  the_sum : type of arguments """return a + bFile: <ipython-input-9-6a548a216e27>Type: function
## Ctrl+C (Stops compilation) 
  
# ADDITION

# Adding figures
print(5+5)

var_one = 1
var_two = 2

print(var_one < 1)
print(var_two >= var_one)

# Adding strings
x = 'apple'
x + ' pie'

# SUBTRACTION
print(10-5)

# MULTIPLICATION
print(10*2)

# DIVISION
print(9/3)

# Cociente and residuo
print(divmod(5, 2))

# EXPONENTIATION (POWER)
# In Python, ** is the exponentiation operator. It is used to raise the first operand to power of second.
print(5**5)

# MODULUS (RESIDUAL)
# In Python, % is the modulus operator. It is used to find the remainder when first operand is divided by the second.
print(10 % 3)

# FLOOR DIVISION
# In Python, // is used to conduct the floor division. It is used to find the floor of the quotient when first operand is divided by the second.
val1 = 100
val2 = 2
  # using the floor division
res = val1 // val2
print(res)

# < operators >
x= 6
if x > 5:
    print('lucky_rabbit')

# ------------------------------------------------------------------- #
#### VARIABLES
# ------------------------------------------------------------------- #

var_1 = 10
var_1

var_2 = 10.1
var_2

var_3 = True
var_3

var_4 = 'Curso'
var_4

var_5 = "Curso"
var_5

var_6 = var_1/float(2)
var_6

#### Var_Types (type)

type(var_1)
type(var_2)
type(var_3)
type(var_4)
type(var_5)

# Examples
Salario_Bruto = 1200
Seguro_Medico = Salario_Bruto * (10.5 / 100)
Ahorro = Salario_Bruto * 0.02
Impuesto = Salario_Bruto * 0.10
Salario_Neto = Salario_Bruto - Seguro_Medico - Ahorro - Impuesto
print(Salario_Neto)

#### Casting_type
cast_01 = float(var_1)

#### Delete_Variables (del)
del var_1

# ============================================================
#### STRINGS
# ============================================================

my_string = 'thisStringIsAwesome'
my_string


# ============================================================
#### DATES AND TIMES
# ============================================================

## Create date
import pandas as pd

# Frequence by Days
dates_d = pd.date_range('20191110', periods=10, freq='D')
# Frequence by Months
dates_m = pd.date_range('20191110', periods=10, freq='M')
# Create data with date
df = pd.DataFrame(random, index=dates_m, columns=list('ABCD'))

# Demistify timestamp format into datetime-categories
from datetime import datetime 
datetime.strptime('2018-04-29T17:45:25Z', '%Y-%m-%dT%H:%M:%SZ')

from dateutil.parser import parse
parse('2018-04-29T17:45:25Z')

import arrow 
arrow.get('2018-04-29T17:45:25Z').datetime

import moment
moment.date("tomorrow")

import maya
maya.parse('2018-04-29T17:45:25Z').slang_time()

# Datetime_tutorials
    # https://www.geeksforgeeks.org/python-datetime-module/

from datetime import date
today = date.today()
print("Today's date is", today)

from datetime import datetime
# Calling now() function
today = datetime.now()
print("Current date and time is", today)

# Convert datetime to string format
from datetime import datetime as dt
# Getting current date and time
now = dt.now()
string = dt.isoformat(now)
print(string)
print(type(string))

from datetime import date
today = date.today()
print("Current year:", today.year)
print("Current month:", today.month)
print("Current day:", today.day)

from datetime import time
Time = time(11, 34, 56)
print("hour =", Time.hour)
print("minute =", Time.minute)
print("second =", Time.second)
print("microsecond =", Time.microsecond)

from datetime import datetime
a = datetime(1999, 12, 12, 12, 12, 12)
print("year =", a.year)
print("month =", a.month)
print("hour =", a.hour)
print("minute =", a.minute)
print("timestamp =", a.timestamp())

from datetime import datetime
# Getting Datetime from timestamp
date_time = datetime.fromtimestamp(1887639468)
print("Datetime from timestamp:", date_time)

# Calculating future dates
from datetime import datetime, timedelta
# Using current time
ini_time_for_now = datetime.now()
# printing initial_date
print("initial_date", str(ini_time_for_now))
# Calculating future dates for two years
future_date_after_2yrs = ini_time_for_now + timedelta(days=730)
future_date_after_2days = ini_time_for_now + timedelta(days=2)
# printing calculated future_dates
print('future_date_after_2yrs:', str(future_date_after_2yrs))
print('future_date_after_2days:', str(future_date_after_2days))

# Difference between two date and times
from datetime import datetime, timedelta
# Using current time
ini_time_for_now = datetime.now()
# printing initial_date
print("initial_date", str(ini_time_for_now))
# Some another datetime
new_final_time = ini_time_for_now + \
    timedelta(days=2)
# printing new final_date
print("new_final_time", str(new_final_time))
# printing calculated past_dates
print('Time difference:', str(new_final_time -
                              ini_time_for_now))

# Apply date format to datetime operations
from datetime import datetime as dt
# Getting current date and time
now = dt.now()
print("Without formatting", now)
# Example 1
s = now.strftime("%A %m %-Y")
print('\nExample 1:', s)
# Example 2
s = now.strftime("%a %-m %y")
print('\nExample 2:', s)
# Example 3
s = now.strftime("%-I %p %S")
print('\nExample 3:', s) 
# Example 4
s = now.strftime("%H:%M:%S")
print('\nExample 4:', s)

# import datetime module from datetime
from datetime import datetime
# consider the time stamps from a list  in string
# format DD/MM/YY H:M:S.micros
time_data = ["25/05/99 02:35:8.023", "26/05/99 12:45:0.003",
             "27/05/99 07:35:5.523", "28/05/99 05:15:55.523"] 
# format the string in the given format : day/month/year 
# hours/minutes/seconds-micro seconds
format_data = "%d/%m/%y %H:%M:%S.%f"
# Using strptime with datetime we will format string
# into datetime
for i in time_data:
    print(datetime.strptime(i, format_data))
# Timezone_tutorials
    # https://www.geeksforgeeks.org/python-pytz/

import datetime as dt
from datetime import datetime, date, time, timedelta

path = r'C:\Users\Asus VivoBook\Dropbox\My PC (DESKTOP-GN5CQHE)\Documents\My Studies\PowerUp Institute\Python\week 04\BDTienda.csv'
df = pd.read_csv(path,sep=',',header=0,index_col=False,
                 encoding='latin-1',engine='python',
                 parse_dates=['Order Date','Ship Date'])

# consulto metadata
df.info()

# ============================================================
#### IF ELIF ELSE
# ============================================================

lista1 = []

for producto in df['Product ID']:
    if producto >=50:
        lista1.append(True)
    else:
        lista1.append(False)
        
len(lista1)
        
fil_1 = pd.Series(lista1)
        
df_new = df[fil_1]

# ============================================================================
# IF con una condiciion a cumplirse y un resultado para cuando no se cumple
# ============================================================================

x = 10

### IF con una condicion

if x <12:
    print('10 es menor que 12')


### IF con una condicion a cumplir y cuando no se cumple

if x < 9:
    print('10 es menor que 9')
else:
    print('10 no es menor que 12')
    
### IF anidado que evalue la cantidad de varuiables condicionales

if x > 11 and x < 20:
    print('10 es mayor que 11 y menor que 20')
elif x > 5 or x < 9:
    print('10 es mayor que 5 o menor que 9')
else:
    print('Nose cumple ningun criterio')
    
# Example_02

lst = [4, 5, 6, 8, 10]
i = 6

if i in lst:
	print("Yes 6 is present in the list")
else:
	print("No 6 is not present in the list")

# =============================================================
#### BUCLES FOR
# =============================================================
        
for columna, fila in df.iterrows():
    df.loc[columna, 'ShipCityCopia'] = fila['ShipCity'].upper()
    
print(df.head())

df['ShipCityCopia2'] = df['ShipCity'].apply(len)

for columna, fila in df.iterrows():
    df.loc[columna, 'ShipCityCopia'] = fila['ShipCity'].upper()

print(df.head())

df['ShipCityCopia2'] = df['ShipCity'].apply(len)

# =============================================================
#### LISTS []
# =============================================================
# You use lists to store or organize data in a sequential order. 
# This data can be a string, numbers, or iterables like a list.
# A list is also mutable, which means that it can expand and change after you declare it (you add new elements to it).

Lista_1 = ["Dayana", "Juan", "Roger", "Antonio"]
Lista_2 = ["Luis", 90, "Gerald", 40, "Anthony", 30]

#### Insert Values into a list (extend, insert, append)

# Method 01 extend (Inserts multiple objects at the time)
Lista_2.extend(["Esteban", 20])
Lista_2
# Method 02
Lista_2 = Lista_2 + ["Celeste", 10]
# Method 03 insert ((Inserts multiple objects at the time))
Lista_2.insert(11, "Hola")
print(Lista_2)
# Method 04 append (Inserts 1 object at the time)
Lista_2.append('Snowflake')
print(Lista_2)

#### Remove Values from a list (remove)

Lista_2.remove("Hola")
print(Lista_2)

#### Remove Values by Position (remove)
# Elimina los 2 elementos q se encuentren anteriores al ultimo
del(Lista_2[-2:])
print(Lista_2)

#### Position of an element within a list (index)

print(Lista_2.index("Anthony"))
print(Lista_2[4:6])

# The below exercise helps us to get an letter from an object in a list
# 1st index is associated to an object
# 2nd index refers to the 
favorites = ['raindrops', 'roses', 'whiskers', 'snowflakes']
print(favorites[-2][-3])
# Inversely if we need to get the last object
# Note: Index [0] acts for the 1st object solely.
favorites[-1]
favorites[1]

#### A List composed by multiple lists

Lista_3 = [["Antonio", 80], ["Luis", 90], ["Gerald,40"], ["Esteban", 20]]

#### Number of items in a list(len.function)
# The len() function returns the number of items in an object
len(Lista_3)

#### Adding Lists

Morph_list = favorites + Lista_3

#### Convert two lists into a Dictionary (zip, dict)

name = ["Dave", "Jerry", "Sasha"]
score = [43, 56, 78]
result = zip(name, score)
type(result)
dict = dict(result)

#### Add Index using the enumerate function

l1 = ["eat", "sleep", "repeat"]
s1 = "geek"
# creating enumerate objects
obj1 = enumerate(l1)
obj2 = enumerate(s1)
print ("Return type:", type(obj1))
print (list(obj1))
# changing start index to 2 from 0
print (list(enumerate(s1, 2)))

# Count the number of times the values in an iterable occurs (counter)
from collections import Counter
lst = ["Free", "Code", "Camp", "Code", "Free"]
print(Counter(lst))

# =============================================================
#### TUPLES ()
# =============================================================
# A tuple is another data collection type in Python. 
# You also use it to store and organize data in the form of a list.
# The only difference is that it is immutable, which means it cannot expand (you can't add new elements to it) like a list.

Tupla_1 = ("Gerald", 40, "Marlon", 20, "Luis", 10)
Tupla_2 = (("Gerald", 40), ("Marlon", 20), ("Luis", 10))

#### Position of an element within a Tuple []

Tupla_1[1]

Tupla_2[1]

#### Convert a Tuple into a List

lista_4 = list(Tupla_1)
type(lista_4)

Tupla_3 = tuple(lista_4)
type(Tupla_3)

#### Consult an object within a tuple (by Name)

print("Gerald" in Tupla_1)

#### Qty of values in a Tuple (len)

print(len(Tupla_3))

# =============================================================
#### DICTIONARIES {}
# =============================================================
# A dictionary is a Python collection that stores data as key-value pairs.
# You can create a dictionary using curly braces. Also dictionaries are mutable.

estudiantes = {"Juan": "Python", "Luis Diego": "RStudio", "Roger": "SQL"}
type(estudiantes)

#### Consult Dictionary Keys (keys)

estudiantes.keys()

#### Consult Pair_Values associated to a Key

estudiantes["Juan"]

#### Add New Key_Value_Pairs

estudiantes["Esteban"] = "Julia"

del estudiantes["Esteban"]

#### # A Dictionary made by multiple dictionaries

equipo = {"Dayana": {"Curso": "RPA", "Nota": 90},
          "Gerald": {"Curso": "R", "Nota": 100}}

#### # Add a Dictionary into a Dictionary

equipo["Esteban"] = {"Curso": "Python", "Nota": 80}

print(equipo)

# =============================================================
#### FUNCTIONS
# =============================================================


# There are 3 types of Funcions: 
    # 01. Functions with No Arguments
    # 02. Functions with One-Single Argument
    # 03. Functions with Multiple Arguments.

# Resources: https://www.kaggle.com/code/alexisbcook/functions

### EXAMPLE_01 (With No-Argument)

# Define the function with no arguments and with no return
def print_hello():
    print("Hello, you!")
    print("Good morning!")
    
# Call the function
print_hello()

### EXAMPLE_01 (One-Single Argument)
    
# Step_02: Define the function
# The add_three() function below accepts any number, adds three to it, and then returns the result.
def add_three(input_var): # input_var  is a <single_argument>
    output_var = input_var + 3
    return output_var   

# Step_03: Run the function with 10 as input
new_number = add_three(10)
# Check that the value is 13, as expected
print(new_number)  

### EXAMPLE_02 (One-Single Argument)

# Calculate a weekly paycheck after taxes.
# They're in a 12% tax bracket (in other words, 12% of their salary is taken for taxes, and they only take home 88%), and
# They're paid hourly, at a rate of $15/hour.
def get_pay(num_hours):
    # Pre-tax pay, based on receiving $15/hour
    pay_pretax = num_hours * 15
    # After-tax pay, based on being in 12% tax bracket
    pay_aftertax = pay_pretax * (1 - .12)
    return pay_aftertax

# Calculate pay based on working 40 hours
pay_fulltime = get_pay(40)
print(pay_fulltime)

### EXAMPLE_03 (One-Single Argument)

def evaluate_temp(temp):
    # Set an initial message
    message = "Normal temperature."
    # Update value of message only if temperature greater than 38
    if temp > 38:
        message = "Fever!"
    return message

print(evaluate_temp(37))
print(evaluate_temp(39))

### EXAMPLE_04 (One-Single Argument)

def evaluate_temp_with_else(temp):
    if temp > 38:
        message = "Fever!"
    else:
        message = "Normal temperature."
    return message

print(evaluate_temp_with_else(37))

### EXAMPLE_05 (One-Single Argument)

def evaluate_temp_with_elif(temp):
    if temp > 38:
        message = "Fever!"
    elif temp > 35:
        message = "Normal temperature."
    else:
        message = "Low temperature."
    return message

evaluate_temp_with_elif(36)

### EXAMPLE_06 (One-Single Argument)

def get_taxes(earnings):
    if earnings < 12000:
        tax_owed = .25 * earnings
    else:
        tax_owed = .30 * earnings
    return tax_owed

ana_taxes = get_taxes(9000)
bob_taxes = get_taxes(15000)

print(ana_taxes)
print(bob_taxes)

### EXAMPLE_07 (One-Single Argument)

def get_dose(weight):
    # Dosage is 1.25 ml for anyone under 5.2 kg
    if weight < 5.2:
        dose = 1.25
    elif weight < 7.9:
        dose = 2.5
    elif weight < 10.4:
        dose = 3.75
    elif weight < 15.9:
        dose = 5
    elif weight < 21.2:
        dose = 7.5
    # Dosage is 10 ml for anyone 21.2 kg or over
    else:
        dose = 10
    return dose

print(get_dose(12))

### EXAMPLE_01 (Multiple Arguments)

# get_pay_with_more_inputs() function below, which calculates a weekly paycheck based on three arguments:
# num_hours - number of hours worked in one week
# hourly_wage - the hourly wage (in $/hour)
# tax_bracket - percentage of your salary that is removed for taxes

def get_pay_with_more_inputs(num_hours, hourly_wage, tax_bracket):
    # Pre-tax pay
    pay_pretax = num_hours * hourly_wage
    # After-tax pay
    pay_aftertax = pay_pretax * (1 - tax_bracket)
    return pay_aftertax

higher_pay_aftertax = get_pay_with_more_inputs(40, 24, .22)
print(higher_pay_aftertax)

#### LOOPS
Loops: A loop is a piece of code that runs over and over again until the condition is false.

my_tuple = (2, 3, 4, 6, 10, 12)
my_new_lst = []
for i in my_tuple:
    if i % 3 == 0:
        my_new_lst.append(i)
print(my_new_lst)



# *************************************************************
####                    P  A  N  D  A  S  
# *************************************************************
import pandas as pd
pd.__version__
print(dir(pd))
help(pd.__loader__)

# =============================================================
#### Series
# =============================================================
import numpy as np

a = pd.Series([10, 20, 30])
print(a)
a = pd.Series([10, 20, 30], index=['a', 'b', 'c'])
print(a)
a = pd.Series([10, 20,np.nan])
type(a)

# =============================================================
#### Dataframes
# =============================================================

#### Convert a Dictionary into a DataFrame

# 01. Create a Dictionary
equipo = {"Dayana": {"Curso": "RPA", "Nota": 90},
          "Gerald": {"Curso": "R", "Nota": 100}}
type(equipo)

# 02 Convert the Dict into a DF
x = pd.DataFrame(equipo)
type(x)

names = ["Luis Diego", "Anthony", "Gerald",
         "Roger", "Ruy", "Antonio", "Dayana", "Juan"]

country = ["Peru", "Guatemala", "Mexico", "Chile",
           "Argentina", "Costa Rica", "Panama", "Colombia"]

Age = [20, 21, 22, 23, 24, 25, 26, 27]

Calificacion = [90, 80, 90, 80, 90, 100, 70, 60]

Estudiantes = {"Nombre": names, "Pais": country,
               "Edad": Age, "Nota": Calificacion}

df = pd.DataFrame(Estudiantes)
print(df)



#### READ-WRITE FILES

# BEST PRACTICES:
# 01. Define a Working Directory. Use the OS library.    

import os
import pandas as pd

# Define the path to the WD
wd_path = os.path.abspath(
    'C:\\Users\\Asus VivoBook\\Dropbox\\My PC (DESKTOP-GN5CQHE)\\Desktop\\Documentos\\The Vault\\Python\\PyWD'
    )

# Check if the WD exists
if not os.path.exists(wd_path):
    # create the directory if it doesn't exist
    os.makedirs(wd_path)
    
# Get the WD
os.getcwd()

# Additionally you can change the WD path as follows:
os.chdir("C:\\Users\\DELL\\Documents\\")
os.getcwd()

#### READ FILES

# CSV
df = pd.read_csv('C:\\Users\\Asus VivoBook\\Dropbox\\My PC (DESKTOP-GN5CQHE)\\Desktop\\Documentos\\The Vault\\Python\\PyWD\\csv_01.csv')

# Excel
path = r'C:\Users\Asus VivoBook\Dropbox\My PC (DESKTOP-GN5CQHE)\Documents\My Studies\PowerUp Institute\Python\week 01'
df = pd.ExcelFile(path+'\AdventureWorks.Xlsx').parse(sheet_name='Customer',header=0,index_col=0)
# Check the type ( must be a dataframe <df>)
type(df)
df['MaritalStatus'] = df['MaritalStatus'].astype('bool')

df.head()

# Assign function allow us to add new columns to the dataframe
df_new = df.assign(new_col=df['NumberCarsOwned']*2)

# Query function allow us to filter data from a DF based on a Boolean expression.
df.info()
df_query = df.query('' == 'Victoria')

#### WRITE FILES

df.to_csv("C:/Users/Asus VivoBook/Dropbox/My PC (DESKTOP-GN5CQHE)/Desktop/Pendientes de todos los dias/csv_01.csv") 
# You can also setup additional customizations as follows: 
    # Omit header and add delimiters: 
        # df.to_csv("c:/tmp/courses.csv", header=False, sep='|')
    # Append DataFrame to existing CSV File:
        # df.to_csv("c:/tmp/courses.csv", header=False, sep='|', index=False, mode='a')

# Create a Pandas Excel writer using XlsxWriter as the engine.
writer = pd.ExcelWriter('Python_Output.xlsx', engine='xlsxwriter')

# Convert the dataframe to an XlsxWriter Excel object.
xls.to_excel(writer, sheet_name='Output_01', index=False)

===================
#### Define your own column names instead of header row from CSV file
emp1 = pd.read_csv("emp10.csv", skiprows=1,
names=['Emp_ID','Emp_Name','Emp_Desig','Emp_DOJ','Emp_
Sal'])
print(emp1)
skiprows = 1 means we are ignoring first row and names=
option is used to assign variable names manually.

===================
#### Add prefix to column names
emp1 = pd.read_csv("emp10.csv", header = None,
prefix="var")
print(emp1)
In this case, we are setting var as prefix which tells python to
include this keyword before each column name.

===================
#### Specify missing values
----------------------
The na_values= options is used to set some values as blank /
missing values while importing CSV file.
emp1 = pd.read_csv("emp10.csv", na_values=['.'])
print(emp1)

===================
#### Change column type while importing CSV
--------------------------------------
Suppose you want to change column format from int64 to
float64 while loading CSV file into Python. We can use dtype =
option for the same.
emp = pd.read_csv("emp10.csv", dtype = {"sal" : "float64"})
print(emp)
emp.info()

===================
#### Measure time taken to import big CSV file
-----------------------------------------
With the use of verbose=True, you can capture time taken for
Tokenization, conversion and Parser memory cleanup.
emp = pd.read_csv("emp10.csv", verbose=True)

===================
#### How to read CSV file without using Pandas package
--------------------------------------------------
To import CSV file with pure python way, you can submit the following command :
    
import csv
with open("E:/MLDataSets/emp10.csv") as a:
 d = csv.DictReader(a)
 l=list(d)
 
===================
#### How to read CSV file from URL without using Pandas package
----------------------------------------------------------
import csv
import requests
response = requests.get('https://dyurovsky.github.io/psyc201/data/lab2/nycflights.csv').textlines = response.splitlines()
d = csv.DictReader(lines)
l = list(d)

===================
#### Read CSV File from External URL
===============================
You can directly read data from the CSV file that is stored on a
web link.
a =
pd.read_csv("http://winterolympicsmedals.com/medals.csv")
a.shape
a.head()
# This DataFrame contains 2311 rows and 8 columns. Using mydata02.shape, you can generate this summary.

===================
#### Skip Last 5 Rows While Importing CSV
-------------------------------------
a =
pd.read_csv("http://winterolympicsmedals.com/medals.csv",
skipfooter=5)
a.shape
a.head()
# In the above code, we are excluding bottom 5 rows using skipfooter= parameter

===================
#### Read Text File
==============
We can use read_table() function to pull data from text file. We
can also use read_csv() with sep= "\t" to read data from tabseparated file.
a = pd.read_table("E:/MLDataSets/demo.txt")
a = pd.read_csv("E:/MLDataSets/demo.csv", sep ="\t")

===================
#### Read Excel File
===============
The read_excel() function can be used to import excel data into
Python.
emp = pd.read_excel("E:/MLDataSets/emp10.xlsx")
print(emp)
If you do not specify name of sheet in sheetname= option, it
would take by default first sheet.

===================
#### Read delimited file
===================
Suppose you need to import a file that is separated with white
spaces.
mydata2 =
pd.read_table("http://www.ssc.wisc.edu/~bhansen/econometri
cs/invest.dat", sep="\s+", header = None)

===================
#### Read JSON files, then Convert it into CSV format                           ---VERIFIED
===================

import pandas as pd

# Load the JSON file into a Pandas dataframe
df = pd.read_json('C:\data\export.json')

# Write the dataframe to a CSV file
df.to_csv(r'C:\data\export.csv', index=False)

# Alternatively, you can use the os library to open the csv automatically.
import os
os.startfile('C:\data\export.csv')

===================
#### Read ORC files, then convert to csv format
===================

import pandas as pd
import pyarrow.orc as orc

# Open the ORC file
file = orc.ORCFile(filename)
# Read the entire ORC file into a table
table = file.read()
# Convert the table to a pandas DataFrame
df = table.to_pandas()

# or, alternatively:

import pandas as pd
import pyarrow.orc as orc

with open(filename) as file:
    data = orc.ORCFile(file)
    df = data.read().to_pandas()
    
===================
#### Read AVRO files, then convert to csv format
===================

import fastavro

# Open the Avro file
with open('file.avro', 'rb') as f:
    reader = fastavro.reader(f)
    
    # Iterate over the records in the Avro file
    for record in reader:
        print(record)

===================
#### Read ZIP files, then convert to csv format
===================
 
import zipfile
import pandas as pd

# read the zip file
with zipfile.ZipFile('C:\data\jar_files.zip', "r") as zip_ref:
    zip_ref.extractall("extracted_content")

# read the extracted file into a pandas dataframe
df = pd.read_csv('extracted_content\C:\data\export.csv')

# save the dataframe as a csv file
df.to_csv("converted.csv", index=False)

===================
#### TEXT DATA
===================
import pandas as pd

# Series: A Pandas Series is like a column in a table. It is a one-dimensional array holding data of any type.
s = pd.Series(
    ['Srinivas', 'DATAhill', '9292005440','Hyderabad', 'info@datahill.in', 'dataanalysis', 'PYTHON','Pandas']
     )



s.str.islower()
s.str.lower()
s.str.isupper()
s.str.upper()
s.str.isnumeric()
s.str.swapcase()
s.str.len()
s.str.cat(sep='_')
s.str.replace('@','$')
s.str.repeat(2)
s.str.count('s')
s.str.startswith ('P')
s.str.endswith('s')
 
# -----------------         DATA MANIPULATION WITH PANDAS         ---------------- #     

import pandas as pd
path = r'C:\Users\Asus VivoBook\Dropbox\My PC (DESKTOP-GN5CQHE)\Documents\My Studies\PowerUp Institute\Python\week 01'
df = pd.read_csv(path+'\\NorthWind.csv', sep = ',',index_col=False, header=0,encoding='Latin-1',engine='python')
print(df.columns)

#### Subsets Creation

sub_df_01 = df['ShipCity']  # Cuando el texto esta encerrado en 1 SquareBracket es una SERIE DE PANDAS
type(df['ShipCity'])
sub_df_02 = df[['ShipCity','ShipRegion','ShipAddress']] ## Cuando esta encerrado en 2 SquareBrackets es un DATAFRAME
type(df[['ShipCity']])

#### Trace objects by Position
df[1:4]

##### Freezepanes (set_index)
df_01 = df.set_index('ShipName') # DF.SET.INDEX es el quivalente de FreezePanes en Excel.
df_01 = df.set_index(['ShipName','ShipperName'])

#### Selection Columns by Label (.loc) with pandas
# https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.iloc.html
df_02 = df_01.loc[['QUICK-Stop','Rancho grande']]
df_07 = df.iloc[:,[0,1]]
df_08 = df.iloc[1:100,[0,1]]
df_09 = df.iloc[[100,200,300,400] , 0:4]

#### Select Specific Columns 
df_03 = df.loc[:,['ShipName','ShipAddress']]
df_04 = df_01.loc[['QUICK-Stop','Rancho grande'],['ShipAddress','ShipRegion']]

#### Selection Columns by Position (.iloc)
df_05 = df.iloc[1:100] # TOP 100

#### Select range (iloc)
df_06 = df.iloc[[100,200]]

# =============================================================
# Filtering DataSets
# =============================================================

import numpy as np
import pandas as pd

df[['ProductID','CustomerID']] # Poner 2 SquareBrackets nos permite seguir ingresando mas columnas hacia la derecha
df.loc[:,['ProductID', 'CustomerID']]
result_2 = df[df['ProductID'] > 50] 

# Filtering using Logical Ops (and / or / not / isin)
df_fil_3 = df[df['ShipName']=='LILA-Supermercado']
df_fil_3 = df[(df['ShipName']=='LILA-Supermercado') & (df['ProductID']==30)]

# isin # Nos permite realizar busquedas especificas
df_fil_4 = df[df['ShipName'].isin(['LILA-Supermercado','Familia Arquibaldo'])]

# np.logical_and // np.logical_or // np.logical_not # Customize your filters by rank
df_fil_5 = df[np.logical_and(df['ProductID']>=50,df['ProductID']<=60)]
df_fil_6 = df[np.logical_not(df['ProductID']>=50)]
df_fil_7 = df[np.logical_not(df['ProductID']>=50)][['ShipName','ShipAddress']]
df_fil_8 = df.loc[np.logical_not(df['ProductID']>=50),['ShipName','ShipAddress']]



# ============================================================================
# BUCLE FOR para cada variable es una secuencia que ejecuta el sgte paso
# ============================================================================

import numpy as np

edades = [20,30,40,50,60,70]

### Como hacer un bucle en una lista

for age in edades:
    print(age)

### Como hacer un Bucle en un diccionario

for age, key in edades.items():
    print(age)
    
### Array

for age in np.nditer(edades):
        print(age)
        
df_bucle = pd.DataFrame({'uno':[1,2,3], 'dos':[4,5,6],'tres':[7,8,9]},index = ['x','y','z'])
    
### Iteracion por columnas del DataFrame

fol col in df_bucle:
        print(df_bucle[col].mean())

### Iteracion por filas del DataFrame

for indice_fila, fila in df_bucle.iterrows():
    print(indice_fila)
    print(fila)


for columna, fila in df.iterrows():
    df.loc[columna, 'ShipCityCopia'] = fila['ShipCity'].upper()
    
print(df.head())

df['ShipCitytCopia2'] = df['ShipCity'].apply(len)


# ========================================================================
#### Transformacion de Columnas
# ========================================================================

### Agregando una columna nueva calculada

df['SalesAmount'] = df['Quantity']*df['UnitPrice']

### Eliminando los duplicados de las columnas

df_dup_1 = df.drop_duplicates(subset='ShipName')

df_dup_2 = df.drop_duplicates(subset=['ShipName','Salesperson'])

#### Aggregation Functions

### Obteniendo la media agrupada por ShipName
df_gr_1 = df.groupby('ShipeName')['Quantity'].mean()

### Diferentes funciones de Agregacion median(), value_counts(normalize=True)
df_gr_2 = df.groupby('ShipName')['Quantity'].agg([min, max, sum, np.mean])

### Agrupando por 2 Variables ShipName & ShipperName y dif agregaciones
df_gr_3 = df.groupby('ShipName, ShipperName')['Quantity'].agg([min, max, sum, np.mean])

### Agrupando por 2 Variables e indicando el tipo de agregacion a cada variable
df_gr_4 = df.groupby('ShipName, ShipperName')[['Quantity', 'UnitPrice']].agg({'Quantity':['sum'], 'UnitPrice':['mean']})

# ========================================================================
#### Tablas Dinamicas
# ========================================================================

pivot_table = df.pivot_table('SalesAmount', index='ShipCountry', columns='ShipperName',aggfunc=[np.sum])

### Rellenando los vacios con 0 y agregando totales
pivot_table = df.pivot('SalesAmount', index='ShipCountry',columns='ShipperName',aggfunc=[np.median, np.sum], fill_value=0, margins=True)

# =============================================================
##### CONCAT & APPEND
# =============================================================
   
path = r('C:\Users\Asus VivoBook\Dropbox\My PC (DESKTOP-GN5CQHE)\Documents\My Studies\PowerUp Institute\Python\week 01\Tiendas\vta_2014.csv')
path = r('C:\Users\Asus VivoBook\Dropbox\My PC (DESKTOP-GN5CQHE)\Documents\My Studies\PowerUp Institute\Python\week 01\Tiendas\vta_2013.csv')
ap1 = pd.read_csv(path1,sep=',',header=0,index_col=False,encoding='Latin-1',engine='python')
ap2 = pd.read_csv(path2,sep=',',header=0,index_col=False,encoding='Latin-1',engine='python')

### Append anexa de forma vertical y deja valores repetidos
ap3 = ap1.append(ap2).reset_index(drop=True)

### Si quisieramos anexar mas de 2 bases ap1.append(ap2).append(ap3)

### Pero es mejor anexando concat pandas nos lleva al sgte nivel
### Concatenar al nivel de la fila
ap4 = pd.concat([ap1,ap2],ignore_index=True, axis=0)

### concatenar a nivel de columna
ap5 = pd.concat([ap1,ap2],ignore_index=True, axis=1))
   
# ========================================================================
#### SORT the Dataset (sort.values)
# ========================================================================

### Ordenando de forma ascendente
sort1 = df.sort_values('ProductID')

### Ordenando de forma descendente
sort2 = df.sort_values('ProductID', ascending=False)

### Ordenando por Multiples Columnas
sort3 = df.sort_values(['ProductID', 'OrderID'])

### Ordenando por multiples columnas y descendente y ascendente
sort4 = df.sort_values(['ProductID', 'OrderID'], ascending=[False, True])
sort4 = df.sort_values(['ProductID', 'OrderID'], ascending=[False, True])

### Ordenando por el indice
sort5 = df.set_index('ShipName').sort_index()

# =============================================================
#### JOIN - MERGE
# =============================================================
import pandas as pd
path3 = r'C:\\Users\\Asus VivoBook\\Dropbox\\My PC (DESKTOP-GN5CQHE)\\Documents\\My Studies\\PowerUp Institute\\Python\\week 01\\Tiendas\\vta_2014.csv')
Precios = pd.ExcelFile(path3).parse(sheet_name='Precios',header=0,index_col=[0,1])
Existencias = pd.ExcelFile(path3).parse(sheet_name='Existencias',header=0,index_col=[0,1])
Catalogo = pd.ExcelFile(path3).parse(sheet_name='Catalogo',header=0,index_col=[0,1])

# ============================================================
# JOIN -- MERGE
# ============================================================
path = r'C:\Users\Asus VivoBook\Dropbox\My PC (DESKTOP-GN5CQHE)\Documents\My Studies\PowerUp Institute\Python\week 04\Combinar Consultas.csv')
Existencias = pd.ExcelFile(path3).parse(sheet_name='Existencias',header=0,index_col=[0,1])
Catalogo = pd.ExcelFile(path3)

########## UNIENDO POR UNA COLUMNA

Inner1 = pd.merge(Existencias,Precios,on = 'Codigo')

########## UNIENDO POR UNA LLAVE EN LAS COLUMNAS (2 O mas)

iNNER2 = pd.merge(Existencias,Precios,on = 'Codigo','Descripcion')

########## UNIENDO LAS COLUMNAS SI SE LLAMARN DIFERENTES

Inner3 = pd.merge(Existencias,Precios,
                  left_on='Codigo',
                  right_on='Codigo')

#### LEFT JOIN

Left1 = pd.merge(Existencias,Precios,
                  left_on='Codigo',
                  right_on='Codigo'
                 how='left').reset_index()


#### RIGHT JOIN

Right1 = pd.merge(Existencias,Precios,
                  left_on='Codigo',
                  right_on='Codigo'
                 how='right')
                 
#### FULL OUTER JOIN 
Outer11 = pd.merge(Existencias,Precios,
                  left_on='Codigo',
                  right_on='Codigo'
                 how='outer')
             
#### REPLACE SPECIAL CHARACTERS
path = r'C:\Users\Asus VivoBook\Dropbox\My PC (DESKTOP-GN5CQHE)\Documents\My Studies\PowerUp Institute\Python\week 04\Cohersion.csv'
df = pd.read_csv(path,sep =';',header=0,index_col=False,encoding='Latin-1',engine='python')
df['Venta'] = df['Venta'].str.strip('$')

#### MODIFY DATA TYPES
df['Venta'] = df['Venta'].astype('float')
df['NroMes'] = df['NroMes'].astype('int')
df['Mes'] = df['Mes'].astype('str')

# ============================================================
#### DATA CLEANSING
# ============================================================

############ ELIMINANDO LOS MESES QUE NO EXISTEN

df.drop(df[df['NroMes']>12].index,inplace=True)

############ ELIMINANDO MIS VALORES DUPLICADOS

df = [df.duplicated(subset='NroMes',keep=False)]


#### DELETE DUPLICATE VALUES
df.drop_duplicates(subset='NroMes',keep='first',inplace=True)
print(df)

########## LIMPIANDO MIS DATOS CATEGORICOS

df_Mes = pd.DataFrame(
    {'Mes':['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo',
            'Junio', 'Julio', 'Agosto', 'Septiembre',
            'Octubre', 'Noviembre', 'Diciembre']})

#### DELETE BLANK_SPACES (strip)
df_Mes['Mes'] = df_Mes['Mes'].str.strip()

######### CALCULANDO LA DIFERENCIA DE UNA LISTA DEFINIDA CON MI COLUMNA
diferencia = set(df['Mes']).difference(df_Mes['Mes'])

########## CREANDO PRUEBA LOGICOS TRUE FALSE PARA MANTENER O DESCARTAR VALORES

diferencia_1 = df['Mes'].isin(diferencia)

########## VALIDAMOS QUE ES LO Q NO ESTA PARA ASEGURARNOSDE QUITARLO

df2 = df[diferencia_1]

########## REMOVEMOS LOS VALORES DEL TRUE DEL BOOL

df2 = df[~diferencia_1] 

########## REEMPLAZANDO VALORES DE UNA COLUMNA POR UN DICCIONARIO

df_reemplazar = {'Enero':'Q1','Febrero':'Q1','Marzo':'Q1',
                 'Abril':'Q2','Mayo':'Q2','Junio':'Q2',
                 'Julio':'Q3','Agosto':'Q3','Septiembre':'Q3',
                 'Octubre':'Q4','Noviembre':'Q4','Diciembre':'Q4'}


########## REEMPLAZAMOS LA LISTA

df2['Mes']= df2['Mes'].replace(df_reemplazar)

########## VALORES PERDIDOS

import numpy as np

df_Mis = pd.DataFrame({
    'Mes':['Enero','Febrero','Marzo','Abril','Mayo',
           'Junio','Julio',np.nan,'Septiembre',
           'Octubre','Noviembre',np.nan]})

print(df_Mis.isna().sum()) ### cuando son mis valores vacios

########## ELIMINANDO VALORES FALTANTES

df.Mis.dropna(subset=['Mes'])

########## RELLENANDO LOS VALORES EN BLANCO

df_mean = np.array([1,2,3,4,5,6,7,8,9,10,11,12]).mean()

df_filna = df_Mis.fillna({'Mes':df_mean})

# ============================================================
# VALIDACION CRUZADA, VALIDANDO LA INTEGRIDAD DE LOS DATOS
# ============================================================

viajes = pd.DataFrame({
    'Aerolineas':['Delta','Avianca','United','TACA','AirFrance'],
    'Mexico_Pasajeros':[10,20,30,40,50],
    'USA_Pasajeros':[10,20,30,40,50],
    'España_Pasajeros':[10,20,30,40,50],
    'Total_Pasajeros':[30,50,90,120,160]},
    columns = ['Aerolineas','Mexico_Pasajeros','USA_Pasajeros',
               'España_Pasajeros','Total_Pasajeros'])

########## SUMAR COLUMNAS

df_v1 = viajes[['Mexico_Pasajeros','USA_Pasajeros', 'España_Pasajeros']].sum(axis=1)

########## REALIZAMOS LA VALIDACION CRUZADA BOOLEANO

Validado = df_v1 == viajes['Total_Pasajeros']

########## FILTRAMOS LOS QUE SI ESTAN OK y LOS QUE NO

Viajes_Buenos = viajes[validado]
viajes_malos = viajes[validado]

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import datetime as dt

path = r'C:\Users\Asus VivoBook\Dropbox\My PC (DESKTOP-GN5CQHE)\Documents\My Studies\PowerUp Institute\Python\week 05\List of Orders.csv'
list_orders = pd.read_csv(path+',sep=',',header=0,index_col=False,
                 encoding='latin-1',engine='python')

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import datetime as dt

path = r'C:\Users\Asus VivoBook\Dropbox\My PC (DESKTOP-GN5CQHE)\Documents\My Studies\PowerUp Institute\Python\week 05'
list_orders = pd.read_csv(path+'\List of Orders.csv',sep=';',header=0,index_col=False,
                 encoding='latin-1',engine='python')
order_details = pd.read_csv(path+'\Order Details.csv',sep=';',header=0,index_col=False,
                 encoding='latin-1',engine='python')

list_orders.head()

# Recordar transformar

list_orders

orders_details.head()

# Recodar transformar 

list_orders['Order Date'] = pd.to_datetime(list_orders['Order Date'])

########## UNIR BASES

df = pd.merge(order_details, list_orders,
              left_on)


########## CREAMOS COLUMNAS DE MES Y AÑO

df['Mes'] = pd.to_datetime(df['Order Date']).dt.month
df['Anio'] = pd.to_datetime(df['Order Date']).dt.year

df_mes = pd.DataFrame(df.groupby(['Mes'])['Amount','Quantity'].sum().reset_index())


########## REALIZAMOS AGRUPACION DE LA BASE A MES  - VTA CANTIDAD

df_mes = pd.DataFrame(df.groupby(['Mes'])[['Amount,'Quantity]].sum()).reset_index()


# *************************************************************
####                     N  U  M  P  Y    
# *************************************************************

# https://numpy.org/doc/stable/user/absolute_beginners.html
import numpy as np
np.version.version
print(dir(np))
help(np.trace)

# =============================================================
#### ARRAYS aka VECTORS
# =============================================================
# With respect to Python, a vector is a one-dimensional array of lists.

#### UNIDIMENSIONAL Arrays
array_01 = np.array([1,2,3,4,5])
arr = np.array([2, 1, 5, 3, 7, 4, 6, 8])

#### Array_Dimension (shape)
array_01.shape

#### Array_Dimension (size)
array_01.size

#### Sort Arrays
np.sort(arr)

#### Array_Indexes
array_01[0]
print("Hello", "...this is are the results after computing today´s workload:", array_01[1], array_01[4])
array_01[-1]

# Create Custom Arrays
array_empty = np.zeros((3,3))
array_ones = np.ones((3,3))
array_full = np.full((3,3), 5)
array_random = np.random.randn(10,4)
arraylinspace= np.linspace(0, 10, num=5)
arraylinspace

#### Optimizing byte_datasize
arrayint64 = np.ones(2, dtype=np.int64)
arrayint64.dtype
arrayint64 = np.ones(2, dtype=np.int32)
arrayint64.dtype
arrayint64 = np.ones(2, dtype=np.int16)
arrayint64.dtype

#### Define a random array with (np.ceil and np.floor)
b = np.array([-1.7, -1.5, -0.2, 0.2, 1.5, 1.7, 2.0])
b
c = np.ceil(b)
c
d = np.floor(b)
d

#### Extract the nearest int which is closer to zero (np.trunc)
e = np.trunc(b)
e

#### Round elements of the array to the nearest integer. (np.rint)
f = np.rint(b)
f

#### Round to nearest integer towards zero.
g = np.fix(3.14)
g

#### Evenly round to the given number of decimals.
h = np.round(16.055, 2)
h

i = np.around([0.37, 1.64], decimals=1)
i

j = np.around([.5, 1.5, 2.5, 3.5, 4.5]) # rounds to nearest even value
j

k = np.around([1,2,3,11], decimals=-1)
k


#### BIDIMENSIONAL Arrays
calificaciones = np.array(
    [
    [60,80,83,80,69,70],
    [0.10, 0.10, 0.10, 0.20, 0.20, 0.30]
    ]
    )

calificaciones.shape

#### Bidimensional Arrays composed by a sequence of values (arange) 
array_02 = np.arange(1,16)

#### Reshaping_Array_Dimensions (reshape)
array_03 = array_02.reshape(3,5)

#### Arrays composed by random values (randbetween)
# Lets create a pair of arrays with randbetween values (1000 values, 2 decimals)
x = np.round(np.random.normal(1.5, 0.05, 1000), 2)
y = np.round(np.random.normal(50.1, 5, 1000), 1)

#### Locate values in Bidimensional Arrays

# Locate values as follows: < : >(on both arrays), positions 2 and 3 (range 2-4)
calificaciones[:,2:4]  
# Display <0> (array 0), <:> all values
notas2 = calificaciones[0,:]

#### Merge Arrays
# Condition: Arrays must share the same dimensions
xy = np.column_stack((x,y))

#### Convert Array_Values from one type to another (dtype)
array_floats= array_01 = np.array([1,2,3,4,5], dtype=float)

#### Convert Lists into Arrays
# 01 Lets begin defining a pair of lists
Notas = [60,80,83,80,69,70]
Porcentaje = [0.10, 0.10, 0.10, 0.20, 0.20, 0.30]
# 02 Convert into Arrays
np_notas = np.array(Notas)
np_porcentaje = np.array(Porcentaje)

#### Convert Arrays into DataFrames
# Arrays contain similar types of objects or elements whereas DataFrame can have objects or multiple or similar data types.

## Numpy to pandas
h = np.array([[1,2],[3,4]])
df_h = pd.DataFrame(h)
print(df_h)
## Pandas to numpy
df_h_n = np.array(df_h)
print(df_h_n)

#### Create Random List
#  Parameters: 10 random values, conditions = Min=1, Max=6)
rolls = np.random.randint(low=1, high=6, size=10)
rolls
type(rolls)
print(dir(rolls))
help(rolls.mean)
rolls.mean()

#### Convert an Array into a List
rolls.tolist()

#### Arrays Arithmetical Ops 
a = np_notas[np_notas > 80]

# Multiplicar las notas x los %
desglose_promedio = np_notas * np_porcentaje

# Utilizamos la funcion Sum para validar la suma de la matriz
Nota_Final = sum(desglose_promedio)
print(sum(desglose_promedio))

#### Find dissimilar objects (setdiff1d)
# Lets create a apair of arrays:
d = np.array([1,2,3,4,5,6,7,8])
e = np.array([1,2,3,6,7,8])
# 
f = np.setdiff1d(d,e)
print(f)

#### Find homologous (counterpart) values (intersect1d)
g = np.intersect1d(d,e)
print(g)

#### Encode / Decode

import base64

# 01. Encode
encoded = base64.b64encode(b'Hello')
print(encoded)
# 02. Decode
data = base64.b64decode(encoded)
print(data)

# ============================================================
####             M  A  T  P  L  O  T  L  I  B
# ============================================================

df['price'].plot.box()
df['price'].plot.box(vert=False)
df['price'].plot()
df['price'].plot.bar()
df['price'].plot.barh()
df['price'].plot.hist(bins=20)
df['price'].diff.hist(bins=20)
df['price'].plot.area()
df['price'].plot.scatter(x='a', y='b')
df['price'].plot.pie(subplots=True)

fig, ax = plt.subplots()
plt.show()

fig, ax = plt.subplots()
ax.plot(df_mes['Mes'],df_mes['Amount'], marker = 'o', linestyle = '--')
ax.plot(df_mes['Mes'],df_mes['Quantity'], marker = 'v', linestyle = '--', color = 'b')
ax.set_xlabel('Mes')
ax.set_ylabel('Sales vs Quantity')
ax.set_title('Monthly Analysis by Sales & Quantity')
plt.show()

########## MOSTRAR 2 GRAFICOS DIFERENTES [Primer argumento filas y luego columnas]
###### El orden de los parentesis cuadrados es [0,1]

fig,ax = plt.subplots(2,1)

#sharey = True nos indica que los ejes en los graficos 

ax[0].plot(df_mes['Mes'], df_mes['Amount'], marker='o', linestyle = '--', color = 'b')
ax[1].plot(df_mes['Mes'], df_mes['Quantity'], marker = 'v', linestyle = None, color = 'g')
ax[0].set_ylabel('Sales')
ax[1].set.ylabel('Quantity')
ax[1].set.xlabel('Mes')
plt.show()


########## GRAFICANDO 2 EJES CON ESCALAS DIFERENTES

fig,a x = plt.subplots()
ax.plot(df_mes['Mes'], df_mes['Amount'], color = 'blue')
ax.set_xlabel('Mes')
ax.set_ylabel('Ventas', color = 'blue')
ax.tick_parrams('y',colors = 'blue')
ax2.ax.twinx()
ax2.plot(df_mes['Mes'], df_mes['Quantity'], color = 'magenta')
ax2.set_ylabel('Cantidad', color = 'magenta')
ax2.tick_params('y', colors = 'magenta')
ax.invert_yaxis() # Invertir ejes
ax.set_ylim(0,70000) # Parametros de Escala
plt.show()
