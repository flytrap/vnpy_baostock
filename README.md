# vn.py框架的BaoStock数据服务接口

<p align="center">
  <img src ="https://vnpy.oss-cn-shanghai.aliyuncs.com/vnpy-logo.png"/>
</p>

<p align="center">
    <img src ="https://img.shields.io/badge/version-1.0.0-blueviolet.svg"/>
    <img src ="https://img.shields.io/badge/platform-windows|linux|macos-yellow.svg"/>
    <img src ="https://img.shields.io/badge/python-3.7-blue.svg"/>
    <img src ="https://img.shields.io/github/license/vnpy/vnpy.svg?color=orange"/>
</p>

## 说明

基于baostock模块的0.8.8版本开发，支持以下中国金融市场的K线数据：

* 股票：
  * SSE：上海证券交易所
  * SZSE：深圳证券交易所

## 安装

安装需要基于2.6.0版本以上的[VN Studio](https://www.vnpy.com)。

直接使用pip命令：

```
pip install vnpy_baostock
```

或者下载解压后运行：

```
python setup.py install
```

## 使用

在vn.py中使用BaoStock时，需要在全局配置中填写以下字段信息：

|名称|含义|必填|举例|
|---------|----|---|---|
|datafeed.name|名称|是|baostock|
|datafeed.username|用户名|否|anonymous|
|datafeed.password|密码|否|123456|
