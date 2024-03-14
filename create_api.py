import os


def create_api():
    api_name = os.sys.argv[1]

    dir_name = f'./apis/{api_name}'
    if os.path.exists(dir_name):
        print(f'{api_name}APIは既に存在します')
        return

    os.makedirs(dir_name)
    open(f'{dir_name}/__init__.py', 'w').close()
    open(f'{dir_name}/models.py', 'w').close()
    open(f'{dir_name}/routers.py', 'w').close()
    open(f'{dir_name}/views.py', 'w').close()
    print(f'{api_name}APIを作成しました')


if __name__ == '__main__':
    create_api()
