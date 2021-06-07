#   Copyright 2021 by Godwin peter <me@godwin.dev>, Tolaram Group.
#   All rights reserved.
#   This file is part of the the Titan micro task scheduler project,
#   and is released under the "MIT License Agreement". Please see the LICENSE
#   file that should have been included as part of this package.

import urllib3
from titan.common.utils.log import logger
import json


class http:

    response = None

    def __init__(self, payload):
        self.payload = payload

    def execute(self):
        params = self.payload
        # Params sample content
        # params = {
        #   "callType": "POST",
        #   "host": "https://localhost/test",
        #   "headers": {
        #     "Content-Type": "application/json",
        #     "Accept-Charset": "UTF-8",
        #     "Authorization": "",
        #   },
        #   "body": {
        #     "from": "xxxx",
        #     "to": ["+2347xxxxxxxxx", "+2348xxxxxxxxx"],
        #     "text": "",
        #   },
        #   "params": {},
        # }
        try:
            callback_instance = urllib3.PoolManager()
            response = callback_instance.request(
                params["callType"],
                params["host"],
                body=json.dumps(params["body"]).encode("utf-8"),
                headers=params["headers"],
                fields=params["params"],
            )
            self.response = response

            if response.status >= 200 & response.status <= 204:
                logger.info("HTTP request completed..")
            else:
                logger.error("HTTP request encountered some errors..")

        except urllib3.exceptions.NewConnectionError:
            logger.warn("HTTP request failed to complete..")

    def result(self):
        return self.response.data
