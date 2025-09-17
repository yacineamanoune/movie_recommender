import os
import kaggle
from pathlib import Path

def download_letterboxd_data():

    dataset = 'samlearner/letterboxd-movie-ratings-data'

    data_dir = Path('data')
    data_dir.mkdir(exist_ok=True)
    
    print("Downloading Letterboxd dataset from Kaggle...")
    print(f"Dataset: {dataset}")
    print(f"Destination: {data_dir.absolute()}")
    
    try:
        kaggle.api.dataset_download_files(
            dataset, 
            path=str(data_dir), 
            unzip=True
        )
        
        print(" Download completed successfully!")
        
        
        print("\nDownloaded files:")
        for file in data_dir.glob("*.csv"):
            size_mb = file.stat().st_size / (1024 * 1024)
            print(f"  📁 {file.name} ({size_mb:.1f} MB)")
            
    except Exception as e:
        print(f" Download failed: {e}")

if __name__ == "__main__":
    download_letterboxd_data()