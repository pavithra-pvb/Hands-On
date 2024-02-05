import os

def make_folders(folders_list, nest=False):
  if nest:
    """
    Nest all the folders, like
    ./Music/fun/parliament
    """
    path_to_new_folder = "."
    for folder in folders_list:
      path_to_new_folder += "/{}".format(folder)
      try:
        print(path_to_new_folder)
        os.makedirs("./" + path_to_new_folder)
      except FileExistsError:
        continue
  else:
    """
    Makes all different folders, like
    ./Music/ ./fun/ and ./parliament/
    """
    for folder in folders_list:
      try:
        os.makedirs(folder)

      except FileExistsError:
        continue

make_folders(['Music', 'fun', 'parliament'])