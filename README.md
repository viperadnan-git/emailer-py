
# Emailer

An API to send emails through python3's smtplib module.
Just configure your SMTP server credentials and you are ready to send a lot of emails through API, designed to be used as a newsletter service.

_This project is under development, you can face bugs and you shouldn't use it in production._ 
## Features

- Send emails via HTTP `POST` request
- Blacklist & Whitelist email addresses
- Only allowed IP can post requests


## Roadmap

- Multiple email support
- Email verification via OTP
- SMS Support using AWS SNS

If you have any other suggestions, feel free to open a Issue or Pull Request

## Tech Stack

**Client:** Swagger, Bootstrap

**Server:** Python, FastAPI, smtplib


## Installation

This project is built with `python-3.9` and `fastapi`

- Installing pre-requisites

```bash
apt-get install git python3 python3-pip
```

- Cloning Project
```bash
git clone https://github.com/viperadnan-git/emailer-py
cd emailer-py
```

- Installing dependencies via `pip`
```bash
pip install -r requirements.txt
```
## Configuration

All configuration are inside a single file [`config.yml`](./config.yml)
```yaml
server:
    allowed_hosts: ["127.0.0.1", "103.201.127.144", "*"]

smtp:
    username: viperadnan@email.com
    password: TheStr@ngPassword
    host: smtp.mail.yahoo.com
    port: 587

options:
    whitelist: ["*@gmail.com"]
    blacklist: ["*-*@gmail.com"]
```
## Deployment

To deploy this project via uvicorn (ASGI server implementation) run

```bash
uvicorn main.app:app
```

By default this will listen to `localhost` and port `8000`.
To listen to desired host nad port pass the `--host <host>` and `--port <port>` flags accordingly.

If you want to listen on all host and `HTTP` request (with port 80)
```bash
uvicorn main.app:app --host 0.0.0.0 --port 80
``` 


## Usage Example

```python
import requests

reqUrl = "http://<host>:<port>/email/send"

headersList = {
 "Content-Type": "application/json" 
}

payload = json.dumps({
    "email":"viperadnan@gmail.com",
    "body": "Hello from emailer-py"
})

response = requests.request("POST", reqUrl, data=payload,  headers=headersList)

print(response.text)
```

- You can use a `for` loop if you have multiple emails as a list.