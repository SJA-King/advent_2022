
import os

HERE = os.path.dirname(os.path.abspath(__file__))
INPUT = os.path.join(HERE, "../input.txt")

class Score():
    score = None

    def __init__(self, my_score_value):
        self.score = my_score_value

    def get_score(self):
        return self.score


class RPS(Score):
    n_opp = None
    n_you = None

    def __init__(self, score, letter_for_opponent, letter_for_player):
        Score.__init__(self, score)
        self.n_opp = letter_for_opponent
        self.n_you = letter_for_player

    def get_player(self):
        return self.n_you

    def get_opp(self):
        return self.n_opp


ROCK = RPS(1, 'A', 'X')
PAPER = RPS(2, 'B', 'Y')
SCISSORS = RPS(3, 'C', 'Z')
DRAW = Score(3)
WIN = Score(6)
LOSS = Score(0)

BEATS = {
    ROCK: SCISSORS,
    SCISSORS: PAPER,
    PAPER: ROCK
}

LOSSES = {
    ROCK: PAPER,
    SCISSORS: ROCK,
    PAPER: SCISSORS
}


def part_1():
    print("Part 1")

    with open(INPUT, 'r') as it:
        data = it.readlines()

    total_score = 0
    for line in data:
        score = 0
        # print(f"Line: {line}")
        opp, player = line.replace("\n", "").split(" ")
        # print(f"Opp: {opp}, Player: {player}")

        if ROCK.get_opp() == opp:
            opp = ROCK
        elif SCISSORS.get_opp() == opp:
            opp = SCISSORS
        elif PAPER.get_opp() == opp:
            opp = PAPER
        else:
            raise Exception("Unknown Opp")

        # print(player)
        if ROCK.get_player() == player:
            player = ROCK
        elif SCISSORS.get_player() == player:
            player = SCISSORS
        elif PAPER.get_player() == player:
            player = PAPER
        else:
            raise Exception("Unknown Player")

        score += player.get_score()

        if opp == player:
            score += DRAW.get_score()
        elif BEATS[player] == opp:
            score += WIN.get_score()
        elif BEATS[opp] == player:
            score += LOSS.get_score()

        # print(f"Score: {score}")
        total_score += score

    print(f"Total Score: {total_score}")


def part_2():
    print("Part 2")

    with open(INPUT, 'r') as it:
        data = it.readlines()

    flump = {
        'X': LOSS,
        'Y': DRAW,
        'Z': WIN,
    }
    total_score = 0
    for line in data:
        score = 0
        # print(f"Line: {line}")
        opp, result = line.replace("\n", "").split(" ")
        print(f"Opp: {opp}, Result: {result}")

        if ROCK.get_opp() == opp:
            opp = ROCK
        elif SCISSORS.get_opp() == opp:
            opp = SCISSORS
        elif PAPER.get_opp() == opp:
            opp = PAPER
        else:
            raise Exception("Unknown Opp")

        if flump[result] == DRAW:
            score += DRAW.get_score()
            score += opp.get_score()

        elif flump[result] == LOSS:
            score += LOSS.get_score()
            score += BEATS[opp].get_score()

        elif flump[result] == WIN:
            score += WIN.get_score()
            score += LOSSES[opp].get_score()

        else:
            raise Exception(f"Score: {score}")

        total_score += score

    print(f"Total Score: {total_score}")


def main():
    print("Day 1")

    part_1()
    part_2()


if __name__ == "__main__":
    main()
