# SquareYards Apartment Scraper

## Description
Scrapes the first 100 ready-to-move **apartments** for sale in Bangalore from SquareYards. Outputs key details in CSV.

## Setup
1. Install dependencies:
   ```
   pip install -r requirements.txt
   ```
2. Ensure Chrome & ChromeDriver are installed (matching versions).

## Usage
```
python scraper.py
```

Output: `apartments_data.csv` with columns:
- Apartment Name
- Location
- Minimum Price
- Maximum Price
- Photo URL
- Listing URL
