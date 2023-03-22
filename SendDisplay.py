import requests
import json



def load_json_file():
    with open("wallet.json") as f:
        return json.loads(f.read())


def send_http_post(json_obj):
    r = requests.post('https://mythologic.fr:8080', json=json_obj)
    print(r.status_code, r.text)


def main():
    json_obj = load_json_file()
    send_http_post(json_obj)


if __name__ == '__main__':
    main()