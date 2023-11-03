"""
 Analysis Example
 Get Device List

 This analysis retrieves the device list of your account and print to the console.
 There are examples on how to apply filter.
"""
from tagoio_sdk import Analysis, Resources
from tagoio_sdk.types import DeviceInfoList


def get_device_list() -> list[DeviceInfoList]:
    """Retrieves the device list of your account.

    Returns:
        list[DeviceInfoList]: List of devices
    """
    # Example of filtering devices by Tag.
    # You can filter by: name, last_input, last_output, bucket, etc.
    my_filter = {
        "tags": [
            {"key": "keyOfTagWeWantToSearch", "value": "valueOfTagWeWantToSearch"}
        ],
        # "bucket": "55d269211a2e236c25bb9859",
        # "name": "My Device",
        # "name": "My Dev*"
    }

    resources = Resources()
    devices = resources.devices.listDevice(
        {"page": 1, "fields": ["id", "tags"], "filter": my_filter, "amount": 20}
    )

    return devices


def my_analysis(context, scope: list) -> None:
    list_devices = get_device_list()

    print(list_devices)
    print(f"Total devices: {len(list_devices)}")


# The analysis token in only necessary to run the analysis outside TagoIO
Analysis.use(my_analysis, params={"token": "MY-ANALYSIS-TOKEN-HERE"})
