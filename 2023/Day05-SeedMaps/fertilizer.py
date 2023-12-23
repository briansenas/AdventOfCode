import argparse
import re


def generate_map(
    destination: int,
    source: int,
    length: int
):
    return {source: (destination, length)}


def parse_maps(
    maps: list[list[str]],
):
    fertilizer_map = []
    for i, map_ in enumerate(maps):
        source_keys = []
        destination_keys = []
        lengths = []
        for manual in map_:
            manual = manual.split(' ')
            destination_keys.append(manual[0])
            source_keys.append(manual[1])
            lengths.append(manual[2])
        indexes = [i for i in range(len(map_))]
        indexes = sorted(indexes, key=lambda x: source_keys[x])
        source_keys = [int(source_keys[i]) for i in indexes]
        destination_keys = [int(destination_keys[i]) for i in indexes]
        lengths = [int(lengths[i]) for i in indexes]
        fertilizer_map.append((source_keys, destination_keys, lengths))
    return fertilizer_map


def find_seed(
    seed: int,
    sources: list[int],
    lengths: list[int]
):
    for i, value in enumerate(sources):
        if value <= seed and value + lengths[i] > seed:
            return i, seed - value
    return -1, 0


def search_location(
    seed: int,
    fertilizer_map: list[list[dict]],
    i: int = 0
):
    if i >= len(fertilizer_map):
        return seed
    sources, destinations, lengths = fertilizer_map[i]
    destinations.append(seed)
    index, distance = find_seed(seed, sources, lengths)
    location = search_location(
        destinations[index] + distance, fertilizer_map, i+1
    )
    del destinations[-1]
    return location


def search_locations(
    seeds: list[int],
    fertilizer_map: list[list[dict]],
):
    locations = []
    for seed in seeds:
        locations.append(search_location(seed, fertilizer_map))
    return locations


def read_file(filename: str):
    regex_expr = re.compile(r".*?map:")
    with open(input_args.input, 'r') as file:
        seeds = file.readline().split(':')[1].strip().split(' ')
        file.readline()
        file.readline()
        maps = file.read()
        maps = re.split(regex_expr, maps)
    maps = "".join(maps)
    maps = maps.split('\n\n')
    maps = [x.strip('\n') for x in maps]
    maps = [x.split('\n') for x in maps]
    seeds = [int(x) for x in seeds]
    return seeds, maps


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--input', type=str,
                        default='input.txt')
    input_args = parser.parse_args()
    seeds, maps = read_file(input_args.input)
    fertilizer_map = parse_maps(maps)
    locations = search_locations(seeds, fertilizer_map)
    print(min(locations))
