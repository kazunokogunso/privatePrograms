import bs4
import getpass


def templateCFile(html):
    template = "#include <stdio.h>\n"
    template += "int main(int argc, char const *argv[]) {\n\treturn 0;\n}"
    return template


studentId = getpass.getuser()[:6]
rank = input("第何回(2桁で入力してください 例: 09)\n: ")
issues = f"/Users/{studentId}{studentId[0]}{studentId[0]}/Downloads/issues{rank}.md.html"
goalStr = "ファイル名: <code>"

try:
    with open(issues, 'r', encoding="utf-8") as html:
        for line in html:
            if goalStr not in line:
                continue
            sidx = line.find(rank+"_")
            eidx = line.find(".c", sidx)+2
            line = line.replace("k20000", studentId)
            try:
                with open(line[sidx:eidx], 'x', encoding="utf-8") as cFile:
                    print("ファイルを生成しました: " + line[sidx:eidx])
                    cFile.write(templateCFile(issues))
            except FileExistsError as fee:
                print("ファイルは既に生成されています: " + line[sidx:eidx])
except FileNotFoundError as ose:
    print(f"ファイルがダウンロードフォルダ内に見つかりません\n: issues{rank}.md.html\n")
