import os
import zipfile


zip_path = 'data-analysis-projects/videogamesales.zip'     # zip path
extract_dir = os.path.splitext(zip_path)[0]              # folder name


# extract all files inside the folder (extract_dir)
with zipfile.ZipFile(zip_path, 'r') as zip_ref:
    zip_ref.extractall(extract_dir)                         

# filters out only the files that ends with .csv
csv_file = [f for f in os.listdir(extract_dir) if f.endswith('.csv')]

try: 
    csv_path = os.path.join(extract_dir, zip_path[0])

except Exception as e:
    print(f"Error  :  {e}")