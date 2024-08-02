import os
import sys

from jinja2 import Environment, FileSystemLoader

if len(sys.argv) == 1:
    basename = os.path.basename(__file__)
    print(f'usage: {basename} <template_child_file>')
    sys.exit(1)

# コマンドライン引数に指定されたファイル名からテンプレートローダーを作成
template_file_path = sys.argv[1]
template_dir = os.path.dirname(os.path.abspath(template_file_path))
loader = FileSystemLoader(template_dir)

# テンプレートに埋め込むデータ
my_desire = 'I want some money! to buy my favorite pizza...'

# データとして使用する辞書を定義
context = {
    "a_variable": my_desire
}

env = Environment(loader=loader)

# テンプレートを作成
template = env.get_template(template_file_path)

# テンプレートをレンダリング
output = template.render(context)

# 結果を出力
print(output)
