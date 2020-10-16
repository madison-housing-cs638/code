import os
import urllib3
import pandas as pd

def download_file(url, path):
    chunk_size = 255

    http = urllib3.PoolManager()
    r = http.request('GET', url, preload_content=False)

    with open(path, 'wb') as out:
        while True:
            data = r.read(chunk_size)
            if not data:
                break
            out.write(data)

    r.release_conn()

DATA_PATH = 'temp_data'

DATASETS = {
  "all_parcel_assessments.csv": "https://raw.githubusercontent.com/madison-housing-cs638/data/master/all_parcel_assessments.csv",
  "all_parcel_names.csv": "https://raw.githubusercontent.com/madison-housing-cs638/data/master/all_parcel_names.csv",
  "all_parcel_sales.csv": "https://raw.githubusercontent.com/madison-housing-cs638/data/master/all_parcel_sales.csv",
  "all_parcel_locations.csv": "https://raw.githubusercontent.com/madison-housing-cs638/data/master/all_parcel_locations.csv",
  "single_family_locations.csv": "https://raw.githubusercontent.com/madison-housing-cs638/data/master/single_family_locations.csv",
  "single_family_names.csv": "https://raw.githubusercontent.com/madison-housing-cs638/data/master/single_family_names.csv",
  "single_family_sales.csv": "https://raw.githubusercontent.com/madison-housing-cs638/data/master/single_family_sales.csv",
  "all_parcel_core.csv": "https://raw.githubusercontent.com/madison-housing-cs638/data/master/all_parcel_core.csv",
  "single_family_core.csv": "https://raw.githubusercontent.com/madison-housing-cs638/data/master/single_family_core.csv",
  "year_sales.csv": "https://raw.githubusercontent.com/madison-housing-cs638/data/master/year_sales.csv",
}

def download_datasets():
  for f in DATASETS:
      filePath = os.path.join(os.pardir, DATA_PATH, f)
      fileUrl = DATASETS[f]
      download_file(fileUrl, filePath)

def load_csv_datasets(*datasets): #Returns a tupple of pandas dataframes.
    result = []
    for datasetName in datasets:
        fullPath = os.path.join(os.pardir, DATA_PATH, datasetName + '.csv')
        df = pd.read_csv(fullPath)
        if("Parcel" in df.columns):
            df["Parcel"] = df["Parcel"].astype("str")
            df.set_index("Parcel", inplace=True)
        result.append(df)
    return tuple(result)
