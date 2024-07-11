import pandas as pd
import chardet


# 使用 chardet 检测文件编码
def detect_encoding(file_path):
    with open(file_path, 'rb') as f:
        raw_data = f.read()
        result = chardet.detect(raw_data)
        encoding = result['encoding']
    return encoding


def result1(rank, course_requirement, weights):
    # 读取包含专业信息的CSV文件，并检测编码
    file_path_subjects = 'C:\\Users\\Ken-Suzhou\\Documents\\GitHub\\smart-college-application-web\\code\\django_web\\info\\data.csv'
    encoding_subjects = detect_encoding(file_path_subjects)
    df_subjects = pd.read_csv(file_path_subjects, encoding=encoding_subjects)

    # 读取包含霍兰德六个维度人格类型的CSV文件，并检测编码
    file_path_holland = 'C:\\Users\\Ken-Suzhou\\Documents\\GitHub\\smart-college-application-web\\code\\django_web\\info\\data_subject_holland.csv'
    encoding_holland = detect_encoding(file_path_holland)
    df_holland = pd.read_csv(file_path_holland, encoding=encoding_holland)

    # 读取cluster_results.csv，并检测编码
    file_path_cluster = 'C:\\Users\\Ken-Suzhou\\Documents\\GitHub\\smart-college-application-web\\code\\django_web\\info\\cluster_results.csv'
    encoding_cluster = detect_encoding(file_path_cluster)
    df_cluster = pd.read_csv(file_path_cluster, encoding=encoding_cluster)

    if course_requirement[0] == 'PC':
        course_requirement = '物理+化学'
    elif course_requirement[0] == 'P':
        course_requirement = '物理+不限'
    elif course_requirement[0] == 'H':
        course_requirement = '历史+不限'
    # 根据排名和选课要求筛选符合条件的专业
    print(course_requirement)
    filtered_subjects = df_subjects[
        (df_subjects['low_rank'] >= int(rank)) &
        ((df_subjects['elective_info'] == course_requirement) | (df_subjects['elective_info'] == ''))
        ]

    # 初始化字典，用于存储专业与匹配度
    matches = {}
    top_matches = {}

    # 遍历筛选后的专业，计算匹配度
    for index, row in filtered_subjects.iterrows():
        subject = row['subject']
        university = row['college']
        weight_score_rank = (1000 - abs(row['low_rank'] - int(rank))) / 1000
        weight_score_interest = 0

        # 查找对应专业的霍兰德六个维度人格类型数据
        row_holland = df_holland[df_holland['subject'] == subject]
        if not row_holland.empty:
            total = (float(row_holland['R'].values[0]) +
                     float(row_holland['I'].values[0]) +
                     float(row_holland['A'].values[0]) +
                     float(row_holland['S'].values[0]) +
                     float(row_holland['E'].values[0]) +
                     float(row_holland['C'].values[0]))

            # 计算匹配度
            for char in weights:
                if char in ['R', 'I', 'A', 'S', 'E', 'C']:
                    weight_score_interest += row_holland[char].values[0]

            weight_score_interest = (weight_score_interest / total) / 0.6

        # 将匹配度存储到字典中
        matches[(subject, university)] = weight_score_rank * 0.65 + weight_score_interest * 0.35

    # 根据匹配度排序并输出前几个匹配的结果
    sorted_matches = sorted(matches.items(), key=lambda x: x[1], reverse=True)
    top_matches = sorted_matches[:5]  # 前5个匹配度最高的结果

    # 根据权重将适合的专业输出
    sorted_weights = ''.join(sorted(weights))  # 对输入的权重进行排序
    matching_subjects = df_cluster[
        df_cluster['Top Features'].apply(lambda x: ''.join(sorted(x)) == sorted_weights)]['Subject'].tolist()
    return matching_subjects


def result2(rank, course_requirement, weights):
    # 读取包含专业信息的CSV文件，并检测编码
    file_path_subjects = 'C:\\Users\\Ken-Suzhou\\Documents\\GitHub\\smart-college-application-web\\code\\django_web\\info\\data.csv'
    encoding_subjects = detect_encoding(file_path_subjects)
    df_subjects = pd.read_csv(file_path_subjects, encoding=encoding_subjects)

    # 读取包含霍兰德六个维度人格类型的CSV文件，并检测编码
    file_path_holland = 'C:\\Users\\Ken-Suzhou\\Documents\\GitHub\\smart-college-application-web\\code\\django_web\\info\\data_subject_holland.csv'
    encoding_holland = detect_encoding(file_path_holland)
    df_holland = pd.read_csv(file_path_holland, encoding=encoding_holland)

    # 读取cluster_results.csv，并检测编码
    file_path_cluster = 'C:\\Users\\Ken-Suzhou\\Documents\\GitHub\\smart-college-application-web\\code\\django_web\\info\\cluster_results.csv'
    encoding_cluster = detect_encoding(file_path_cluster)
    df_cluster = pd.read_csv(file_path_cluster, encoding=encoding_cluster)

    if course_requirement[0] == 'PC':
        course_requirement = '物理+化学'
    elif course_requirement[0] == 'P':
        course_requirement = '物理+不限'
    elif course_requirement[0] == 'H':
        course_requirement = '历史+不限'
    # 根据排名和选课要求筛选符合条件的专业
    filtered_subjects = df_subjects[
        ((df_subjects['low_rank'] >= int(rank)) &
         (df_subjects['elective_info'] == course_requirement)) |
        (df_subjects['elective_info'] == '')
        ]

    # 初始化字典，用于存储专业与匹配度
    matches = {}
    top_matches = {}

    # 遍历筛选后的专业，计算匹配度
    for index, row in filtered_subjects.iterrows():
        subject = row['subject']
        university = row['college']
        weight_score_rank = (1000 - abs(row['low_rank'] - int(rank))) / 1000
        weight_score_interest = 0

        # 查找对应专业的霍兰德六个维度人格类型数据
        row_holland = df_holland[df_holland['subject'] == subject]
        if not row_holland.empty:
            total = (float(row_holland['R'].values[0]) +
                     float(row_holland['I'].values[0]) +
                     float(row_holland['A'].values[0]) +
                     float(row_holland['S'].values[0]) +
                     float(row_holland['E'].values[0]) +
                     float(row_holland['C'].values[0]))

            # 计算匹配度
            for char in weights:
                if char in ['R', 'I', 'A', 'S', 'E', 'C']:
                    weight_score_interest += row_holland[char].values[0]

            weight_score_interest = (weight_score_interest / total) / 0.6

        # 将匹配度存储到字典中
        matches[(subject, university)] = weight_score_rank * 0.65 + weight_score_interest * 0.35

    # 根据匹配度排序并输出前几个匹配的结果
    sorted_matches = sorted(matches.items(), key=lambda x: x[1], reverse=True)
    top_matches = sorted_matches[:5]  # 前5个匹配度最高的结果

    match_res = ''
    for match in top_matches:
        match_res += f"专业：{match[0][0]}, 大学：{match[0][1]}, 匹配度：{str(match[1])}"
    return match_res
