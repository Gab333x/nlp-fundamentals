# AG News Dataset

This directory should contain the AG News Classification dataset files.

## Download Instructions

1. Visit the dataset page: [AG News Classification Dataset on Kaggle](https://www.kaggle.com/datasets/amananandrai/ag-news-classification-dataset)

2. Download the following files:
   - `train.csv` (28MB, 120,000 samples)
   - `test.csv` (1.7MB, 7,600 samples)

3. Place them in this directory:
   ```
   classification/data/
   ├── train.csv
   └── test.csv
   ```

## Dataset Details

### Format
```
Class Index, Title, Description
```

### Classes
- **1**: World
- **2**: Sports
- **3**: Business  
- **4**: Sci/Tech

### Statistics
- **Training samples**: 120,000
- **Test samples**: 7,600
- **Total**: 127,600 news articles
- **Balanced**: 30,000 samples per class (train)

## Alternative: Programmatic Download

If you have Kaggle API configured:

```bash
pip install kaggle

# Place your kaggle.json in ~/.kaggle/
kaggle datasets download -d amananandrai/ag-news-classification-dataset
unzip ag-news-classification-dataset.zip
```

## Verification

After downloading, verify the files:

```python
import pandas as pd

# Load and check
train = pd.read_csv('train.csv')
test = pd.read_csv('test.csv')

print(f"Train shape: {train.shape}")  # Should be (120000, 3)
print(f"Test shape: {test.shape}")    # Should be (7600, 3)
print(f"Classes: {train.iloc[:, 0].unique()}")  # Should be [1, 2, 3, 4]
```

Expected output:
```
Train shape: (120000, 3)
Test shape: (7600, 3)
Classes: [1 2 3 4]
```

## Troubleshooting

**Issue**: Files not loading

**Check**:
1. Files are in correct directory
2. File names are exactly `train.csv` and `test.csv`
3. Files are not corrupted (check file sizes)

**Issue**: Kaggle download not working

**Solution**: Download manually from the web interface

