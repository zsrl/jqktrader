# -*- coding: utf-8 -*-
import logging
import sys

from .clienttrader import ClientTrader
from jqktrader.log import logger


if sys.version_info <= (3, 5):
    raise TypeError("不支持 Python3.5 及以下版本，请升级")


def use( debug=False, **kwargs):
    """用于生成同花顺交易对象
    :param debug: 控制 debug 日志的显示, 默认为 True
    :param initial_assets: [雪球参数] 控制雪球初始资金，默认为一百万
    :return the class of trader

    """
    if debug:
        logger.setLevel(logging.DEBUG)

    return ClientTrader()
