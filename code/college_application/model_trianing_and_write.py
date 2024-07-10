import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error
from transformers import BertTokenizer, BertModel

# 假设我们有一个数据集，包含专业名称、描述和六项指数
data = pd.read_csv('subject.csv')

# 读取CSV文件
csv_file = 'data.csv'
column_name = 'subject'  # 指定要读取的列的名称
subject_list = []

df = pd.read_csv(csv_file, encoding='gbk')
subject_list.extend(df[column_name].unique())

# 初始化BERT模型和分词器
tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
bert_model = BertModel.from_pretrained('bert-base-uncased')


def get_bert_embedding(text):
    inputs = tokenizer(text, return_tensors='pt', max_length=512, truncation=True, padding='max_length')
    outputs = bert_model(**inputs)
    return outputs.last_hidden_state.mean(dim=1).detach().numpy()


# 获取专业描述的BERT嵌入
data['bert_embedding'] = data['description'].apply(get_bert_embedding)

# 将嵌入展开为多个特征
bert_embeddings = np.vstack(data['bert_embedding'])
X = bert_embeddings
y = data[['R', 'I', 'A', 'S', 'E', 'C']]

# 划分训练集和测试集
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 训练随机森林回归模型
rf_model = RandomForestRegressor(n_estimators=100, random_state=42)
rf_model.fit(X_train, y_train)

# 预测
y_pred = rf_model.predict(X_test)

# 评估模型
mse = mean_squared_error(y_test, y_pred)
print(f'Mean Squared Error: {mse}')

# 使用模型预测新专业的霍兰德六项指数
for i in subject_list:
    new_major_description = i
    new_major_embedding = get_bert_embedding(new_major_description)
    predicted_indices = rf_model.predict(new_major_embedding)
    csv_file_path = 'data_subject_holland.csv'
    df = pd.read_csv(csv_file_path)
    new_row = {
        'subject': i,
        'R': predicted_indices[0][0],
        'I': predicted_indices[0][1],
        'A': predicted_indices[0][2],
        'S': predicted_indices[0][3],
        'E': predicted_indices[0][4],
        'C': predicted_indices[0][5]
    }
    new_row_df = pd.DataFrame([new_row])
    df = pd.concat([df, new_row_df], ignore_index=True)
    df.to_csv('data_subject_holland.csv', index=False)
