# 🌊 Water Quality Analysis Project

## 📌 Overview  
This project focuses on analyzing **water quality** by integrating **Sentinel-2 satellite imagery** with **in-situ water quality measurements**. The primary data sources include:  

- **Sentinel-2 satellite imagery** via **Google Earth Engine (GEE) API**  
- **Gemstat dataset**, which provides water quality data for major lakees in the world  

By leveraging spectral bands from Sentinel-2, the project aims to explore correlations between **satellite-derived parameters** and **water quality indicators** such as **chlorophyll-a, turbidity, total suspended solids (TSS), and more**.  

---

## 🚀 Features  
✅ Fetching **Sentinel-2 satellite data** using **Google Earth Engine (GEE) API** in Python  
✅ Integrating **Gloria dataset** with spectral band information  
✅ Performing **feature selection** to identify key **water quality indicators**  
✅ **Analyzing correlations** between spectral bands and water parameters  
✅ **Visualizing results** to interpret water quality trends  

---

## 🎯 Recommended Target Variables  

The following **water quality indicators** are selected as target variables due to their strong correlation with spectral bands:  

### **1️⃣ Chlorophyll-a (Chl-a)**  
🔹 **Reason**: Correlates strongly with **B4 (red), B5 (red-edge), B6, B7 (red-edge/NIR), and B8 (NIR)**  
🔹 **Significance**: Chlorophyll absorbs blue/red light and reflects NIR, making it detectable via satellite  

### **2️⃣ Turbidity (TURB)**  
🔹 **Reason**: Higher turbidity increases light scattering, affecting **B2 (blue), B3 (green), and B4 (red)**  
🔹 **Significance**: Directly linked to sedimentation, pollution, and water clarity  

### **3️⃣ Total Suspended Solids (TSS)**  
🔹 **Reason**: Strongly related to **B2 (blue), B3 (green), B4 (red), and B8 (NIR)**  
🔹 **Significance**: High TSS levels indicate sediment content and pollution  

### **4️⃣ Dissolved Organic Carbon (DOC)**  
🔹 **Reason**: Affects UV/blue light absorption, detected in **B2 (blue) and B3 (green)**  
🔹 **Significance**: Influences water color and dissolved matter concentration  

### **5️⃣ Total Phosphorus (TP) & Total Nitrogen (TN)**  
🔹 **Reason**: Key nutrients for **algal blooms**, impacting reflectance in **B5, B6, and B7 (red-edge bands)**  
🔹 **Significance**: Essential for **eutrophication** studies  

### **6️⃣ Dissolved Oxygen (O2-Dis)**  
🔹 **Reason**: Related to biological activity, inferred through **Chl-a, turbidity, and DOC**  
🔹 **Significance**: Critical for assessing **water health** and **ecosystem balance**  

### **7️⃣ Electrical Conductivity (EC) & Total Dissolved Solids (TDS)**  
🔹 **Reason**: High salt content influences **B11 (SWIR1) and B12 (SWIR2)**  
🔹 **Significance**: Important for measuring **water salinity** and **pollution levels**  

💡 **Note**: Heavy metals (**Pb-Tot, Hg-Tot, Ni-Tot**) are **not selected** as they are not directly detectable via remote sensing.

---

## 🛰️ Sentinel-2 Satellite Data  

### **🔹 Spectral Bands Used**
| Band  | Name                  | Wavelength (nm) | Primary Use |
|-------|-----------------------|----------------|-------------|
| B2    | **Blue**              | 490            | Water clarity, turbidity |
| B3    | **Green**             | 560            | Vegetation, water quality |
| B4    | **Red**               | 665            | Chlorophyll absorption |
| B5    | **Red Edge 1**        | 705            | Vegetation stress, water quality |
| B6    | **Red Edge 2**        | 740            | Algal blooms, suspended matter |
| B7    | **Red Edge 3**        | 783            | Nutrient levels, chlorophyll |
| B8    | **Near Infrared (NIR)** | 842          | Biomass, algae detection |
| B8A   | **Narrow NIR**        | 865            | Water quality analysis |
| B11   | **Shortwave Infrared 1 (SWIR1)** | 1610 | Suspended solids, salinity |
| B12   | **Shortwave Infrared 2 (SWIR2)** | 2190 | Organic matter, pollutants |

📌 **Why These Bands?**  
These bands cover the **visible (B2-B4), near-infrared (B5-B8A), and shortwave infrared (B11, B12)** spectrum, which are **optimal for detecting water quality changes**.  

---

## 🛠️ Tools & Technologies  

- **🌍 Google Earth Engine (GEE)** → Fetch Sentinel-2 data  
- **🐍 Python** → Data processing & integration  
- **📊 Pandas** → Data manipulation & feature engineering  
- **🌍 Geospatial Libraries (geopandas, shapely)** → Handling spatial data  

---

## 🔧 Setup Instructions  

1️⃣ **Create Environment & Install Dependencies**  
```bash
python -m venv water_quality_env
source water_quality_env/bin/activate   # On macOS/Linux
water_quality_env\Scripts\activate      # On Windows
pip install earthengine-api pandas geopandas
```

2️⃣ **Authenticate Google Earth Engine (Only Once)**  
```bash
earthengine authenticate
```

3️⃣ **Run the Analysis**  
```bash
python water_quality_analysis.py
```

---

## 📌 Future Improvements  

- ✅ Incorporate **machine learning models** for water quality prediction  
- ✅ Improve **visualizations** for better data interpretation  
- ✅ Extend analysis to **different water bodies & seasons**  

---

## 📜 License  
This project is **open-source** under the **MIT License**.  

---

### **📬 Have Questions?**  
Feel free to reach out or contribute to the project! 🚀  

---
