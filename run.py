#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging
import config

from amazonmws.mwsclient import MWS
from formatters import ColorFormatter

logging.getLogger("").setLevel(logging.DEBUG)
logging.getLogger("boto").setLevel(logging.DEBUG)
consoleHandler = logging.StreamHandler()
consoleHandler.setFormatter(ColorFormatter())
logging.getLogger("").addHandler(consoleHandler)

mws = MWS(seller_id=config.MERCHANT_ID,
          aws_access_key_id=config.AWS_ACCESS_KEY_ID,
          aws_secret_access_key=config.SECRET_KEY)
try:
    report_ids = mws.get_report_list()
    for r in report_ids:
        report = mws.get_report(report_id=r)
except Exception as e:
    logging.error(e.message)
