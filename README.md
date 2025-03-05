{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### 这是一份简要的代码食用说明\n",
    "#### 用于Erchaaa的辩讨准备"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "##### Ⅰ 数据获取\n",
    "+ 来源：[大籽《白月光与朱砂痣》完整版MV](https://www.bilibili.com/video/BV1uA411H7CR)\n",
    "+ 爬取过程省略，得到库中comment.txt"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "##### Ⅱ 数据整理\n",
    "+ 转为CSV格式方便后续处理\n",
    "+ 得到库中comment.csv\n",
    "+ 处理使用代码：[txt_to_csv.py](txt_to_csv.py)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "##### Ⅲ NLP+情感处理\n",
    "+ 考虑到边际效应递减的问题\n",
    "+ 考虑到长文本情绪可能更强\n",
    "+ 考虑到负面情绪的判断方式\n",
    "+ 处理使用代码：[emotional_analysis.py](emotional_analysis.py)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "##### Ⅳ 数据结果\n",
    "+ 有效评论个数: 886  \n",
    "+ 消极评论个数: 781  \n",
    "+ 负面情绪占比: 88.15%"
   ]
  }
 ],
 "metadata": {
  "language_info": {
   "name": "python"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
