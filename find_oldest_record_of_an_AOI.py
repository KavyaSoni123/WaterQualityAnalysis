from datetime import datetime
import ee
from config import PROJECT_ID

try:
    ee.Initialize(project=PROJECT_ID)
except Exception as e:
    print("Error initializing Earth Engine:", e)


AOI = ee.Geometry.Polygon(
    [
        [-97.63949, 15.86973],  # Bottom-left (Min Lon, Min Lat)
        [-97.63949, 16.06973],  # Top-left (Min Lon, Max Lat)
        [-97.43949, 16.06973],  # Top-right (Max Lon, Max Lat)
        [-97.43949, 15.86973],  # Bottom-right (Max Lon, Min Lat)
    ]
)


# Define the Image Collection
S2 = (
    ee.ImageCollection("COPERNICUS/S2_SR_HARMONIZED")
    .filterBounds(AOI)
    .sort("system:time_start", True)
)  # Sort by time in ascending order (oldest first)

# Get the first 10 images
oldest_images = S2.limit(10)


def get_metadata(image):
    # image is already a dictionary here, directly access the properties
    timestamp_ms = image["properties"]["system:time_start"]
    cloud_coverage = image["properties"]["CLOUDY_PIXEL_PERCENTAGE"]

    # Convert timestamp to a human-readable format
    readable_date = datetime.utcfromtimestamp(timestamp_ms / 1000).strftime(
        "%Y-%m-%d %H:%M:%S"
    )

    return {"Date": readable_date, "Cloud Coverage": cloud_coverage}


# Get metadata for the 10 oldest images
# getInfo() is called on the whole list, not individual images
image_metadata = [get_metadata(image) for image in oldest_images.toList(10).getInfo()]

# Print metadata
for i, metadata in enumerate(image_metadata):
    print(f"Image {i + 1}:")
    print(f"  Date: {metadata['Date']}")
    print(f"  Cloud Coverage: {metadata['Cloud Coverage']}%\n")
