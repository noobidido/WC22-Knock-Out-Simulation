# WC22 Knock-Out Simulation

The FIFA world cup is considered the greatest show on earth by many. And rightly so. No other event brings these much people closer, people of different gender, race, religion, people from every corner of the world. The emotion behind this event is simply unmatched. For a month almost every person in this world is following the world cup.

For the very first time, this year the FIFA world cup is being held in Qatar. The group stage of the tournament is already completed and it was probably the most competitive and uncertain of all the world cups in the recent times. Many footballing giants were knocked out of the tournament and many not-so-big teams in the traditional sense qualified for the RO16. 

This world cup features a lot of great teams, who are very likely to win the World Cup. And also a lot of teams capable of pulling some upsets and writing everyone's favorite world cup fairy tales. In a world cup like this, it is almost impossible to make any predictions. But it is not stopping regular football fans and new football fans alike. Everyone is making their predictions. Some with their pure emotion about a team, some with their intuition and understanding of the game, and others with their complex mathematical models.

I will also try to make a prediction. Actually not a prediction, but I would like to know if there is no major upset and everyone plays to their strength, which team has the best chance to win the tournament. I will not be using any complex models, not as much for my disincination towards unnecessarily complex models but for my lack of experience. Nevertheless, I will be using a very simple simulation model that anyone with a bit of python-knowledge can understand. 

The actual simulation is based on [Lab6 of Harvard's CS50](https://cs50.harvard.edu/x/2022/labs/6/). It is the sole back-bone of the simulation program(tournament.py), and we will be adding other utilities on top of that to make our quest better.

## How the simulation works
In any football game there are two teams. Either both of them are of equal strength, any one of them can win, or one is better and stronger than the other. In that case the strong team will likely win. There is no gurantee of something happening in this reasoning. In any single meeting any one of them can win. But given enough matches, the stronger team will come out ahead. This way we can see who has the best chance of winning the tournament.
