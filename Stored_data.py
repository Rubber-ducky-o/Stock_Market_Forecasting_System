from pathlib import Path

def creating_folder():
    path_folder = Path('stored_stock_data')
    if path_folder.is_dir():
        return
    else:
        print('Folder to store stock data will be created named Stored_stock_data, ensure that the '
              'folder is not accidentally deleted.')
        path_folder.mkdir(parents = True, exist_ok = True)
    return 'Folder has been created'