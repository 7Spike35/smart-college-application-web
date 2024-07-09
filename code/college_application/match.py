import pandas as pd
import chardet

# 使用 chardet 检测文件编码
def detect_encoding(file_path):
    with open(file_path, 'rb') as f:
        raw_data = f.read()
        result = chardet.detect(raw_data)
        encoding = result['encoding']
    return encoding

# 读取包含专业信息的CSV文件，并检测编码
file_path_subjects = 'data.csv'
encoding_subjects = detect_encoding(file_path_subjects)
df_subjects = pd.read_csv(file_path_subjects, encoding=encoding_subjects)

# 读取包含霍兰德六个维度人格类型的CSV文件，并检测编码
file_path_holland = 'data_subject_holland.csv'
encoding_holland = detect_encoding(file_path_holland)
df_holland = pd.read_csv(file_path_holland, encoding=encoding_holland)

# 输入排名、选课要求和比重（例如 'RIA'）
rank = 13000  # 替换为实际输入的排名
course_requirement = '物理+不限'  # 替换为实际输入的选课要求
weights = 'ISE'  # 替换为实际输入的比重

# 根据排名和选课要求筛选符合条件的专业
filtered_subjects = df_subjects[(df_subjects['low_rank'] >= rank) & (df_subjects['elective_info'] == course_requirement)|(df_subjects['elective_info']=='')]
# print(filtered_subjects)

# 初始化一个字典，用于存储专业与匹配度
matches = {}

# 遍历筛选后的专业，计算匹配度
for index, row in filtered_subjects.iterrows():
    subject = row['subject']
    university = row['college']
    # print(subject,university)
    weight_score_rank = (1000-abs(row['low_rank']-rank))/1000
    weight_score_interest = 0

    # 查找对应专业的霍兰德六个维度人格类型数据
    row_holland = df_holland[df_holland['subject'] == subject]
    # print(row_holland['R'].values[0])
    total = float(row_holland['R'].values[0]) + float(row_holland['I'].values[0]) + float(row_holland['A'].values[0]) + float(row_holland['S'].values[0]) + float(row_holland['E'].values[0]) + float(row_holland['C'].values[0])

    if not row_holland.empty:
        # 计算匹配度
        for char in weights:
            if char in ['R', 'I', 'A', 'S', 'E', 'C']:
                weight_score_interest += row_holland[char].values[0]


        weight_score_interest = (weight_score_interest/total)/0.6

    # 将匹配度存储到字典中
    matches[(subject, university)] = weight_score_rank*0.65 + weight_score_interest*0.35
    # 根据匹配度排序并输出前几个匹配的结果
    sorted_matches = sorted(matches.items(), key=lambda x: x[1], reverse=True)
    top_matches = sorted_matches[:5]  # 前5个匹配度最高的结果

# 打印输出结果
for match in top_matches:
    print(f"专业：{match[0][0]}, 大学：{match[0][1]}, 匹配度：{match[1]}")
