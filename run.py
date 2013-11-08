#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging
import config
import boto

from csv import reader
from boto.mws import connection
from boto.mws.exception import ResponseError
from formatters import ColorFormatter
from StringIO import StringIO

boto.set_stream_logger('boto')

logging.getLogger("").setLevel(logging.DEBUG)
logging.getLogger("boto").setLevel(logging.DEBUG)
consoleHandler = logging.StreamHandler()
consoleHandler.setFormatter(ColorFormatter())
logging.getLogger("").addHandler(consoleHandler)

mws = connection.MWSConnection(SellerId=config.MERCHANT_ID,
                               aws_access_key_id=config.AWS_ACCESS_KEY_ID,
                               aws_secret_access_key=config.SECRET_KEY)

try:
    reports = mws.get_report_list()
    report_infos = reports.GetReportListResult.ReportInfo
    for report_info in report_infos:
        if report_info.ReportType != '_GET_FLAT_FILE_ORDERS_DATA_' or \
                report_info.Acknowledged != 'false':
            continue
        report = mws.get_report(ReportId=report_info.ReportId)
        fields = {}
        f = StringIO(report)
        for row in reader(f, delimiter='\t'):
            fields = dict((field, '') for field in row)
            break
except ResponseError as e:
    logging.error(e.message)
