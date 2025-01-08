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

- **Lake 1**:
  ```plaintext
  <DataFrame info for Lake 1>
  ```

- **Lake 2**:
  ```plaintext
  <DataFrame info for Lake 2>
  ```

(Add similar summaries for each lake included in the analysis.)

## Future Work
- Expand the analysis to include additional water bodies globally.
- Apply machine learning models to predict water quality parameters.
- Incorporate other remote sensing datasets for enhanced analysis.

## Contributors
- **Kavya Soni**

## License
This project is licensed under the MIT License. See the LICENSE file for details.

