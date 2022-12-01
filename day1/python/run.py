
import os

HERE = os.path.dirname(os.path.abspath(__file__))
INPUT = os.path.join(HERE, "input.txt")

def part_1():
    print("Part 1")
    # print(HERE)

    with open(INPUT, 'r') as it:
        data = it.readlines()

    max_calorie = 0
    count = 0
    for line in data:
        line = line.replace("\n", "")
        # print(line)
        if line != "":
            count += int(line)
        else:
            # print(count)
            if count > max_calorie:
                max_calorie = count
            count = 0

    print(f"Elf carrying most calories is carrying: {max_calorie}")


def part_2():
    print("Part 2")

    with open(INPUT, 'r') as it:
        data = it.readlines()

    calories = []
    count = 0
    for line in data:
        line = line.replace("\n", "")
        # print(line)
        if line != "":
            count += int(line)
        else:
            calories.append(count)
            count = 0

    top_elfs_calories = sorted(calories)[-3:]
    sum_top_elfs_calories = sum(top_elfs_calories)
    print(f'Total Calories of top 3 elfs is: {sum_top_elfs_calories}')


def main():
    print("Day 1")

    part_1()
    part_2()


if __name__ == "__main__":
    main()
