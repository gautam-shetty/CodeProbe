while(cursor.goto_first_child()):
    print(cursor.node)
    while(cursor.goto_next_sibling()):
        print(cursor.node)