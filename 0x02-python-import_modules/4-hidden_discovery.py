#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    for attribute in dir(hidden_4):
        if attribute[0] != '_' and attribute[1] != '_':
            print(attribute)
