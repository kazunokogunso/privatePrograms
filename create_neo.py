import getpass
import re
import glob
from os.path import basename


def templateCFile(html):
    template = "#include <stdio.h>\n"
    template += "int main(int argc, char const *argv[]) {\n\treturn 0;\n}"
    return template


filePattern = r"issues.+\.md|第.+回 問題詳細"
goalFileNamePattern = re.compile(r"ファイル名: <code>[0-1][0-9]_.*\.c")
extra = "ファイル名: <code>"
studentId = getpass.getuser()[:6]
studentId += studentId[0] * 2
issues = list()

for issue in glob.glob(f"/Users/{studentId}/Downloads/**"):
    if re.search(filePattern, issue):
        issues.append(issue)
print("ファイル一覧")
for i in range(0, len(issues), 1):
    print(f"  {i+1}:{basename(issues[i])}")
print("番号を入力してファイルを選択してください")
selected = int(input(": "))-1

try:
    with open(issues[selected], 'r', encoding="utf-8") as html:
        files = list()
        for line in html:
            for file in goalFileNamePattern.findall(line):
                file = file.replace("k20000", studentId[:6])
                files.append(file[len(extra):])
        for file in files:
            try:
                with open(file, 'x', encoding="utf-8") as cFile:
                    print("ファイルを生成しました: " + file)
                    cFile.write(templateCFile(issues[selected]))
            except FileExistsError as fee:
                print("ファイルは既に生成されています: " + file)
except FileNotFoundError as ose:
    print(f"ファイルがダウンロードフォルダ内に見つかりません\n: issues{rank}.md.html\n")
