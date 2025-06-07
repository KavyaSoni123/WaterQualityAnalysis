from cleaner import load_and_clean_data
import os

raw_data_dir = 'data/Gemstat_Dataset_raw'
cleaned_data_dir = 'data/Gemstat_Data_Cleaned_Raw'

os.makedirs(cleaned_data_dir, exist_ok=True)

for folder_name in os.listdir(raw_data_dir):
    folder_path = os.path.join(raw_data_dir, folder_name)
    if os.path.isdir(folder_path):
        samples_csv_path = os.path.join(folder_path, 'samples.csv')
        metadata_xlsx_path = os.path.join(folder_path, 'metadata.xlsx')
        
        if os.path.exists(samples_csv_path) and os.path.exists(metadata_xlsx_path):

            cleaned_data = load_and_clean_data(samples_csv_path, metadata_xlsx_path)
            
            cleaned_folder_path = os.path.join(cleaned_data_dir, folder_name)
            os.makedirs(cleaned_folder_path, exist_ok=True)
            cleaned_data.to_csv(os.path.join(cleaned_folder_path, 'cleaned_samples.csv'), index=False)