
import os

HERE = os.path.dirname(os.path.abspath(__file__))
INPUT = os.path.join(HERE, "../input.txt")
EXAMPLE = os.path.join(HERE, "../example.txt")


def part_1():
    print("Part 1")

    with open(INPUT, 'r') as it:
        data = it.readlines()

    for line in data:
        line = line.replace("\n", "")
        window = 4
        for i in range(len(line)):
            chars = line[i:i+window]
            chars = [*chars]
            print(chars, set(chars))
            # print(list(set(chars)))
            if sorted(list(set(chars))) == sorted(chars):
                # print(chars)
                print(i + window)
                break
            # print(chars)







def part_2():
    print("Part 2")

    with open(INPUT, 'r') as it:
        data = it.readlines()

    for line in data:
        line = line.replace("\n", "")
        window = 14
        for i in range(len(line)):
            chars = line[i:i+window]
            chars = [*chars]
            print(chars, set(chars))
            # print(list(set(chars)))
            if sorted(list(set(chars))) == sorted(chars):
                # print(chars)
                print(i + window)
                break


def main():
    print("Day 1")

    part_1()
    part_2()


if __name__ == "__main__":
    main()
