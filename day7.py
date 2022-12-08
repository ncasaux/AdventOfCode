import aocd as aocd

f = aocd.get_data(day=7, year=2022)

total_size = 0
eligibleFolderSize = []
structure = []
accessedDirectoryBlocks = []


class DirectoryBlock:
    def __init__(self, name: str, size: int, content: []):
        self.name = name
        self.size = size
        self.content = content


class FileBlock:
    def __init__(self, name: str, size: int):
        self.name = name
        self.size = size


def calculate_directory_block_size(directory_block):
    size = 0
    for x in directory_block:
        if type(x) == DirectoryBlock:
            x.size = calculate_directory_block_size(x.content)
        size += x.size
    return size


def sum_directory_block_size(directory_block):
    for x in directory_block:
        if type(x) == DirectoryBlock:
            if x.size <= 100000:
                global total_size
                total_size += x.size
            sum_directory_block_size(x.content)


def get_closest_size(directory_block, size_to_match):
    for x in directory_block:
        if type(x) == DirectoryBlock:
            if x.size >= size_to_match:
                eligibleFolderSize.append(x.size)
            get_closest_size(x.content, size_to_match)


for currentLine in f.splitlines():
    instructions = currentLine.split(" ")
    match instructions[0]:
        case "$":
            match instructions[1]:
                case "cd":
                    match instructions[2]:
                        case "..":
                            accessedDirectoryBlocks.pop()
                        case _:
                            newDirectoryBlock = DirectoryBlock(instructions[2], -1, [])
                            if accessedDirectoryBlocks:
                                accessedDirectoryBlocks[-1].content.append(newDirectoryBlock)
                                accessedDirectoryBlocks.append(newDirectoryBlock)
                            else:
                                accessedDirectoryBlocks.append(newDirectoryBlock)
                                structure.append(newDirectoryBlock)
                case "ls":
                    pass
        case "dir":
            pass
        case _:
            newFileBlock = FileBlock(instructions[1], int(instructions[0]))
            accessedDirectoryBlocks[-1].content.append(newFileBlock)

print(f"Total used size is: ", calculate_directory_block_size(structure))

sum_directory_block_size(structure)
print(f"Total size of less than 100Ko folders is: {total_size}")

get_closest_size(structure, 30000000 - (70000000 - calculate_directory_block_size(structure)))
print(f"Best folder to delete has size:", min(eligibleFolderSize))
