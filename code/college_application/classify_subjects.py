import numpy as np
import chardet
import pandas as pd
from sklearn.cluster import KMeans
from sklearn.metrics.cluster import homogeneity_score
from sklearn.metrics import homogeneity_completeness_v_measure


def detect_encoding(file_path):
    with open(file_path, 'rb') as f:
        raw_data = f.read()
        result = chardet.detect(raw_data)
        encoding = result['encoding']
    return encoding


# 读取所有专业的名称以及霍兰德六个维度人格类型的CSV文件，并检测编码
file_path_all_subject = 'subject_normal_with_true_labels.csv'
encoding_all = detect_encoding(file_path_all_subject)
df_all = pd.read_csv(file_path_all_subject, encoding=encoding_all)

# 将读取结果转化为六维数组
columns_to_convert = ['R', 'I', 'A', 'S', 'E', 'C']
data = df_all[columns_to_convert].to_numpy()

# 设置聚类数K
K = 20

# 初始化KMeans对象
kmeans = KMeans(n_clusters=K, random_state=0)

# 对数据进行拟合和预测
kmeans.fit(data)
labels = kmeans.predict(data)
centroids = kmeans.cluster_centers_

# 将标签添加到原数据框中
df_all['Cluster'] = labels

# 找到每个聚类中心点中占比最高的三个字母
top_n = 3
top_features = np.argsort(centroids, axis=1)[:, -top_n:]

# 创建一个DataFrame来存储聚类结果
result_df = pd.DataFrame(columns=['Cluster', 'Top Features', 'Subjects'])

for i in range(K):
    top_feature_indices = top_features[i]
    top_feature_names = [columns_to_convert[j] for j in top_feature_indices]
    top_feature_names = top_feature_names[::-1]  # 倒序排列使得最大的排在前面
    cluster_subjects = df_all[df_all['Cluster'] == i]['subject'].tolist()
    result_df = result_df._append({
        'Cluster': i,
        'Top Features': top_feature_names,
        'Subjects': ', '.join(cluster_subjects)
    }, ignore_index=True)

# 打印聚类中心点和标签
print("Cluster centers:")
print(centroids)
print("\nLabels:")
print(labels)

# 打印结果
print("\nCluster Results:")
print(result_df)

true_labels = df_all['true_label']  # 实际标签的列名
homo_score = homogeneity_score(true_labels, labels)
hcv_score = homogeneity_completeness_v_measure(true_labels, labels)
print("\nHomogeneity Score:")
print(homo_score)
print("\nHomogeneity and Completeness Score:")
print(hcv_score)

# 保存结果到CSV文件
result_file_path = 'cluster_results.csv'
result_df.to_csv(result_file_path, index=False)
