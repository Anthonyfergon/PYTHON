# _____________________________________________________________________
#                           PYTHON_LIBRARIES
#               Prepared by AnthonyCRENG28, Rabbit industries.      
# _____________________________________________________________________

#### UPGRADE_PACKAGES
# conda update <packages_name> //recommended
# pip install --upgrade <packages_name>

#### PANDAS
# Aim: Provides high-level data structures and functions designed to make working with structured or tabular data
# Area: Data analysis and manipulation.
# Official_Site: https://pandas.pydata.org/
# Guides: https://pandas.pydata.org/docs/getting_started/index.html#getting-started
# Correlated libraries: Numpy, Matplotlib, Scipy, scikit-learn, statsmodel
# Books: Python for Data Analysis, 
import pandas as pd
pd.__version__
pd.show_versions(as_json=False)
# PowerShell:
# pip list (anaconda(Prompt))
# pip freeze
# pip show pandas

#### NUMPY
# Aim: Multidimensional array and matrices.
# Source: https://numpy.org/devdocs/user/quickstart.html
import numpy as np

#### SCIKIT LEARN
# Aim: Machine Learning Algorithms
# Source: https://scikit-learn.org/stable/install.html
import sklearn

#### PYTHON-CORE
# Aim: No info.
# Derived from: Oracle VM - Dataiku Env
# Source: https://pypi.org/project/python-core/
pip install python-core

#### PYWIN32
# Aim: This is the readme for the Python for Win32 (pywin32) extensions, which provides access to many of the Windows APIs from Python.
# Derived from: Oracle VM - Dataiku Env
# Source: https://pypi.org/project/pywin32/
pip install pywin32

#### ANNOY
# Aim: Approximate Nearest Neighbors in C++/Python optimized for memory usage and loading/saving to disk.
# Area: Machine Learning - Scikit Learn
# Source: https://pypi.org/project/annoy/
# https://anaconda.org/conda-forge/python-annoy
conda install -c conda-forge python-annoy
conda install -c "conda-forge/label/broken" python-annoy
conda install -c "conda-forge/label/cf201901" python-annoy
conda install -c "conda-forge/label/cf202003" python-annoy
conda install -c "conda-forge/label/gcc7" python-annoy 

#### SCIKIT-LEARN
# Aim: Simple and efficient tools for predictive data analysis
# Area: Machine Learning
# Source: https://scikit-learn.org/stable/
pip install -U scikit-learn
conda install scikit-learn
# Books
# Scikit Learn User Guide (C:\Users\Asus VivoBook\Dropbox\My PC (DESKTOP-GN5CQHE)\Desktop\Documentos\The Vault\Python\PYTHON_MACHINE_LEARNING\SCIKIT LEARN\SCIKIT LEARN BOOKS)

#### MATPLOTLIB
# Aim: Matplotlib is a comprehensive library for creating static, animated, and interactive visualizations
# Area:Visualization
# Source: https://matplotlib.org/
# https://matplotlib.org/stable/users/installing/index.html
python -m pip install -U pip
python -m pip install -U matplotlib
import matplotlib as mpl
import matplotlib.pyplot as plt
# Books
# Matplotlib (C:\Users\Asus VivoBook\Dropbox\My PC (DESKTOP-GN5CQHE)\Desktop\Documentos\The Vault\Python\MATPLOTLIB)

#### SEABORN
# Aim: Seaborn is a comprehensive library for creating static, animated, and interactive visualizations
# Area:Visualization
# Source: https://seaborn.pydata.org/
pip install seaborn
conda install seaborn

# Books
# Matplotlib (C:\Users\Asus VivoBook\Dropbox\My PC (DESKTOP-GN5CQHE)\Desktop\Documentos\The Vault\Python\MATPLOTLIB)


#### PyMONGO
# Aim: is a Python distribution containing tools for working with MongoDB, and is the recommended way to work with MongoDB from Python
# Area: Non-Relational Database: MongoDB/MongoAtlas
# Source: https://pymongo.readthedocs.io/en/stable/
# https://pypi.org/project/pymongo/
pip install pymongo

#### SciPy
# Aim: SciPy provides algorithms for optimization, integration, interpolation, eigenvalue problems, algebraic equations, differential equations, statistics and many other classes of problems.
# Area: Statistics
# Source: https://scipy.org/
# https://pypi.org/project/pymongo/
pip3 install scipy
conda install scipy

#### Statsmodels
# Aim:  Provides classes and functions for the estimation of many different statistical models, as well as for conducting statistical tests, and statistical data exploration.
# Area: Statistics
# Source: https://www.statsmodels.org/stable/index.html
pip install statsmodels

#### PyKafka
# Aim: 
# Area: Streaming Data
# Source: https://pykafka.readthedocs.io/en/latest/
pip install pykafka

