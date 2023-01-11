from tree_sitter import Language

import config as cfg

Language.build_library(
    cfg.OUTPUT_PATH,
    
    [
        'vendor/tree-sitter-java',
        'vendor/tree-sitter-javascript',
        'vendor/tree-sitter-python',
    ]
)