import os
import shutil

paths = {
    'chrome_path': os.path.join('C:', os.sep, 'Users', os.getlogin(), 'AppData', 'Local', 'Google', 'Chrome', 'User Data', 'Default', 'Cookies'),
    'opera_path': os.path.join('C:', os.sep, 'Users', os.getlogin(), 'AppData', 'Roaming', 'Opera Software', 'Opera Stable', 'Cookies'),
    'firefox_path': os.path.join('C:', os.sep, 'Users', os.getlogin(), 'AppData', 'Roaming', 'Mozilla', 'Firefox', 'Profiles'),
    'edge_path': os.path.join('C:', os.sep, 'Users', os.getlogin(), 'AppData', 'Local', 'Microsoft', 'Edge', 'User Data', 'Default', 'Cookies'),
    'brave_path': os.path.join('C:', os.sep, 'Users', os.getlogin(), 'AppData', 'Local', 'BraveSoftware', 'Brave-Browser', 'User Data', 'Default')

}

for i, (name, path) in enumerate(paths.items(), start=1):
    print(f'Checking {name} at {path}')
    if os.path.isdir(path):
        print(f'Directory exists for {name}')
        output_path = os.path.join('C:', os.sep, 'Users', os.getlogin(), 'Desktop', f'Cookies_{i}')
        shutil.make_archive(output_path, 'zip', path)
        print(f'{name} has been archived and moved to the desktop.')
    else:
        print(f'Directory does not exist for {name}')

print('Archiver has been finalized and the output file descriptor has closed.')
os.system('pause')