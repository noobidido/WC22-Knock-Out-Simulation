# WC22 Knock-Out Simulation

The FIFA world cup is considered the greatest show on earth by many. And rightly so. No other event brings these much people closer, people of different gender, race, religion, people from every corner of the world. The emotion behind this event is simply unmatched. For a month almost every person in this world is following the world cup.

For the very first time, this year the FIFA world cup is being held in Qatar. The group stage of the tournament is already completed and it was probably the most competitive and uncertain of all the world cups in the recent times. Many footballing giants were knocked out of the tournament and many not-so-big teams in the traditional sense qualified for the RO16. 

This world cup features a lot of great teams, who are very likely to win the World Cup. And also a lot of teams capable of pulling some upsets and writing everyone's favorite world cup fairy tales. In a world cup like this, it is almost impossible to make any predictions. But it is not stopping regular football fans and new football fans alike. Everyone is making their predictions. Some with their pure emotion about a team, some with their intuition and understanding of the game, and others with their complex mathematical models.

I will also try to make a prediction. Actually not a prediction, but I would like to know if there is no major upset and everyone plays to their strength, which team has the best chance to win the tournament. I will not be using any complex models, not as much for my disincination towards unnecessarily complex models but for my lack of experience. Nevertheless, I will be using a very simple simulation model that anyone with a bit of python-knowledge can understand. 

The actual simulation is based on [Lab6 of Harvard's CS50](https://cs50.harvard.edu/x/2022/labs/6/). It is the sole back-bone of the simulation program(tournament.py), and we will be adding other utilities on top of that to make our quest better.

## How the Simulation Works
In any football game there are two teams. Either both of them are of equal strength, any one of them can win, or one is better and stronger than the other. In that case the strong team will likely win. There is no gurantee of something happening in this reasoning. In any single meeting any one of them can win. But given enough matches, the stronger team will come out ahead. This way we can see who has the best chance of winning the tournament.

Now how do we know which team is stronger and which team is relatively weaker? A valid matric is the FIFA rating of these countries. The higher the FIFA rating, the higher the chance of that team winning. 

In fact we use the following formula to calculate the expected win of $1^{st}$ team over the $2^{nd}$ team:

# $$\frac{1}{1 + 10^\{R_{2} - R_{1}}}$$


Now, that we have a better understanding of how to make the simulation, let's start working by

### Collecting Rating points
This project was done in a night. So the code is probably not written in the best of ways. Also, I did not make the code super reusable. Instead of taking a list of World Cup winning teams and their ratings from a website, I hard coded their name and rating points in a text file. I went through all the 32 teams across 8 groups to get their FIFA ratings. I figured it'll be easier and faster than automating the process for a single use. 

### Updating Ratings after Group Stage
