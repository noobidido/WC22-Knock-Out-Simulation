# Simulate a sports tournament

import csv
import sys
import random
import matplotlib.pyplot as plt

# Number of simluations to run
N = 14000605 # Number of outcomes Dr. Strange saw

def main():

    # Ensure correct usage
    if len(sys.argv) != 2:
        sys.exit("Usage: python tournament.py FILENAME")

    teams = []
    # Read teams into memory from file
    with open(sys.argv[1]) as file:
        reader = csv.DictReader(file)
        for team in reader:
            team["rating"] = float(team["rating"])
            teams.append(team)

    counts = {}
    for team in teams:
        counts[team["team"]] = 0

    # Simulates N tournaments and keep track of win counts
    for i in range(N):
        counts[simulate_tournament(teams)] += 1

    # Plots the counts of winnings
    plot_winnings(counts)

    # Print each team's chances of winning, according to simulation
    for team in sorted(counts, key=lambda team: counts[team], reverse=True):
        print(f"{team}: {counts[team] * 100 / N:.1f}% chance of winning")


def simulate_game(team1, team2):
    """Simulate a game. Return True if team1 wins, False otherwise."""
    rating1 = team1["rating"]
    rating2 = team2["rating"]
    probability = 1 / (1 + 10 ** ((rating2 - rating1) / 600))
    return random.random() < probability


def simulate_round(teams):
    """Simulate a round. Return a list of winning teams."""
    winners = []

    # Simulate games for all pairs of teams
    for i in range(0, len(teams), 2):
        if simulate_game(teams[i], teams[i + 1]):
            winners.append(teams[i])
        else:
            winners.append(teams[i + 1])

    return winners


def simulate_tournament(teams):
    """Simulate a tournament. Return name of winning team."""

    # Simulate a tournament until one team remains
    while len(teams) > 1:
        teams = simulate_round(teams)

    return teams[0]["team"]

def plot_winnings(counts):
    # Plots the counts of winnings
    yaxis = list(counts.keys())
    xaxis = [(x * 100 / N)  for x in list(counts.values())]
    yaxis.reverse()
    xaxis.reverse()
    plt.barh(yaxis, xaxis, align='center', )
    plt.title('WC2022 Knock-Out Simulation')
    plt.xlabel('% of tournament wins')
    plt.show()
    return


if __name__ == "__main__":
    main()
