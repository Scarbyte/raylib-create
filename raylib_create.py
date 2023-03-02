"""
file: raylib_create.py

Simple python script to generate a template raylib project.

Author: Mason Armand
"""
import os
import sys

def main():
    if len(sys.argv) == 1:
        print("Please provide a project name as a command line argument")
        return
    if len(sys.argv) == 2:
        print("Please provide a destination directory as a command line argument.")
        return

    project_name = sys.argv[1]
    directory = sys.argv[2]

    os.mkdir(f'{directory}{project_name}')
    print("Created project directory.")

    os.mkdir(f'{directory}{project_name}/src') # source folder
    print("Created project src directory.")

    os.mkdir(f'{directory}{project_name}/res') # res folder
    print("Created project res directory.")

    with open(f"{directory}{project_name}/src/main.c", "w", encoding="UTF-8") as file:
        file.write(get_template_contents(project_name))
        print(f"Created {directory}{project_name}/src/main.c")

    with open(f"{directory}{project_name}/src/{project_name}.h", "w", encoding="UTF-8") as file:
        file.write(get_header_contents(project_name))
        print(f"Created {directory}{project_name}/src/{project_name}.h")

    with open(f"{directory}{project_name}/makefile", "w", encoding="UTF-8") as file:
        file.write(get_makefile_contents(project_name))
        print(f"Created {directory}{project_name}/makefile")

    # gdbinit
    gdb_str = ""
    with open("gdbinit.txt", "r", encoding="UTF-8") as file:
        gdb_str = file.read()

    with open(f"{directory}{project_name}/gdbinit", "w", encoding="UTF-8") as file:
        file.write(gdb_str)
        print(f"Created gdb config ({directory}{project_name}/gdbinit)")


def get_template_contents(project_name: str) -> str:
    main_file_contents = ""

    with open("main.txt", "r", encoding="UTF-8") as file:
        main_file_contents = file.read().replace("PROJECT_NAME", project_name)

    return main_file_contents


def get_header_contents(project_name: str) -> str:
    header_file_contents = ""

    with open("header.txt", "r", encoding="UTF-8") as file:
        header_file_contents = file.read().replace("PROJECT_NAME",
                project_name.upper())

    return header_file_contents


def get_makefile_contents(project_name: str) -> str:
    makefile_contents = ""

    with open("makefile.txt", "r", encoding="UTF-8") as file:
        makefile_contents = file.read().replace("PROJECT_NAME",
                project_name)

    return makefile_contents


if __name__ == "__main__":
    main()
