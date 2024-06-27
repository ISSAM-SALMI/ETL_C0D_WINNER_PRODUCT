import os
import COD_GET_DATA
import Load_Data
import Transform

################
#  EXTRACTION  #
################
print("START_ETL".center(45, "-"))
COD_GET_DATA.Extract("START")
print("END DATA EXTRACTION".center(45, "-"))
################
#  Transform   #
################
print("START TRANSFORM".center(45, "-"))
json_files = [f for f in os.listdir("./DATA") if f.endswith('.json')]
for file_json in json_files :
    Transform.Transform(file_json)
print("END DATA TRANSFORMATION".center(45, "-"))
################
#     Load     #
################
print("START LOAD".center(45, "-"))
config = {
      'user': 'root',
      'password': 'rootissam@@12',
      'host': 'localhost',
      'database': 'COD_NETWORK',
      'raise_on_warnings': True
    }
csv_files = [f for f in os.listdir("./DATA") if f.endswith('.csv')]
for file in csv_files :
    Load_Data.load_data_from_csv_to_mysql(file, file.split(".")[0], config)
print("END DATA LOAD".center(45, "-"))
