
import os

HERE = os.path.dirname(os.path.abspath(__file__))
INPUT = os.path.join(HERE, "../input.txt")


def part_1():
    print("Part 1")

    with open(INPUT, 'r') as it:
        data = it.readlines()

    overlap_count = 0
    for line in data:
        line = line.replace("\n", "").strip()

        elf_one, elf_two = line.split(",")

        elf_one_start = list(map(int, elf_one.split("-")))[0]
        elf_one_stop = list(map(int, elf_one.split("-")))[1]
        # print(list(map(int, elf_one.split("-"))))
        elf_one_zones = set(map(int, range(elf_one_start, elf_one_stop + 1)))

        elf_two_start = list(map(int, elf_two.split("-")))[0]
        elf_two_stop = list(map(int, elf_two.split("-")))[1]
        elf_two_zones = set(map(int, range(elf_two_start, elf_two_stop + 1)))

        print(f"Elf 1: {elf_one_zones}, Elf 2: {elf_two_zones}")

        zones_intersect = elf_one_zones.intersection(elf_two_zones)
        if zones_intersect:
            if zones_intersect == elf_two_zones or zones_intersect == elf_one_zones:
                print(f"Zone contains the other: {zones_intersect}")
                overlap_count += 1

    print(f"Elfs overlap: {overlap_count} many times!")


def part_2():
    print("Part 2")

    with open(INPUT, 'r') as it:
        data = it.readlines()

    overlap_count = 0
    for line in data:
        line = line.replace("\n", "").strip()

        elf_one, elf_two = line.split(",")

        elf_one_start = list(map(int, elf_one.split("-")))[0]
        elf_one_stop = list(map(int, elf_one.split("-")))[1]
        # print(list(map(int, elf_one.split("-"))))
        elf_one_zones = set(map(int, range(elf_one_start, elf_one_stop + 1)))

        elf_two_start = list(map(int, elf_two.split("-")))[0]
        elf_two_stop = list(map(int, elf_two.split("-")))[1]
        elf_two_zones = set(map(int, range(elf_two_start, elf_two_stop + 1)))

        print(f"Elf 1: {elf_one_zones}, Elf 2: {elf_two_zones}")

        zones_intersect = elf_one_zones.intersection(elf_two_zones)
        if zones_intersect:
            overlap_count += 1

    print(f"Elfs overlap: {overlap_count} many times!")


def main():
    print("Day 1")

    part_1()
    part_2()


if __name__ == "__main__":
    main()
