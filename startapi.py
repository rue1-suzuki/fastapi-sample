import os


def startapi(api_name: str):
    dir_name = f'./apis/{api_name}'

    if os.path.exists(dir_name):
        print(f'{api_name}API is already exists')
        return False

    os.makedirs(dir_name)
    open(f'{dir_name}/__init__.py', 'w').close()
    open(f'{dir_name}/models.py', 'w').close()
    open(f'{dir_name}/routers.py', 'w').close()
    open(f'{dir_name}/views.py', 'w').close()
    print(f'{api_name}API is created')
    return True


if __name__ == '__main__':
    if len(os.sys.argv) == 1:
        print('API names is required')
        os.sys.exit(1)

    for api_name in os.sys.argv[1:]:
        startapi(api_name)
