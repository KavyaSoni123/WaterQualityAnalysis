from datetime import datetime
import ee


def print_oldest_dates(AOI):
    S2 = (
        ee.ImageCollection("COPERNICUS/S2_SR_HARMONIZED")
        .filterBounds(AOI)
        .sort("system:time_start", True)
    )  # Sort by time in ascending order

    oldest_images = S2.limit(10)

    def get_metadata(image):
        timestamp_ms = image["properties"]["system:time_start"]
        cloud_coverage = image["properties"]["CLOUDY_PIXEL_PERCENTAGE"]
        readable_date = datetime.utcfromtimestamp(timestamp_ms / 1000).strftime(
            "%Y-%m-%d %H:%M:%S"
        )
        return {"Date": readable_date, "Cloud Coverage": cloud_coverage}

    image_metadata = [
        get_metadata(image) for image in oldest_images.toList(10).getInfo()
    ]

    for i, metadata in enumerate(image_metadata):
        print(f"Image {i + 1}:")
        print(f"  Date: {metadata['Date']}")
        print(f"  Cloud Coverage: {metadata['Cloud Coverage']}%\n")
