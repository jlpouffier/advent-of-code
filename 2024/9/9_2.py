import time

def generate_blockmap(diskmap):
    # For part 2 i'm storing the blockmap as a list of dict. Each dict containing its size, initial index, and file ID
    blockmap = []
    is_file = True
    file_id = 0
    index = 0
    for char in diskmap:
        if is_file:
            blockmap.append({
                'start_index': index,
                'size': int(char),
                'file_id': file_id
            })
            file_id += 1
        index += int(char)    
        is_file = not is_file
    return blockmap

def get_free_spaces(blockmap):
    free_spaces = []
    for i,j in zip(blockmap , blockmap[1:]):
        free_space_size = j['start_index'] - i['start_index'] - i['size']
        if free_space_size > 0:
            free_space_start = i['start_index'] + i['size']
            free_spaces.append({
                'start_index': free_space_start,
                'size': free_space_size,
            })
    return free_spaces

def compact_blockmap(blockmap):
    blockmap_copy = [block for block in blockmap]
    free_spaces = get_free_spaces(blockmap_copy)
    for i in range(len(blockmap)):
        last_i = len(blockmap) - 1 - i
        for free_space in free_spaces:
            if blockmap[last_i]['size'] <= free_space['size']:
                if blockmap[last_i]['start_index'] >= free_space['start_index']:
                    blockmap_copy.remove(blockmap[last_i])
                    blockmap_copy.append({
                        'start_index': free_space['start_index'],
                        'size': blockmap[last_i]['size'],
                        'file_id': blockmap[last_i]['file_id'],
                    })
                    blockmap_copy.sort(key=lambda x: x['start_index'])
                    free_spaces = get_free_spaces(blockmap_copy)
                    break
    return blockmap_copy

def compute_block_map_checksum(block_map):
    result = 0
    for block in block_map:
        size = block['size']
        start_index = block['start_index']
        value = block['file_id']
        for i in range(size):
            result += value * (start_index + i)
    return result

diskmap = ""
with open("2024/9/input.txt", mode="r") as file:
    for line in file:
        diskmap += line

part2_start_time = time.time()

block_map = generate_blockmap(diskmap)
block_map = compact_blockmap(block_map)
print(compute_block_map_checksum(block_map))

part2_end_time = time.time()
part2_runtime = part2_end_time - part2_start_time
print(f"Runtime: {part2_runtime:.6f} seconds")