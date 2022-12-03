import csv
import sys
import random
import matplotlib.pyplot as plt
import numpy as np

def main():

    # Ensure correct usage
    if len(sys.argv) != 3:
        sys.exit("Usage: python rank_update.py PastRating CurrentRating")
    teams = []
    # Read teams into memory from file
    with open(sys.argv[1]) as file:
        reader = csv.DictReader(file)
        for team in reader:
            team["rating"] = float(team["rating"])
            teams.append(team)
    qualified = []
    with open(sys.argv[2]) as file:
        reader = csv.DictReader(file)
        for team in reader:
            team["rating"] = float(team["rating"])
            qualified.append(team)

    change = {}
    for team in qualified:
        change[team['team']] =round(team['rating'] - (next(item for item in teams if item["team"] == team['team']))['rating'], 2)
    plot_change(change)
    

def plot_change(change):
    # Plots the rating change
    x = list(change.keys())
    y = list(change.values())

    fig, ax1 = plt.subplots()
    color = ['r' if Y<0 else 'g' for Y in y]
    ax1.bar(x, y, color=color, align = 'center')
    plt.xticks(rotation = 90)
    plt.ylim(top = 80, bottom = -80)
    plt.show()
    return


if __name__ == "__main__":
    main()
