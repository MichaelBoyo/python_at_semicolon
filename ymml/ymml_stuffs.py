import pathlib
import yaml

file_path = pathlib.Path("./config.yaml").resolve()
textwrap = {'name': 'Boyo', 'age': 18, 'children': ["odogwu", "dorcas"]}


def write():
    with file_path.open(mode='w') as file:
        yaml.dump(textwrap, file, sort_keys=False)


def read():
    with file_path.open(mode='r') as file:
        # return yaml.safe_load(file)
        return yaml.load(file, yaml.Loader)


write()
print(read())
