from pathlib import Path

THIS_FILE = Path(__file__).resolve()
PARENT_DIR = Path(__file__).resolve().parent
PARENT_PARENT_DIR = Path(__file__).resolve().parent.parent
print("This file: ", THIS_FILE)
print("PARENT_DIR: ", PARENT_DIR)
print("PARENT_PARENT_DIR: ", PARENT_PARENT_DIR)

my_dir = Path(__file__)

print("--------------")
print("Current directory: ")
print(Path.cwd())

print("--------------")
print(my_dir.absolute())
print(my_dir.resolve())

print("--------------")
print("all files in directory:")
for file in Path().iterdir():
    print(file)

print("--------------")
print("Path methods on file")

print(my_dir)
print(my_dir.name)
print(my_dir.stem)
print(my_dir.suffix)
print(my_dir.resolve())
print(my_dir.resolve().parent)

print("--------------")
print("Join Paths")
print(my_dir.resolve().parent.joinpath("new_directory"))
print(my_dir.resolve().parent / "new_directory")

print("--------------")
print("file from other folder")
other_folder_file = Path("__init__.py").resolve().parent.parent / "syntax" / "syntax.py"
print(other_folder_file)
print("exists:", other_folder_file.exists())

print("--------------")
home = Path.home()
print(home)

print("--------------")
create_dir = Path("TempDir")
create_dir.mkdir(parents=True, exist_ok=True)
create_dir.rmdir()

create_file = Path("TempFile")
create_file.touch()
create_file.unlink()
