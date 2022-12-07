
import os
from typing import Any

HERE = os.path.dirname(os.path.abspath(__file__))
INPUT = os.path.join(HERE, "../input.txt")
EXAMPLE = os.path.join(HERE, "../example.txt")

ALL_DIRECTORIES = {}


class AFile:
    def __init__(self, a_name: str, a_size: Any = 0):
        self.name = a_name
        self.size = a_size

    def get_size(self):
        # if self.size:
        return self.size
        # raise Exception("Size isnt SET!")


class AFolder(AFile):

    def __init__(self, a_name: str):
        AFile.__init__(self, a_name, 0)
        self.folders = []
        self.files = []

    def add_folder(self, folder_name: str):
        self.folders.append(folder_name)
        if len(self.folders) != len(set(self.folders)):
            raise Exception(f"Duplicate Folders: {self.folders}")

    def add_file(self, file_name: str, file_size: int):
        self.size += file_size
        self.files.append(AFile(file_name, file_size))
        if len(self.files) != len(set(self.files)):
            raise Exception(f"Duplicate Files: {self.files}")

    def get_folders(self):
        # if self.folders:
        return self.folders
        # raise Exception("Folders isnt SET!")

    def get_files(self):
        # if self.files:
        return self.files
        # return

    def get_file_names_sizes(self):
        return_string = ""
        for i_file in self.files:
            return_string += f"<{i_file.name}:{i_file.size}>"
        return return_string

    def get_size(self):
        self.set_size()
        return self.size

    def set_size(self):
        # sum_of_file_sizes = self.size
        # for a_file in self.get_files():
        #     sum_of_file_sizes += a_file.get_size()

        sum_of_folder_sizes = 0
        for a_folder in self.get_folders():
            sum_of_folder_sizes += ALL_DIRECTORIES[a_folder].get_size()

        self.size += sum_of_folder_sizes

    def print_size(self):
        print(self.get_size())


def part_1():
    print("Part 1")

    with open(EXAMPLE, 'r') as it:
        data = it.readlines()

    directory_stack = []
    current_directory = None
    last_cmd_ls = False
    for line in data:
        line = line.replace("\n", "")

        if "$" == line[0]:
            last_cmd_ls = False
            print("Command:")
            if "cd" in line:
                _, _, directory = line.split(" ")
                print(f"CD -> {directory}")

                if directory != "..":
                    directory_stack.append(directory)
                else:
                    directory_stack.pop()

                # Want last directory in stack
                current_directory = directory_stack[-1]
                if current_directory not in ALL_DIRECTORIES:
                    ALL_DIRECTORIES[current_directory] = AFolder(a_name=current_directory)

                print(f"CWD: {current_directory}")

            elif "ls" in line:
                print("ls")
                last_cmd_ls = True

            else:
                raise Exception(f"Unknown CMD {line}!")
        elif last_cmd_ls:
            # Expecting ls output
            ls_one, ls_two = line.split(" ")

            if ls_one == "dir":
                if ls_two not in ALL_DIRECTORIES:
                    ALL_DIRECTORIES[ls_two] = AFolder(a_name=ls_two)

                ALL_DIRECTORIES[current_directory].add_folder(ls_two)
            elif type(int(ls_one)) == int:
                ls_one = int(ls_one)

                ALL_DIRECTORIES[current_directory].add_file(file_name=ls_two, file_size=ls_one)

        else:
            raise Exception(f"Unknown Line {line}!")

    for folder_name, folder_obj in ALL_DIRECTORIES.items():
        print(f"Folder: {folder_name}")
        print(f"is size: {folder_obj.get_size()}")
        print(f"Files: {folder_obj.get_file_names_sizes()}")


def part_2():
    print("Part 2")

    with open(INPUT, 'r') as it:
        data = it.readlines()


def main():
    print("Day 1")

    part_1()
    part_2()


if __name__ == "__main__":
    main()
