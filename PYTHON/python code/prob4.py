# write python program to print the contents of a directory using the os module. search online for the function which does that.

# import os

# # Specify the directory path
# directory_path = '/' # Current directory

# # List all entries in the directory
# entries = os.listdir(directory_path)

# # Print each entry
# for entry in entries:
#     print(entry)

    # or -------------------------------------------------------------------------------------------

# import os

# def walk_limited_depth(directory, max_depth):
#     base_depth = directory.rstrip(os.path.sep).count(os.path.sep)
#     for dirpath, dirnames, filenames in os.walk(directory, onerror=lambda e: print(f"Error: {e}")):
#         current_depth = dirpath.rstrip(os.path.sep).count(os.path.sep)
#         if current_depth - base_depth >= max_depth:
#             dirnames[:] = []  # Stop deeper walk
#         print(f'Found directory: {dirpath}')
#         for file_name in filenames:
#             print(f'\t{file_name}')

# walk_limited_depth('/', max_depth=2)

 #  or ------------------------------------------------------------------------------------------------

import os

# Select the directory whose content you want to list 
directory_path = '/'
with os.scandir(directory_path) as entries:
    for entry in entries:
        print(entry.name)