#### Datetime
# Aim:  Supplies classes for manipulating dates and times.
# Area: Dates manipulation
# Source: https://docs.python.org/3/library/datetime.html
# https://pypi.org/project/DateTime/
pip install DateTime
import datetime as dt
from datetime import datetime, date, time, timedelta

#### Pytz
# Aim:  Brings the Olson tz database into Python.
# Area: This library allows accurate and cross platform timezone calculations
# Source: https://pypi.org/project/pytz/
# https://pypi.org/project/DateTime/
pip install pytz
from pytz import timezone

#### PySpark
# Aim:  PySpark is an interface for Apache Spark in Python which facilitates the analysys of data in a distributed environment (clusters)
# Area: Apache Spark, the fast, general and open-source engine for big data processing
# Source: https://spark.apache.org/docs/latest/api/python/getting_started/index.html
pip install pyspark
pip install pyspark[sql]
conda create -n pyspark_env
conda activate pyspark_env
# PySpark dependencies:
    # PySpark RDD (pyspark.RDD)
    # PySpark DataFrame and SQL (pyspark.sql)
    # PySpark Streaming (pyspark.streaming)
    # PySpark MLib (pyspark.ml, pyspark.mllib)
    # PySpark GraphFrames (GraphFrames)
    # PySpark Resource (pyspark.resource) It’s new in PySpark 3.0

#### PyArrow
# Aim: Is a development platform for in-memory analytics.
# Area: PySpark dependency
# Source: https://arrow.apache.org/docs/python/index.html
pip install pyarrow
import pyarrow as pa
import pyarrow.parquet as pq
import pyarrow.compute as pc
import pyarrow.dataset as ds

#### Py4J
# Aim: Enables Python programs running in a Python interpreter to dynamically access Java objects in a Java Virtual Machine
# Area: PySpark dependency
# Source: https://www.py4j.org/
pip install py4j
from py4j.java_gateway import JavaGateway
import py4j.GatewayServer;

#### PyForest
# Aim: Pyforest lazily-imports all popular Python Data Science and Machine Learning libraries 
# Area: Almost Everything
# Source: https://faun.pub/pyforest-lazy-import-python-libraries-3272a3c33d30
pip install --upgrade pyforest
import pyforest

#### Pprint
# Aim: The pprint module provides a capability to “pretty-print” arbitrary Python data structures in a well-formatted and more readable way.
# Area: Almost Everything
# Source: hhttps://docs.python.org/3/library/pprint.html
pip install pprintpp
from pprint import pprint

#### tesseract
# Aim: Tesselation based Recovery of Amorphous halo Concentrations
# Area: OCR
# Source: https://pypi.org/project/tesseract/
pip install tesseract


#### pytesseract
# Aim: Python-tesseract is a python wrapper for Google's Tesseract-OCR
# Area: OCR
# Source: https://pypi.org/project/pytesseract/
pip install pytesseract
from pytesseract import*

#### pillow
# Aim: Python Imaging Library (Fork)
# Area: OCR
# Source: https://pypi.org/project/Pillow/
pip install pillow
from PIL import Image

#### os
# Aim: a big lib with many usefull tools and it are not only os and sys tools...
# Area: OS
# Source: https://pypi.org/project/os-sys/
pip install os-sys
import os

#### pyspark.pandas
# Aim: Pandas API in Spark
# Area: Pandas API in Spark
# Source: https://pypi.org/project/pyspark-pandas/
pip install pyspark-pandas
import pyspark.pandas as ps

#### findspark
# Aim: Find pyspark to make it importable.
# Area: pyspark
# Source: https://pypi.org/project/findspark/
pip install findspark
import findspark
findspark.init() 
    
#### dataiku
# Aim: Python API client for Dataiku APIs
# Area: dataiku/python
# Source: https://pypi.org/project/dataiku-api-client/
pip install dataiku-api-client
    
#### Google_Cloud_BigQuery
# Aim: Google_Cloud_BigQuery
# Area: Google_Cloud_BigQuery
# Source: https://pypi.org/project/google-cloud-bigquery/
pip install google-cloud-bigquery
    
#### pyforest
# Aim: Lazy-import of all popular Python Data Science libraries. Stop writing the same imports over and over again.
# Area: Data Science libraries
# Source: https://pypi.org/project/pyforest/
pip install pyforest
    
#### psycopg2
# Aim: psycopg2 - Python-PostgreSQL Database Adapter
# Area: PostgreSQL
# Source: https://pypi.org/project/psycopg2/
pip install psycopg2
    
#### pybase64
# Aim: Encode datafiles
# Area: Encrypt/Decrypt
# Source: https://pypi.org/project/pybase64/
pip install pybase64
    
#### 
# Aim: 
# Area: 
# Source:
    
    









