import ee

try:
    # Initialize the Earth Engine API
    if ee.Initialize(project="ee-sujalrajput10"):
        print(
            "\033[92mGoogle Earth Engine authentication successful!\033[0m"
        )  # Green text
    else:
        print(
            "\033[91mGoogle Earth Engine authentication failed. Please authenticate again.\033[0m"
        )  # Red text

except Exception as e:
    print(
        "\033[91mGoogle Earth Engine authentication failed. Error:\033[0m", str(e)
    )  # Red text
