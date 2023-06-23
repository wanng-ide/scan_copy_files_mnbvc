import os
import random
import shutil
from tqdm import tqdm

def copy_random_pdf_files(source_folder, destination_folder, n):
    # 检查源文件夹是否存在
    if not os.path.exists(source_folder):
        print(f"源文件夹 '{source_folder}' 不存在")
        return

    # 创建目标文件夹
    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)

    # 遍历源文件夹，并筛选出pdf文件，同时显示进度条
    with tqdm(total=n, desc="扫描文件夹", ncols=100) as pbar1:
        pdf_files = []
        for entry in os.scandir(source_folder):
            if entry.is_file() and entry.name.endswith(".pdf"):
                pdf_files.append(entry.path)
            pbar1.update(1)

    # 检查是否有足够的文件可供选择
    if len(pdf_files) < n:
        print("源文件夹中的pdf文件数量不足")
        return

    # 随机选择n个pdf文件，并复制到目标文件夹中，同时显示进度条
    with tqdm(total=n, desc="复制文件", ncols=100) as pbar2:
        selected_files = random.sample(pdf_files, n)
        for file in selected_files:
            destination_path = os.path.join(destination_folder, os.path.basename(file))
            shutil.copyfile(file, destination_path)
            pbar2.update(1)

    print(f"成功复制了 {n} 个随机pdf文件到目标文件夹 '{destination_folder}'")

# 使用示例
source_folder = "path/to/source/folder"
destination_folder = "path/to/destination/folder"
n = 1000

copy_random_pdf_files(source_folder, destination_folder, n)
