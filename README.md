# Kung Kim Bon AI
## 现有功能
+ 应用文打分

### 应用文打分
***注: 此处应用文指临沂市2023级普通高中学科素养水平监测试卷(英语学科2025.1)***
#### 环境
+ Python3.7+
+ Package
  + tensorflow
  + requests
  + numpy
  + pillow 
#### Usage
```shell
git clone https://github.com/yishuiyizhong/KongKimBonAI.git
cd KongKimBonAI
```
参数为答题卡第一张图片,例如1.png
```shell
python process.py 1.png
```
![P1](./asse/2.png)
或者是附上英语小题分链接
```shell
python process.py "https://yunyj.linyi.net/wechat/imgs?eg=90361&sid=227010001&eid=903610003"
```
![P1](./asse/1.png)

## Source
训练部分和数据爬虫部分源码将提交于2025.2.11