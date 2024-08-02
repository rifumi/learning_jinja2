import sys
from jinja2 import Template


def read_template_from_stdin():
    return sys.stdin.read()

def read_template_from_file(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            return file.read()
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        sys.exit(1)

if len(sys.argv) > 1:
    # コマンドライン引数にファイル名が指定された場合
    template_string = read_template_from_file(sys.argv[1])
else:
    # パイプでテンプレート文字列を受け取る場合
    template_string = read_template_from_stdin()

if len(template_string) == 0:
    print('Give the Jinja2 template string.')
    sys.exit(1)

# テンプレートに埋め込むデータ
class NavItem:
    def __init__(self, link:str, caption:str):
        self.href = link
        self.caption = caption
nav_list = [
    NavItem(link="aaa.html", caption="caption A"),
    NavItem(link="bbb.html", caption="caption B"),
    NavItem(link="ccc.html", caption="caption C"),
]
my_desire = 'I want some money! to buy my favorite pizza...'

# データとして使用する辞書を定義
context = {
    "navigation": nav_list,
    "a_variable": my_desire
}

# テンプレートを作成
template = Template(template_string)

# テンプレートをレンダリング
output = template.render(context)

# 結果を出力
print(output)
