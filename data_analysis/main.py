'''
Program: Data Analysis
Brother Mellor, CS 241
Author: Doug Irwin
'''

# Library Imports
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
import os

# Root folder
os.chdir("/Users/me/OneDrive - BYU-Idaho/2022a-Winter/CS 241/data_analysis")

# Import data from files
players = pd.read_csv("data/basketball_players.csv",low_memory=False)
master = pd.read_csv("data/basketball_master.csv",low_memory=False)

# Merge data into one variable
nba = pd.merge(players, master, how="left", left_on="playerID", right_on="bioID")

# Remove player statistics that didn't play
nba = nba[nba.GP > 0]

# Statistics for rebounds per game average
nba["reboundsPerGame"] = nba["rebounds"] / nba["GP"]

# Function to save multiple figures (one per page) into one pdf
def save_multi_image(filename):
    pp = PdfPages(filename)
    fig_nums = plt.get_fignums()
    figs = [plt.figure(n) for n in fig_nums]
    for fig in figs:
        fig.savefig(pp, format='pdf', bbox_inches='tight')
    pp.close()

def main():

    """##### - Part One - ######"""
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

    """##### - Part Two - ######"""
    # Requirement 1: Some players score a lot of points because they attempt a lot of shots. Among players that have scored a lot of points, are there some that are much more efficient (points per attempt) than others?

    req5 = plt.figure()
    nba["attempts"] = nba["fgAttempted"]+nba["ftAttempted"]+nba["threeAttempted"]
    nba["efficiency"] = nba["points"]/nba["attempts"]

    sns.boxenplot(data=nba[["efficiency", "attempts"]])

    # Requirement 2: It seems like some players may excel in one statistical category, but produce very little in other areas. Are there any players that are exceptional across many categories?
    
    req6 = plt.figure()


    # Requirement 3: Much has been said about the rise of the three-point shot in recent years. It seems that players are shooting and making more three-point shots than ever. Recognizing that this dataset doesn't contain the very most recent data, do you see a trend of more three-point shots either across the league or among certain groups of players? Is there a point at which popularity increased dramatically?

    req7 = plt.figure()


    """##### - Part Three - ######"""
    # Requirement 1: Many sports analysts argue about which player is the GOAT (the Greatest Of All Time). Based on this data, who would you say is the GOAT? Provide evidence to back up your decision.

    req8 = plt.figure()


    # Requirement 2: The biographical data in this dataset contains information about home towns, home states, and home countries for these players. Can you find anything interesting about players who came from a similar location?

    req9 = plt.figure()



    # Requirement 3: Find something else in this dataset that you consider interesting. Produce a graph to communicate your insight.

    req10 = plt.figure()



    """##### - End of Requirements - #####"""
    
    # Save figures into document
    # save_multi_image("assign13.pdf")
    
if __name__ == "__main__":
    main()