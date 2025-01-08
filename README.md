# Water Quality Analysis Project

## Overview
This project focuses on analyzing water quality using a combination of satellite data and in-situ measurements. The primary data sources include Sentinel-2 satellite imagery accessed through the Google Earth Engine (GEE) API and the Gloria dataset, which provides water quality data for major lakes in the USA. By integrating these datasets, the project aims to explore the relationship between satellite-derived parameters and water quality indicators such as chlorophyll-a, turbidity, and more.

## Features
- Fetching Sentinel-2 satellite data using the GEE API in Python.
- Utilizing the Gloria dataset, which includes detailed water quality measurements.
- Joining satellite band data with Gloria dataset features for comprehensive analysis.
- Leveraging spectral bands (B2 to B12) from Sentinel-2 to derive insights into water quality parameters.

## Dataset Details
### Gloria Dataset
- **Columns Used**:
  - `Site_name`
  - `Country`
  - `Country_code`
  - `Latitude`
  - `Longitude`
  - `Date_Time_UTC`
  - `Water_body_type`
  - `Water_type`
  - `Depth`
  - `Chla` (Chlorophyll-a)
  - `TSS` (Total Suspended Solids)
  - `Turbidity`
  - `Secchi_depth`
  - `Chla_plus_phaeo`
  - `aCDOM440`
  - `Date`
  - `Time`

### Sentinel-2 Satellite Data
- **Bands Used**:
  - B2 (Blue)
  - B3 (Green)
  - B4 (Red)
  - B5 (Red Edge 1)
  - B6 (Red Edge 2)
  - B7 (Red Edge 3)
  - B8 (Near Infrared)
  - B8A (Narrow NIR)
  - B12 (Shortwave Infrared)

## Tools and Technologies
- **Google Earth Engine (GEE)**: To fetch Sentinel-2 satellite data.
- **Python**: For data processing and integration.
- **Pandas**: For data manipulation and joining.
- **Geospatial Libraries**: Such as `geopandas` or `shapely` for handling spatial data.

## Methodology
1. **Fetching Satellite Data**:
   - Used the GEE API to retrieve Sentinel-2 bands for specific locations and dates corresponding to the Gloria dataset.

2. **Data Preprocessing**:
   - Cleaned and prepared the Gloria dataset.
   - Extracted relevant satellite bands and matched them with in-situ measurements.

3. **Data Integration**:
   - Joined satellite band data with Gloria dataset columns based on location and time.

4. **Analysis**:
   - Explored relationships between spectral bands and water quality parameters.
   - Developed visualizations and models to understand water quality dynamics.

## Repository Structure
```
water-quality-analysis/
├── data/                     # Contains raw and processed data files
├── notebooks/                # Jupyter notebooks for data exploration and analysis
├── scripts/                  # Python scripts for data fetching and processing
├── results/                  # Outputs and visualizations
├── README.md                 # Project documentation
└── requirements.txt          # List of dependencies
```

## Installation
1. Clone the repository:
   ```bash
   git clone <repository_url>
   cd water-quality-analysis
   ```
2. Create a virtual environment and activate it:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage
1. Fetch Sentinel-2 data using the `gee_fetch.py` script in the `scripts` directory.
2. Process and join data using the Jupyter notebooks in the `notebooks` directory.
3. Run analysis and generate visualizations or models.

## Results
Key insights from the project include correlations between Sentinel-2 spectral bands and water quality parameters such as:
- Chlorophyll-a concentrations.
- Turbidity and total suspended solids.
- Secchi depth transparency.

## Data Insights
Below is the `df.info()` summary for each lake analyzed in the project:

- **Lake Erie**:
  <img width="390" alt="Screenshot 2025-01-08 at 3 33 35 PM" src="https://github.com/user-attachments/assets/ccec0185-11fb-4884-8702-2cabdd1849b8" />

- **Gulf of Mexico, FL**:
  <img width="398" alt="Screenshot 2025-01-08 at 3 34 36 PM" src="https://github.com/user-attachments/assets/2abe6cda-ba56-40eb-beff-075c81376d8b" />

- **Lake Geneva**:
  <img width="405" alt="Screenshot 2025-01-08 at 3 36 11 PM" src="https://github.com/user-attachments/assets/ddb925ca-2c3b-4d0a-b6ba-05f869bdbb1e" />

- **IJsselmeer**:
 <img width="400" alt="Screenshot 2025-01-08 at 3 36 58 PM" src="https://github.com/user-attachments/assets/f076e5d6-a900-42a2-8d16-a5438deb6bb2" />

- **Guiana**:
  <img width="394" alt="Screenshot 2025-01-08 at 3 37 43 PM" src="https://github.com/user-attachments/assets/5bb63c10-26a7-4f5f-9ba3-fe0c602ce227" />

- **Gulf of Mexico**:
<img width="394" alt="Screenshot 2025-01-08 at 3 38 41 PM" src="https://github.com/user-attachments/assets/8227ef52-fcb5-4943-b2b1-e4c0c2904dc8" />

- **Taihu**:  
<img width="398" alt="Screenshot 2025-01-08 at 3 39 32 PM" src="https://github.com/user-attachments/assets/d8584654-cf86-457e-9690-270f3532c96f" />

- **English Channel**:
<img width="394" alt="Screenshot 2025-01-08 at 3 41 38 PM" src="https://github.com/user-attachments/assets/0c8fc30b-d726-472b-bb4f-67f033cd15a4" />

- **Garda**:  
<img width="397" alt="Screenshot 2025-01-08 at 3 42 23 PM" src="https://github.com/user-attachments/assets/1aec2434-86ba-4048-8dad-aa1b7d29cc3d" />

- **Lake Kasumigaura**:  
<img width="394" alt="Screenshot 2025-01-08 at 3 43 09 PM" src="https://github.com/user-attachments/assets/0fe3f889-2591-46d9-9c42-142c3002d4f6" />

- **Chesapeake Bay, MD**:  
<img width="395" alt="Screenshot 2025-01-08 at 3 43 58 PM" src="https://github.com/user-attachments/assets/4f96f6c8-602e-4603-abc7-246c2303ef57" />

- **Atlantic Ocean, GA**:  
<img width="392" alt="Screenshot 2025-01-08 at 3 44 34 PM" src="https://github.com/user-attachments/assets/3ea61eb4-40e2-4041-a132-c208a766e780" />

## Future Work
- Expand the analysis to include additional water bodies globally.
- Apply machine learning models to predict water quality parameters.
- Incorporate other remote sensing datasets for enhanced analysis.

## Contributors
- **Kavya Soni**

## License
This project is licensed under the MIT License. See the LICENSE file for details.

