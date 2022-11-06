# jqktrader

同花顺自动程序化交易

# 目的

由于`easytrader`年久失修，同花顺自动交易模式存在问题，此包基于`easytrader`部分源码，删去其他部分，只专注与同花顺客户端的自动化交易，并解决`easytrader`现存问题，让使用者可以开箱即用。

# 安装

## 1. 安装 Tesseract OCR

由于程序运行过程中，需要识别验证码，请首先安装`Tesseract OCR`，官方下载地址：

> https://github.com/UB-Mannheim/tesseract/wiki

## 2. 安装 jqktrader

```
pip install jqktrader
```

# 用法