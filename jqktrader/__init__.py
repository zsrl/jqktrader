# -*- coding: utf-8 -*-
import urllib3

from jqktrader import exceptions
from jqktrader.api import use
from jqktrader.log import logger

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
