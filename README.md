# 东京羽田机场 - 爬虫说明文档

## 目标网站

```html
https://tokyo-haneda.com/flight/flightInfo_int.html
```

东京羽田机场国际航班信息爬取，爬取结果已放入`Results`文件夹中。

## 使用说明

### 使用方法

本项目提供了两个爬虫，一个基于`scrapy`，一个基于`requests`。

#### `scrapy` 爬虫

1. 使用`pip install -r requirements.txt`一键安装所有依赖。
2. 将`chromeMiddleware.py`中的`chromedriver`改为您的`chromedriver.exe`所在的绝对路径。
3. 运行`scrapy crawl Haneda -o xxx.json`即可。

#### `requests `爬虫

1. 使用`pip install -r requirements.txt`一键安装所有依赖。
2. 直接使用`python HanedaRequests.py`将会自动在当前目录输出`yyyy-mm-dd.json`文件。

### 爬虫介绍

经过对于目标网站的源码的研究，我们发现该网站可以通过常规`scrapy`的方式进行爬取。由于目标网站有一定的反爬虫机制，我们将`ROBOTSTXT_OBEY`设为`False`，同时引入`uagent.py`随机UA池来进一步绕过网站的反爬机制。

经过对于网站源码的进一步研究，我们发现该网站使用动态渲染，因此我们需要一个下载中间件来完成这一步骤。在此，我们选择了`selenium`+`chromedriver`作为下载中间件完成页面的渲染。详情可以参考`chromeMiddleware.py`文件中相关的内容。至此，我们已经完成了所有的准备工作。

由于本页面使用了动态渲染技术，因此通过抓包分析得到了它的API地址，继而我们使用`requests`实现了另外一版爬虫程序，具体代码请见`HanedaRequests.py`文件。

具体爬虫代码请参考`./spider/Haneda.py`中的内容。如果遇到未提到的错误，请尝试重新运行即可。

### 依赖说明

```python
# requirements.txt

selenium==3.141.0
Scrapy==2.4.1
urllib3==1.26.2
requests==2.25.0
itemadapter==0.2.0
Faker==4.17.1
```

*除去`requirements.txt`中所需的pip包之外，为了运行中间件，我们还需要`chromedriver`以及与其适配的`Chrome`浏览器，在本爬虫中所提供的的`chromedriver.exe`适用于使用`Chrome 87`的`Windows`系统，如果您的环境与之不适配，请自行前往官网下载相适配的`chromedriver`文件，并替换`chromeMiddleware.py`中的路径为相应的绝对路径即可。

## 数据介绍

数据全部来源于以上提到的目标网站，`json`结构请参考如下例子。

```json
//一个json文件示例
    {
        "arrivetime": "23:50",	//整点到达时间
        "changedtime": "[ - ]",	//改签时间
        "destination": "ドーハ", //目的地
        "passbyplace": "",		//经由地
        "airline": [			//航空公司
            "カタール航空",
            "日本航空"
        ],
        "flightnumber": [		//航班号
            "QR0813",
            "JL7999"
        ],
        "flightType": "351",	//飞机型号	
        "terminal": "T3",		//候机楼
        "checkin": "L",			//值班柜台
        "flightstatus": "欠航"   //航班状况
    }
```


