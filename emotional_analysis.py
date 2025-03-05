import pandas as pd
import numpy as np
from snownlp import SnowNLP
from sklearn.svm import SVR
from sklearn.preprocessing import StandardScaler

csv_path = "./comment.csv"
df = pd.read_csv(csv_path)
df.columns = ["姓名", "正文", "时间"]

df["情感得分"] = df["正文"].apply(lambda text: SnowNLP(str(text)).sentiments)
df["评论长度"] = df["正文"].apply(len)

X = df[["评论长度"]]
y = df["情感得分"]

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

svr_model = SVR(kernel='rbf')
svr_model.fit(X_scaled, y)

df["svr预处理"] = svr_model.predict(X_scaled)
df["拟合处理"] = 1 / (1 + np.exp(-8 * df["svr预处理"]))
df["长度处理"] = np.log(df["评论长度"] + 1) / np.log(df["评论长度"].max() + 1)
df["长度加权"] = df["拟合处理"] * df["长度处理"]

negative_comments = df[df["长度加权"] < 0.6]
negative_ratio = len(negative_comments) / len(df)

print(f"有效评论个数: {len(df)}")
print(f"消极评论个数: {len(negative_comments)}")
print(f"负面情绪占比: {negative_ratio:.2%}")
