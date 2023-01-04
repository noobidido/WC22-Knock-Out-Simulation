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


Now, that we have a better understanding of how to make the simulation, let's start working by:

### Collecting Rating points
This project was done in a night. So the code is probably not written in the best of ways. Also, I did not make the code super reusable. Instead of taking a list of World Cup winning teams and their ratings from a website, I hard coded their name and rating points in a text file. Then I imported these data in my program from that file. I went through all the 32 teams across 8 groups to get their FIFA ratings. I figured it'll be easier and faster than automating the process for a single use. So, if I ever want to use the program again for other tournaments, I'll have to retrieve data manually again.

### Updating Ratings after Group Stage
FIFA publishes a rating before the world cup. And another one after the world cup. If we are to take the FIFA's rating for the knock-out stage, it does not consider the group-stage performance of the qualified teams. So, if a country played really well in the group-stage, or were horrible in the group-stage, it will not affect their performance in the simulation. Which is not true in the real world. 
Also, this year's World Cup was one of the most thrilling tournament in the recent history. There was a lot of 'upsets' in the group stage. That's why I felt that teams that advanced from the group-stage should get a new rating before the knock-out. My reasoning behind this was to better capture the moral of these teams. As any team that beat a relatively strong team will be high on confidence and any team that lost to a relatively weak team will be down.
That's why I updated the rating of these teams according to their group-stage matches. After every match, both teams' rating would update and after all three matches they will get a final rating. One thing that's worth mentioning is that, I only used the group-stage matches to update their rating and did not take into account the FIFA friendlies and warm-up matches. 
So, did it had any effect? Well, here's how teams' rating changed after the group-stage:
![download (1)](https://user-images.githubusercontent.com/72381684/210505352-86cb700a-a435-46cb-97dd-f69c9a7aa0dd.png)
Both Brazil and Spain lost rating because of their lose against Cameroon and Japan respectively. While Morocco had the biggest leap with their win against Belgium and Canada and a draw against Croatia. 

