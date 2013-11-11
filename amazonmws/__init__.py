# -*- coding: utf-8 -*-

"""
Amazon Marketplace Web Service (MWS) Client Library
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:copyright: (c) 2013 by Mark A. Richman.
:license: GPL v2, see LICENSE for more details.
"""

__title__ = 'amazonmws'
__version__ = '1.0.0'
__build__ = 0x010000
__author__ = 'Mark A. Richman'
__license__ = 'GPL v2'
__copyright__ = 'Copyright 2013 Mark A. Richman'

__all__ = ['mwsclient']

# Set default logging handler to avoid "No handler found" warnings.
import logging
try:  # Python 2.7+
    from logging import NullHandler
except ImportError:
    class NullHandler(logging.Handler):
        def emit(self, record):
            pass

logging.getLogger(__name__).addHandler(NullHandler())
