import json
import sys
import pandas as pd
import pandas.dataframe as dataframe

try:
    with open(sys.argv[1]) as data:
     df= pd.read.json("/resources/mock_data.json")
       return df.filter[df[location_id[1:5]]
except FileNotFoundError:
    print("File not found, please check your path")
