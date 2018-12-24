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
				"components": [
					{
						"name": "title",
						"type": "string"
					},
					{
						"name": "url",
						"type": "string"
					},
					{
						"name": "price",
						"type": "uint256"
					}
				],
				"name": "ad",
				"type": "tuple"
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
		"name": "get_ad",
		"outputs": [
			{
				"components": [
					{
						"name": "title",
						"type": "string"
					},
					{
						"name": "url",
						"type": "string"
					},
					{
						"name": "price",
						"type": "uint256"
					}
				],
				"name": "ad",
				"type": "tuple"
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