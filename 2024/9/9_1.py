import time

def generate_blockmap(diskmap):
    # I picked a list to store the block map becuase I think the file IDs will be bigger than 9 in the real exmaple.
    # -1 will represent empty blocks
    blockmap = []
    is_file = True
    file_id = 0
    for char in diskmap:
        if is_file:
            blockmap.extend([file_id] * int(char))
            file_id += 1
        else:
            blockmap.extend([-1] * int(char))
        is_file = not is_file
    return blockmap

def compact_blockmap(blockmap):
    # Find free space indexes
    free_space_indexes = []
    for i in range(len(block_map)):
        if block_map[i] == -1:
            free_space_indexes.append(i)
    number_of_moves = len(free_space_indexes)

    # Find movable file block indexes
    movable_file_block_indexes = []
    i = len(block_map) - 1
    while True:
        if block_map[i] != -1:
            movable_file_block_indexes.append(i)
        if len(movable_file_block_indexes) == number_of_moves:
            break
        i -= 1

    # Make the moves
    for i in range(number_of_moves):
        from_block_index = movable_file_block_indexes[i]
        to_block_index = free_space_indexes[i]
        if from_block_index > to_block_index:
            blockmap[from_block_index] , blockmap[to_block_index] = blockmap[to_block_index] , blockmap[from_block_index]
        
def compute_block_map_checksum(block_map):
    result = 0
    index = 0
    for block in block_map:
        if block != -1:
            result += block * index
        index += 1
    return result


diskmap = ""
with open("2024/9/input.txt", mode="r") as file:
    for line in file:
        diskmap += line

part1_start_time = time.time()

block_map = generate_blockmap(diskmap)
compact_blockmap(block_map)
print(compute_block_map_checksum(block_map))

part1_end_time = time.time()
part1_runtime = part1_end_time - part1_start_time
print(f"Runtime: {part1_runtime:.6f} seconds")