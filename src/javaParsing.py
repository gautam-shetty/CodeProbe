import config as cfg
import load_parser
import file_manager

parser = load_parser.JAVA_PARSER

def read_callable(byte_offset, point):
    return src[byte_offset:byte_offset+1]

src = file_manager.bytesOfFile(cfg.JAVA_INPUTFILE_PATH)

tree = parser.parse(read_callable)

print(tree)
print(tree.root_node.sexp())

cursor = tree.walk()
while(cursor.goto_first_child()):
    print(cursor.node)
    while(cursor.goto_next_sibling()):
        print(cursor.node)