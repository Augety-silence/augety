import pandas as pd
from transformers import pipeline

# 读取 CSV 文件
csv_path = "C:\\Users\\Augety\\Desktop\\comment.csv"
df = pd.read_csv(csv_path)
df.columns = ["姓名", "正文", "时间"]

# 使用 Hugging Face 的情感分析管道
sentiment_analyzer = pipeline("sentiment-analysis", truncation=True, max_length=512)

# 定义一个函数，将长文本分割为多个片段
def split_and_analyze(text, max_len=512):
    words = text.split()
    num_chunks = (len(words) + max_len - 1) // max_len
    sentiments = []

    for i in range(num_chunks):
        chunk = ' '.join(words[i * max_len:(i + 1) * max_len])
        sentiment = sentiment_analyzer(chunk)[0]['label']
        sentiments.append(sentiment)
    
    # 合并所有片段的情感标签，可以选择多数投票或平均处理
    positive_count = sentiments.count("POSITIVE")
    negative_count = sentiments.count("NEGATIVE")
    
    return "POSITIVE" if positive_count > negative_count else "NEGATIVE"

# 应用分割和情感分析
df["情感分析结果"] = df["正文"].apply(lambda text: split_and_analyze(text))

# 计算情感得分，label 为 POSITIVE 或 NEGATIVE，映射为 1 或 0
df["情感得分"] = df["情感分析结果"].apply(lambda label: 1 if label == "POSITIVE" else 0)

# 计算负面情绪占比
negative_comments = df[df["情感得分"] == 0]
negative_ratio = len(negative_comments) / len(df)

print(f"有效评论个数: {len(df)}")
print(f"消极评论个数: {len(negative_comments)}")
print(f"负面情绪占比: {negative_ratio:.2%}")
