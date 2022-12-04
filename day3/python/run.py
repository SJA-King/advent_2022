
import os

HERE = os.path.dirname(os.path.abspath(__file__))
INPUT = os.path.join(HERE, "../input.txt")


def part_1():
    print("Part 1")

    with open(INPUT, 'r') as it:
        data = it.readlines()

    sum_of_priorities = 0
    for line in data:
        line = line.replace("\n", "").strip()
        split = int(len(line) / 2)
        # print(split)
        print(line[:split], line[split:])

        in_both = set(line[split:]).intersection(set(line[:split]))

        in_both = ''.join(in_both)


        if in_both.islower():
            char_priority = ord(in_both) - 96

            # print(f"lower")
        elif in_both.isupper():
            # in_both = in_both.lower()
            char_priority = ord(in_both) - 38
            # print("upper")
        else:
            raise Exception("Unknown")

        print(f"In Both: {in_both}, Priority: {char_priority}")
        sum_of_priorities += char_priority

    print(f"Sum of priorities: {sum_of_priorities}")


def part_2():
    print("Part 2")

    with open(INPUT, 'r') as it:
        data = it.readlines()

    three_bags = []
    sum_of_priorities = 0
    for line in data:
        line = line.replace("\n", "").strip()

        # if not three_bags:
        three_bags.append(line)
        # elif len(three_bags) < 2:
        #     three_bags.append(line)
        if len(three_bags) > 2:
            print(three_bags)
            in_three = set(three_bags[0]).intersection(set(three_bags[1])).intersection(set(three_bags[2]))

            in_three = ''.join(in_three)

            char_priority = 0
            for badge in in_three:

                if badge.islower():
                    char_priority += ord(badge) - 96

                    # print(f"lower")
                elif badge.isupper():
                    # in_both = in_both.lower()
                    char_priority += ord(badge) - 38
                    # print("upper")
                else:
                    raise Exception("Unknown")

            three_bags = []

            print(f"In Three: {in_three}, Priority: {char_priority}")
            sum_of_priorities += char_priority

    print(f"Sum of priorities: {sum_of_priorities}")



def main():
    print("Day 1")

    part_1()
    part_2()


if __name__ == "__main__":
    main()
