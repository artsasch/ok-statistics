import hashlib


with open("utils/access_token.txt", "r") as file:
    access_token = file.read().strip()

with open("utils/application_key.txt", "r") as file:
    application_key = file.read().strip()
    
with open("utils/session_secret_key.txt", "r") as file:
    session_secret_key = file.read().strip()

request_format = "json"
api_url = "https://api.ok.ru/fb.do"


def md5(method, url):
    string = f"application_key={application_key}format={request_format}method={method}url={url}{session_secret_key}"
    sig = hashlib.md5(string.encode("utf")).hexdigest()
    return sig
