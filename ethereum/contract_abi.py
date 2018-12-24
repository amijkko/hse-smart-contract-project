import json
abi_raw = """
[
	{
		"constant": false,
		"inputs": [
			{
				"name": "key",
				"type": "string"
			},
			{
				"name": "title_",
				"type": "bytes32"
			},
			{
				"name": "url_",
				"type": "string"
			},
			{
				"name": "price_",
				"type": "uint256"
			}
		],
		"name": "set_ad",
		"outputs": [],
		"payable": false,
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"constant": true,
		"inputs": [
			{
				"name": "key",
				"type": "string"
			}
		],
		"name": "get_ad_price",
		"outputs": [
			{
				"name": "price_",
				"type": "uint256"
			}
		],
		"payable": false,
		"stateMutability": "view",
		"type": "function"
	},
	{
		"constant": true,
		"inputs": [
			{
				"name": "key",
				"type": "string"
			}
		],
		"name": "get_ad_title",
		"outputs": [
			{
				"name": "title_",
				"type": "bytes32"
			}
		],
		"payable": false,
		"stateMutability": "view",
		"type": "function"
	},
	{
		"constant": true,
		"inputs": [
			{
				"name": "key",
				"type": "string"
			}
		],
		"name": "get_ad_url",
		"outputs": [
			{
				"name": "url_",
				"type": "string"
			}
		],
		"payable": false,
		"stateMutability": "view",
		"type": "function"
	}
]
"""
replace_dict = {'"false"': 'False', '"true"': 'True'}


def replace_abi(raw):
    for k, v in replace_dict.items():
        raw = raw.replace(k, v)
    return raw

abi = json.loads(replace_abi(abi_raw))