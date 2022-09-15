
# Emailer

An API to integrate in other apps to send emails, OTPs or newsletter. No need to setup your on SMTP server you can use Gmail, AWS, Yahoo, Yandex or any other email services to confiugre this app and send emails programatically.

[![GitHub license](https://img.shields.io/github/license/viperadnan-git/emailer-py?style=for-the-badge)](https://github.com/viperadnan-git/emailer-py/blob/main/LICENSE)
![](https://img.shields.io/badge/Python-3.9-blue?style=for-the-badge)
![](https://img.shields.io/badge/Made%20With-%F0%9F%92%99-red?style=for-the-badge)

> This project is under development, not recommended for use in production directly.
## Table of Contents
- [Features](#features)
    - [Roadmap](#roadmap)
    - [Tech Stack](#tech-stack)
- [Usage/Example](#api-reference)
  - [API Reference](#api-reference)
  - [Example](#usage-example)
- [Getting Started](#installation)
  - [Installation](#installation)
  - [Configuration](#configuration)
  - [Deployment](#deployment)
- [Contribution](#contributing)
- [License](#license)
## Features

- Send emails via HTTP `POST` request
- Configure `HTML` and `RAW` body seperately
- Blacklist & Whitelist email addresses
- Whitelist IP for API calls
## Roadmap

- Multiple email support
- Email verification via OTP
- SMS Support using AWS SNS

If you have any other suggestions, feel free to open a Issue or Pull Request
## Tech Stack

**Client:** Swagger, Bootstrap

**Server:** Python3, FastAPI, smtplib

## API Reference

#### Sends an Email

```http
POST /email/send
```

| Parameter | Type     | Description                | Required |
| :-------- | :------- | :------------------------- | :------- |
| `email` | `string` | Email of the receipent | True |
| `body` | `string` | Raw body of the email | True |
| `subject` | `string` | Subject of the email | False |
| `sender` | `string` | Email of the sender | False |
| `sender_name` | `string` | Name of the sender | False |
| `html` | `string` | HTML body of the email | False |

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
## Installation

This project is built with `python-3.9` and `FastApi` so you need to install python and should have atleast one public PORT and IP

- Installing pre-requisites

```bash
apt install git python3 python3-pip
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

## Contributing

Contributions are always welcome!

To discuss about the improvement/contribution on this project join [group chat](https://t.me/vipercommunity).


## License

Made with ♥ and Licensed under [GNU General Public License v3.0](./LICENSE) 

