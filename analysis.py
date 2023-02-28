"""
 Analysis Example
 Get Device List

 This analysis retrieves the device list of your account and print to the console.
 There are examples on how to apply filter.

 Environment Variables
 In order to use this analysis, you must setup the Environment Variable table.

 account_token: Your account token

 Steps to generate an account_token:
 1 - Enter the following link: https://admin.tago.io/account/
 2 - Select your Profile.
 3 - Enter Tokens tab.
 4 - Generate a new Token with Expires Never.
 5 - Press the Copy Button and place at the Environment Variables tab of this analysis.
"""
from tagoio_sdk import Account, Analysis
from tagoio_sdk.modules.Account.Device_Type import DeviceInfoList


def query_devices(account: Account) ->list[DeviceInfoList]:
	# Example of filtering devices by Tag.
	# You can filter by: name, last_input, last_output, bucket, etc.
	my_filter = {
		"tags": [
			{"key": "keyOfTagWeWantToSearch", "value": "valueOfTagWeWantToSearch"}
		],
		# "bucket": "55d269211a2e236c25bb9859",
		# "name": "My Device"
	}

	devices = account.devices.listDevice({
		"page": 1,
		"fields": ["id", "tags"],
		"filter": my_filter,
		"amount": 20
	})

	return devices


def list_devices(context: list[dict], scope: list) -> None:
	# reads the value of account_token from the environment variable
	account_token = list(filter(lambda account_token: account_token["key"] == "account_token", context.environment))
	account_token = account_token[0]["value"]

	if not account_token:
		return print("Missing account_token Environment Variable.")

	account =  Account(params={"token": account_token})
	list_devices = query_devices(account=account)

	print(list_devices)
	print(f"Total devices: {len(list_devices)}")


# The analysis token in only necessary to run the analysis outside TagoIO
Analysis(params={"token": "MY-ANALYSIS-TOKEN-HERE"}).init(list_devices)
