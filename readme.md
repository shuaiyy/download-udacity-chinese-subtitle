# 从udacity在线课堂提取网页版字幕

在线视频会提供三种字幕，英文，中文，中英双语，官方直接提供打包下载的是英文字幕。

### 相关依赖

+ selenium
+ chrome driver (对应chrome 版本69)
+ scrapy中的Selector，可以换成你熟悉的HTML解析器
+ requests 用来下载字幕文件

### 运行

+ 首先安装相关依赖
+ 修改这几行配置

```python
browser = webdriver.Chrome(executable_path="./chromedriver.exe") # chrome driver路径
login_name = "xx@qq.com" # 登录邮箱
login_password = "你的密码"
c_url = 'https://classroom.udacity.com/courses/ud827'  # 课堂地址， 修改udxxx部分
```

+ 然后执行 `selenium_spider.py`文件，

  chrome跳转到udacity登录界面，点击登录按钮，等待程序执行很久，因为每个网页都用chrome打开一次，中间还会停个3秒。

  可以将网页播放器静音，最小化chrome浏览器，然后去做其他事情。

+ 执行`download.py`

  上一步执行完成后，会生成n个txt文件，如果这门课有20课程，就会有1~20.txt，里面存放的每个课程的每一课的title和双语字幕的url地址，如果某一课没有视频，则url为None。

  ```python
  # 12.txt 课程12的所有课时
  ## ++ 为分隔符，前面是title，后面是字幕url
  1 - 练习Intuitioneng-cn.vtt++https://s3.cn-north-1.amazonaws.com.cn/u-subs-vtt/en-us_zh-cn/Yy5vdqbdlKU.vtt
  1 - 练习Intuitioncn.vtt++https://s3.cn-north-1.amazonaws.com.cn/u-subs-vtt/zh-cn/Yy5vdqbdlKU.vtt 
  # 没有视频时，URL为None
  10 - 练习Within-Group Variabilityeng-cn.vtt++None
  10 - 练习Within-Group Variabilitycn.vtt++None
  ```

  ​