### 这是一份简要的代码食用说明
#### 用于Erchaaa的辩讨准备

##### Ⅰ 数据获取
+ 来源：[大籽《白月光与朱砂痣》完整版MV](https://www.bilibili.com/video/BV1uA411H7CR/)
+ 爬取过程省略，得到库中[comment.txt](comment.txt)

##### Ⅱ 数据整理
+ 转为CSV格式方便后续处理
+ 得到库中[comment.csv](comment.csv)
+ 处理使用代码：[txt_to_csv.py](txt_to_csv.py)

##### Ⅲ NLP+情感处理
+ 考虑到边际效应递减的问题
+ 考虑到长文本情绪可能更强
+ 考虑到负面情绪的判断方式
+ 处理使用代码：[emotional_analysis.py](emotional_analysis.py)

##### Ⅳ 数据结果
+有效评论个数: 538 
+消极评论个数: 537 
+负面情绪占比: 99.81% 
