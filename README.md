# Letterboxd Movie Recommender

A movie recommendation system built using Letterboxd user ratings data.

## Dataset

This project uses the [Letterboxd Movie Ratings Data](https://www.kaggle.com/datasets/samlearner/letterboxd-movie-ratings-data) from Kaggle, which contains:


**Attribution**: Dataset created by Sam Learner, licensed under CC BY 4.0

## Quick Setup

### 1. Clone and Setup Environment

```bash
git clone <your-repo-url>
cd letterboxd-recommender
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### 2. Configure Kaggle API

1. Create a Kaggle account and go to your [Account settings](https://www.kaggle.com/account)
2. Click "Create New API Token" to download `kaggle.json`
3. Place the file in your home directory:
   ```bash
   # Linux/Mac
   mkdir ~/.kaggle
   mv ~/Downloads/kaggle.json ~/.kaggle/
   chmod 600 ~/.kaggle/kaggle.json
   
   # Windows
   mkdir %USERPROFILE%\.kaggle
   move %USERPROFILE%\Downloads\kaggle.json %USERPROFILE%\.kaggle\
   ```

### 3. Download Dataset

```bash
python scripts/download_data.py
```

