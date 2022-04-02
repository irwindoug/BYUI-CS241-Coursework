import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
import os

os.chdir("/Users/me/OneDrive - BYU-Idaho/2022a-Winter/CS 241/data_analysis")

players = pd.read_csv("data/basketball_players.csv",low_memory=False)
master = pd.read_csv("data/basketball_master.csv",low_memory=False)

nba = pd.merge(players, master, how="left", left_on="playerID", right_on="bioID")

nba = nba[nba.GP > 0]

nba["reboundsPerGame"] = nba["rebounds"] / nba["GP"]

def save_multi_image(filename):
    pp = PdfPages(filename)
    fig_nums = plt.get_fignums()
    figs = [plt.figure(n) for n in fig_nums]
    for fig in figs:
        fig.savefig(pp, format='pdf', bbox_inches='tight')
    pp.close()

def main():

    # Requirement 1: Calculate the mean and median number of points scored. (In other words, each row is the amount of points a player scored during a particular season. Calculate the median of these values. The result of this is that we have the median number of points players score each season.)

    req1 = plt.figure()
    min = players["points"].min()
    max = players["points"].max()
    mean = players["points"].mean()
    median = players["points"].median()

    plt.text(.1, .5, (("Points Scored Mean: %s\nPoints Scored Median: %s") % (mean, median)), transform=req1.transFigure, ha="left")
    plt.axis('off')

    # Requirement 2: Determine the highest number of points recorded in a single season. Identify who scored those points and the year they did so.

    pd.set_option("display.max_rows", None)

    req2 = plt.figure()
    nba_topPointEarner_perYear = nba.sort_values('points', ascending=False).drop_duplicates(["year"]).sort_values("year").reset_index()

    plt.text(.1, 0, str(nba_topPointEarner_perYear[["year", "useFirst", "lastName", "points"]]))
    plt.axis('off')
    # print(nba_topPointEarner_perYear[["year", "useFirst", "lastName", "points"]])
    
    
    # Requirement 3: Produce a boxplot that shows the distribution of total points, total assists, and total rebounds (each of these three is a separate box plot, but they can be on the same scale and in the same graphic).

    req3 = plt.figure()
    sns.boxenplot(data=nba[["points","assists", "rebounds"]]).set_title("Distribution of Points, Assists, and Rebounds")

    # Requirement 4: Produce a plot that shows how the number of points scored has changed over time by showing the median of points scored per year, over time. The x-axis is the year and the y-axis is the median number of points among all players for that year.

    req4 = plt.figure()
    nba_medianPoints_perYear = nba[["points", "year"]].groupby("year").median()
    nba_medianPoints_perYear = nba_medianPoints_perYear.reset_index()
    sns.regplot(data=nba_medianPoints_perYear, x="year", y="points").set_title("Median Points per Year")

    save_multi_image("assign12.pdf")
    
if __name__ == "__main__":
    main()