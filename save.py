from glob import glob
import os
from zipfile import ZipFile, ZIP_DEFLATED
import getpass
import shutil

studentId = getpass.getuser()[:6]
zipFilePath = f"./{studentId}.zip"
unzipedFilePath = f"./{studentId}"

try:
    os.remove(path=zipFilePath)
except FileNotFoundError as fnfe:
    pass
shutil.rmtree(path=unzipedFilePath, ignore_errors=True)

rank = input("第何回(2桁で入力してください 例: 09)\n: ")
which = input("練習問題を圧縮する場合は任意のキーを,\n課題ファイルを圧縮する場合はそのままreturnを入力してください\n: ")
targetFiles = f"{rank}_??_*.c" if which != "" else f"{rank}_*_{studentId}.c"
with ZipFile(file=zipFilePath, mode="w", compression=ZIP_DEFLATED) as zf:
    for file in glob(targetFiles):
        zf.write(file)
        print(f"zipファイルに追加しました: {file}")
