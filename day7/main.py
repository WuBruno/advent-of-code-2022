from collections import deque

class Directories():
    file_sizes = 0
    subdirectories = []

    def __init__(self, f, c):
        file_sizes = f
        children = c

    def __str__(self):
        return file_sizes + " " + str(subdirectories)

    def __repr__(self):
        return str(self.file_sizes) + " " + str(self.subdirectories)

def main():
    text_input = open("input.txt", "r")

    directories = {}
    stack = deque()

    curr_files = 0
    curr_subdirectories = []
    on_ls = False

    # Build the tree
    for line in text_input:
        parts = line.strip().split(" ")
        if parts[0] == "$":
            if parts[1] == "cd":
                if on_ls:
                    name = stack[len(stack)-1]
                    if name not in directories:
                        directories[name] = Directories(curr_files, curr_subdirectories)
                    on_ls = False

                if parts[2] == "..":
                    stack.pop()
                else:
                    stack.append(parts[1])

            elif parts[1] == "ls":
                curr_files == 0
                curr_subdirectories == []
                on_ls = True
        else:
            if parts[0] == "dir":
                curr_subdirectories.append(parts[1])
            else:
                curr_files += int(parts[0])


    print(directories)


    # Traverse and sum the tree at different points



print(main())
