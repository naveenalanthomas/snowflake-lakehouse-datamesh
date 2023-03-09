import os
import _snowflake 
import io 

def file_extension_extract(file_path): 
    text = '' 
    #file = _snowflake.open(file_path, is_owner_file=True).read()
    split_tup = os.path.splitext(file_path)
    file_extension = split_tup[1]
    if file_extension in ('.gz', '.zip'):
        file_extension = split_tup[0].split('.')[-1]
    return file_extension