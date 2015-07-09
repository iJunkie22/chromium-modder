__author__ = 'ethan'
import os

ref_table = """
# ID        Extension   Chrome virtual path
2210        css         chrome://resources/css/chrome_shared.css
2216        css         chrome://resources/css/trash.css
2219        css         chrome://resources/css/widgets.css
23201       html        chrome://settings-frame/
"""

def read_table():
    for table_row_str in ref_table.splitlines():
        if table_row_str != "" and table_row_str[0] != "#":
            yield table_row_str.split()

def search_table(pos, value):
    value_str = str(value)
    assert isinstance(pos, int)
    for row_tup in read_table():
        if row_tup[pos] == value_str:
            return row_tup
    return None, None, None

def by_id(target_id):
    return search_table(0, target_id)

def by_vpath(chrome_path):
    return search_table(2, chrome_path)

def to_chrome_path(path_str):
    assert isinstance(path_str, str)
    assert path_str[0:6] == 'chrome'
    path_parts = path_str.split(os.sep)
    path_parts[0] = 'chrome:/'
    return '/'.join(path_parts)

def to_non_chrome_path(vchrome_path):
    assert isinstance(vchrome_path, str)
    p1 = vchrome_path.replace('chrome://', 'chrome/', 1)
    return p1.replace('/', os.sep)

