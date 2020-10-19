import os
from zipfile import ZipFile, ZIP_DEFLATED

lib_path = 'venv/Lib/site-packages'


def should_include(file_dir, file):
    if (
            str(file_dir).endswith('egg-info')
            # or str(file_dir).endswith('dist-info')
            or str(file_dir).startswith(os.path.join(lib_path, 'pip'))
            or str(file_dir).__contains__('__pycache__')
            or (str(file).startswith('setuptools') and str(file).endswith('egg'))
    ):
        return False
    else:
        return True


def get_files_to_archive(dir_name):
    file_paths = []
    for root, _, files in os.walk(dir_name):
        for file in files:
            if should_include(root, file):
                file_path = os.path.join(root, file)
                file_paths.append(file_path)
                print('[Include] ' + root, file)
            else:
                print('[Skipped] ' + root, file)
    return file_paths


def export_archive():
    lib_paths = get_files_to_archive(lib_path)
    app_paths = get_files_to_archive('app')
    file_paths = lib_paths + app_paths
    with ZipFile('lambda_build.zip', 'w', ZIP_DEFLATED) as zip_util:
        zip_util.write('lambda_function.py')
        # writing each file one by one
        for file in file_paths:
            zip_util.write(file, file.replace(lib_path, ''))

    print('All files zipped successfully!')


if __name__ == '__main__':
    export_archive()
