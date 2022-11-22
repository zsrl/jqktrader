![qrcode](./qrcode.png)
# jqktrader

同花顺自动程序化交易

# 目的

由于`easytrader`年久失修，同花顺自动交易模式存在问题，此包基于`easytrader`部分源码，删去其他部分，只专注与同花顺客户端的自动化交易，并解决`easytrader`现存问题，让使用者可以开箱即用。

# 解决的问题

* 升级pywinauto到最新版
* 补全缺少的依赖，如`pytesseract`、`pypiwin32`
* 修复无法自动填写输入框的各种问题
* 增加Tesseract的路径配置

# 安装

## 1. 安装 Tesseract OCR

由于程序运行过程中，需要识别验证码，请首先安装`Tesseract OCR`，官方下载地址：

> https://github.com/UB-Mannheim/tesseract/wiki

## 2. 安装 jqktrader

```
pip install jqktrader
```
> 需要python版本3.8+

# 用法

> jqktrader不维护同花顺客户端的登录状态，请手动登录后再使用。

```python
import jqktrader

user = jqktrader.use()

user.connect(
  exe_path=r'D:\同花顺软件\同花顺\xiadan.exe',
  tesseract_cmd=r'D:\Program Files\Tesseract-OCR\tesseract.exe'
)

user.position
```

**exe_path** 同花顺`xiadan.exe`的路径

**tesseract_cmd** Tesseract OCR `tesseract.exe`的路径

# API

沿用easyTrader官方的api，非同花顺相关的已删除。

参看文档：https://easytrader.readthedocs.io/zh/master/usage/

