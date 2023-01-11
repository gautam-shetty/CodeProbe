import config as cfg
import load_parser
import file_manager

parser = load_parser.PYTHON_PARSER

def read_callable(byte_offset, point):
    return src[byte_offset:byte_offset+1]

src = file_manager.bytesOfFile(cfg.PYTHON_INPUTFILE_PATH)

tree = parser.parse(read_callable)

print(tree)
print(tree.root_node.sexp())

cursor = tree.walk()

while(cursor.goto_first_child()):
    print(cursor.node)
    while(cursor.goto_next_sibling()):
        print(cursor.node)

# assert cursor.node.type == 'module'

# assert cursor.goto_first_child()
# assert cursor.node.type == 'function_definition'

# assert cursor.goto_first_child()
# assert cursor.node.type == 'def'

# # Returns `False` because the `def` node has no children
# assert not cursor.goto_first_child()

# assert cursor.goto_next_sibling()
# assert cursor.node.type == 'identifier'

# assert cursor.goto_next_sibling()
# assert cursor.node.type == 'parameters'

# assert cursor.goto_parent()
# assert cursor.node.type == 'function_definition'

