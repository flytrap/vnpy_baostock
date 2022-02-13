#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Created by flytrap
# Created time: 2022/02/13
import importlib_metadata

from .baostock_datafeed import BaoStockDatafeed as Datafeed


try:
    __version__ = importlib_metadata.version("vnpy_baostock")
except importlib_metadata.PackageNotFoundError:
    __version__ = "dev"
