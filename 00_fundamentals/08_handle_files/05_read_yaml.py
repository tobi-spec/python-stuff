import yaml

with open("./files/test.yaml", "r") as file:
    yaml_file = yaml.safe_load(file)
    print(yaml_file)
    print(type(yaml_file))
