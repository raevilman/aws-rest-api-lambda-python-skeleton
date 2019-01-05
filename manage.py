import os
import sys
import io
from zipfile import ZipFile, ZIP_DEFLATED
# import boto3
import json

lib_path = 'venv/Lib/site-packages'


def should_include(file_dir, file):
    if(
            str(file_dir).endswith('egg-info')
            or str(file_dir).endswith('dist-info')
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
                print('[Include] '+root, file)
            else:
                print('[Skipped] '+root, file)
    return file_paths


def export_archive():
    lib_paths = get_files_to_archive(lib_path)
    app_paths = get_files_to_archive('app')
    file_paths = lib_paths + app_paths
    # buf = io.BytesIO()
    # with zipfile.ZipFile(buf, 'w', zipfile.ZIP_DEFLATED) as zfh:
    #     # Add my main file
    #     zfh.write('lambda_function.py')
    # buf.seek(0)
    # pkg = buf.read()
    # return pkg
    # writing files to a zipfile
    with ZipFile('lambda_build.zip', 'w') as zip:
        zip.write('lambda_function.py')
        # writing each file one by one
        for file in file_paths:
            zip.write(file,file.replace(lib_path,''))

    print('All files zipped successfully!')


def archive():
    lib_paths = get_files_to_archive(lib_path)
    app_paths = get_files_to_archive('app')
    file_paths = lib_paths + app_paths
    buf = io.BytesIO()
    with ZipFile(buf, 'w', ZIP_DEFLATED) as zfh:
        # Add my main file
        zip.write('lambda_function.py')
        # writing each file one by one
        for file in file_paths:
            zip.write(file, file.replace(lib_path, ''))
    buf.seek(0)
    pkg = buf.read()
    return pkg


def environment():
    with open('config.json') as config_file:
        env_json = json.load(config_file)

    return env_json


def zip_create_function():
    pass
    # lambda_client = boto3.client('lambda')
    #
    # pkg = archive()
    # env_json = environment()
    #
    # response = lambda_client.create_function(
    #     FunctionName='Py3Lambda',
    #     Runtime='python3.6',
    #     Role='<<your role ARN>>',
    #     Handler='app.lambda_handler',
    #     Code={'ZipFile': pkg},
    #     Environment={
    #         'Variables': env_json
    #     },
    #     Description='Python3 Lambda function',
    #     Timeout=60,
    #     MemorySize=128,
    #     Publish=True
    # )
    #
    # print(json.dumps(response))


def zip_update_function():
    pass
    # lambda_client = boto3.client('lambda')
    #
    # pkg = archive()
    # env_json = environment()
    #
    # response = lambda_client.update_function_code(
    #     FunctionName='Py3Lambda',
    #     ZipFile=pkg,
    #     Publish=True
    # )
    #
    # print(json.dumps(response))
    #
    # response = lambda_client.update_function_configuration(
    #     FunctionName='Py3Lambda',
    #     Environment={
    #         'Variables': env_json
    #     }
    # )
    #
    # print(json.dumps(response))


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print('Invalid option')
    elif sys.argv[1] == 'create':
        zip_create_function()
    elif sys.argv[1] == 'update':
        zip_update_function()
    elif sys.argv[1] == 'archive':
        archive()
    elif sys.argv[1] == 'export_archive':
        export_archive()
    else:
        print('Invalid option')
