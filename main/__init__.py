import logging
import os
import sys
from types import SimpleNamespace

import yaml
from dotenv import load_dotenv
from fastapi import FastAPI

load_dotenv()
if os.path.exists('log.txt'):
    with open('log.txt', 'r+') as f:
        f.truncate(0)

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    handlers=[logging.FileHandler(
                        'log.txt'), logging.StreamHandler()],
                    level=logging.INFO)

if os.path.exists('config.yml'):
    with open("config.yml", "r") as stream:
        try:
            config = SimpleNamespace(**yaml.safe_load(stream))
        except yaml.YAMLError as exc:
            logging.error('Invalid YAML config file provided.',
                          '\nExiting now..')
            sys.exit()
else:
    logging.error('Configuration file missing (config.yml)',
                  '\nExiting now...')
    sys.exit()


app = FastAPI()
