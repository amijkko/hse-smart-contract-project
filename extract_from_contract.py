import requests
import json
import codecs


def load_file(fname):
    with open(fname, 'r') as f:
        text = f.read(-1).strip()
    return text


def my_rstrip(text):
    for _ in range(1000):
        if text[-2:] == '00':
            text = text[:-2]
    return text


def my_lstrip(text):
    for _ in range(1000):
        if text[:2] == '00':
            text = text[2:]
    return text


def decode_response(response):
    text = json.loads(response.text)
    return codecs.decode(my_lstrip(my_rstrip(text['result'][2:].replace('200000', ''))), 'hex').decode('ascii')


def enc_len(x):
    h = str(hex(x)).lstrip('0x')
    return ('0' * (2 - len(h)) + h).encode('ascii')


def _get_by_keyword(contract_address, enc_func, keyword):
    enc_name = (enc_len(len(keyword)) + codecs.encode(keyword.encode('ascii'), 'hex')).decode('ascii')
    enc_name += '0' * (66 - len(enc_name))
    js = """{"jsonrpc":"2.0","id":4,"method":"eth_call",
               "params":[{"to":"%s","data":"0x%s000000000000000000000000000000000000000000000000000000000000002000000000000000000000000000000000000000000000000000000000000000%s"},"latest"]}"""  % (contract_address.lower(), enc_func, enc_name)

    response = requests.post("https://ropsten.infura.io/", data = js)
    return decode_response(response)


def get_title(keyword):
    enc_func = 'a2e0bcfd'
    return _get_by_keyword(contract_address, enc_func, keyword)


def get_url(keyword):
    enc_func = 'baa1d13a'
    return _get_by_keyword(contract_address, enc_func, keyword)


contract_address = load_file('ethereum/contract_address.txt').lower()

if __name__ == '__main__':
    for test_keyword in ['test keyword', 'cat food']:
        print('Keyword: ', test_keyword)
        print('Title is:', get_title(test_keyword))
        print('Url is:', get_url(test_keyword))