import os
import random
import shutil
from tqdm import tqdm
import argparse

def scan_files(source_folder, file_types):
    files = []
    for root, dirs, files_in_dir in tqdm(os.walk(source_folder), desc="扫描文件夹", ncols=100):
        for file in files_in_dir:
            if file.endswith(tuple(file_types)):
                file_path = os.path.join(root, file)
                files.append(file_path)
    return files

def copy_random_files(source_folder, destination_folder, n, file_types):
    # 检查源文件夹是否存在
    if not os.path.exists(source_folder):
        print(f"源文件夹 '{source_folder}' 不存在")
        return

    # 创建目标文件夹
    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)

    # 扫描源文件夹及其子文件夹中的所有文件，并显示进度条
    files = scan_files(source_folder, file_types)

    # 检查是否有足够的文件可供选择
    if len(files) < n:
        print("源文件夹及其子文件夹中的文件数量不足")
        return

    # 随机选择n个文件，并复制到目标文件夹中，同时显示进度条
    with tqdm(total=n, desc="复制文件", ncols=100) as pbar:
        selected_files = random.sample(files, n)
        for file in selected_files:
            destination_path = os.path.join(destination_folder, os.path.relpath(file, source_folder))
            os.makedirs(os.path.dirname(destination_path), exist_ok=True)
            shutil.copyfile(file, destination_path)
            pbar.update(1)

    print(f"成功复制了 {n} 个随机文件到目标文件夹 '{destination_folder}'")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='复制随机文件')
    parser.add_argument('--source_folder', required=True, help='源文件夹')
    parser.add_argument('--destination_folder', required=True, help='目标文件夹')
    parser.add_argument('--n', type=int, required=True, help='需要复制的文件数量')
    parser.add_argument('--file_types', nargs='+', required=True, help='需要复制的文件类型，例如pdf doc png')

    args = parser.parse_args()

    copy_random_files(args.source_folder, args.destination_folder, args.n, args.file_types)
