
import os

HERE = os.path.dirname(os.path.abspath(__file__))
INPUT = os.path.join(HERE, "../input.txt")
EXAMPLE = os.path.join(HERE, "../example.txt")


def part_1():
    print("Part 1")

    with open(INPUT, 'r') as it:
        data = it.readlines()

    lines_with_start_state = []
    got_start_state = False
    crate_stacks = {}
    for line in data:
        line = line.replace("\n", "")
        # print(line)

        if got_start_state:
            _, crates_to_move, _, from_stack, _, to_stack = line.split(" ")

            print(f"Crate Stacks BEFORE: {crate_stacks}")
            print(crates_to_move, from_stack, to_stack)

            for i in range(int(crates_to_move)):
                crate_stacks[to_stack].append(crate_stacks[from_stack].pop())

            print(f"Crate Stacks AFTER: {crate_stacks}")
        else:
            if line == "":
                print("Gap")
                got_start_state = True

                for i in lines_with_start_state[-1:][0].replace(" ", ""):
                    crate_stacks[i] = []

                for j in reversed(lines_with_start_state[:-1]):
                    n = 4
                    crates_on_line = [j[i:i + n] for i in range(0, len(j), n)]
                    # print(crates_on_line)
                    for x in range(len(crates_on_line)):
                        y = str(x + 1)
                        # print(crates_on_line[x])
                        if "[" in crates_on_line[x] and "]" in crates_on_line[x]:
                            crate_stacks[y].append(crates_on_line[x].replace("[", "").replace("]", "").replace(" ", ""))
                    # for every 4th char in non alpha line

                print(f"Crate Stacks START: {crate_stacks}")
            else:
                lines_with_start_state.append(line)

    top_of_stacks = ""
    for x in range(len(crates_on_line)):
        y = str(x + 1)
        top_of_stacks = top_of_stacks + str(crate_stacks[y][-1:][0])

    print(top_of_stacks)


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
