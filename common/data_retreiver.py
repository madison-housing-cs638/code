import os
import urllib3
import pandas as pd
import geopandas as gpd

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

FAMILY_DATASETS = {
    "single_family_core.csv": DATASETS["single_family_core.csv"],
    "year_sales.csv": DATASETS["year_sales.csv"],
    "single_family_sales.csv": DATASETS["single_family_sales.csv"],
    "year_sales.csv": DATASETS["year_sales.csv"]
}

GEO_DATA = {
    "single_family_areas_shapes.zip": "https://raw.githubusercontent.com/madison-housing-cs638/data/master/single_family_areas_shapes.zip"
}

def download_datasets():
  for f in DATASETS:
      filePath = os.path.join(os.pardir, DATA_PATH, f)
      fileUrl = DATASETS[f]
      download_file(fileUrl, filePath)

def download_family_datasets():
    for f in FAMILY_DATASETS:
      filePath = os.path.join(os.pardir, DATA_PATH, f)
      fileUrl = FAMILY_DATASETS[f]
      download_file(fileUrl, filePath)

def download_geo_data():
    for f in GEO_DATA:
      filePath = os.path.join(os.pardir, DATA_PATH, f)
      fileUrl = GEO_DATA[f]
      download_file(fileUrl, filePath)

def load_geo_datasets(*datasets):
    result = []
    for datasetName in datasets:
        fullPath = os.path.join(os.pardir, DATA_PATH, datasetName + '.zip')
        geo_df = gpd.read_file(f"zip://{fullPath}")
        result.append(geo_df)
    return tuple(result)

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
