import csv
import sys
import random

def main():

    # Ensure correct usage
    if len(sys.argv) != 3:
        sys.exit("Usage: python rank_update.py CurrentRank MatchResults")

    teams = []
    # Read teams into memory from file
    with open(sys.argv[1]) as file:
        reader = csv.DictReader(file)
        for team in reader:
            team["rating"] = float(team["rating"])
            teams.append(team)
    # print(teams)
    file1 = open(sys.argv[2], 'r')
    lines = file1.readlines()
    for line in lines:
        t1, t1g, t2, t2g = line.split()
        t1g = int(t1g)
        t2g = int(t2g)
        for team in teams:
            if team['team'] == t1:
                team1 = team
            elif team['team'] == t2:
                team2 = team
        update_rank(team1, team2, t1g, t2g)
    file1.close()

    columns = ['team', 'rating']
    qualified = ["Netherlands", "USA", "Argentina", "Australia",
    "Japan", "Croatia", "Brazil", "Korea", "France", "Poland",
    "England", "Senegal", "Morocco", "Spain", "Portugal",
    "Switzerland"]

    csv_file = "Latest_Ranking.csv"
    with open(csv_file, 'w') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=columns)
        writer.writeheader()
        for team in teams:
            if team["team"] not in qualified:
                continue
            writer.writerow(team)

def update_rank(team1, team2, t1g, t2g):
    R1o = team1['rating']
    R2o = team2["rating"]
    K = 50
    G = countG(abs(t1g-t2g))
    W1, W2 = W(t1g, t2g)
    We1, We2 = We(R1o, R2o)
    team1['rating'] = R1o + (K * G * (W1 - We1))
    team2['rating'] = R2o + (K * G * (W2 - We2))
    return



def countG(gd):
    if gd <= 1:
        return 1
    if gd == 2:
        return 1.5
    return (11 + 3) / 8


def W(t1g, t2g):
    if t1g == t2g:
        return (0.5, 0.5)
    if t1g > t2g:
        return (1, 0)
    return (0,1)


def We(R1o, R2o):
    w1 = 1 / (1 + 10 ** ((R1o - R2o) / - 600))
    w2 = 1 / (1 + 10 ** ((R2o - R1o) / - 600))
    return (w1, w2)


if __name__ == "__main__":
    main()
