from tree_sitter import Language, Parser

import config as cfg

JAVA_LANGUAGE = Language(cfg.OUTPUT_PATH, 'java')
JAVA_PARSER = Parser()
JAVA_PARSER.set_language(JAVA_LANGUAGE)

JS_LANGUAGE = Language(cfg.OUTPUT_PATH, 'javascript')
JS_PARSER = Parser()
JS_PARSER.set_language(JS_LANGUAGE)

PYTHON_LANGUAGE = Language(cfg.OUTPUT_PATH, 'python')
PYTHON_PARSER = Parser()
PYTHON_PARSER.set_language(PYTHON_LANGUAGE)