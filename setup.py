import os

repos = [
    'https://github.com/tree-sitter/tree-sitter-java',
    'https://github.com/tree-sitter/tree-sitter-javascript',
    'https://github.com/tree-sitter/tree-sitter-python'
]

absolute_path = os.path.dirname(os.path.abspath(__file__))
vendor_absolute_path = absolute_path+'\\vendor'

if not(os.path.exists(vendor_absolute_path)):
    os.makedirs(vendor_absolute_path)
    os.chdir(vendor_absolute_path)
else:
    os.chdir(vendor_absolute_path)

for repo in repos:
    os.system('git clone '+repo+'.git')