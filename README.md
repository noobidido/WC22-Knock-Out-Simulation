# WC22 Knock-Out Simulation

The FIFA world cup is considered the greatest show on earth by many. And rightly so. No other event brings these many people closer, people of different gender, race, religion, and people from every corner of the world. The emotion behind this event is simply unmatched. For a month, almost every person in this world follows the world cup.

For the first time this year, the FIFA world cup is being held in Qatar. The tournament's group stage is already completed, and it was probably the most competitive and uncertain of all the world cups in recent times. Many footballing giants were knocked out of the tournament, and many not-so-big teams in the traditional sense qualified for the RO16. 

This world cup features many great teams who are very likely to win the World Cup. And also many teams capable of pulling some upsets and writing everyone's favorite world cup fairy tales. It is almost impossible to make predictions in a world cup like this. But it is not stopping regular football fans and new football fans alike. Everyone is making their predictions. Some with their pure emotion about a team, some with their intuition and understanding of the game, and others with their complex mathematical models.

I will also make a prediction. Actually, not a prediction, but I would like to know if there is no major upset and everyone plays to their strength, which team has the best chance to win the tournament. I will not be using any complex models, not as much for my disinclination towards unnecessarily complex models but for my lack of expertise. Nevertheless, I will use a simple simulation model that anyone with a bit of python-knowledge can understand. 

The actual simulation is based on [Lab6 of Harvard's CS50](https://cs50.harvard.edu/x/2022/labs/6/). It is the sole backbone of the simulation program(tournament.py), and we will add other utilities to improve our quest.


## How the Simulation Works
In any football game, there are two teams. Either both of them are of equal strength, any one of them can win, or one is better and stronger than the other. In that case, the strong team will likely win. There is no guarantee of something happening in this reasoning. In any single meeting, any one of them can win. But given enough matches, the stronger team will come out ahead. This way, we can see who has the best chance of winning the tournament.

How do we know which team is stronger and which is relatively weaker? A valid metric is the FIFA rating of these countries. The higher the FIFA rating, the higher the team's chance to win. 

In fact, we use the following formula to calculate the expected win of $1^{st}$ team over the $2^{nd}$ team:

# $$\frac{1}{1 + 10^\{R_{2} - R_{1}}}$$


Now that we have a better understanding of how to make the simulation, let's start working by:

### Collecting Rating points
This project was done in a night. So the code is probably not written in the best of ways. Also, I could have made the code more reusable. Instead of taking a list of teams qualified for the World Cup and their ratings from a website, I hard-coded their name and rating points in a text file. Then I imported these data into my program from that file. I went through all 32 teams across eight groups to get their FIFA ratings. I figured it'd be easier and faster than automating the whole process for one-time use. So, if I ever want to use the program again for other tournaments, I'll have to retrieve data manually again.

### Updating Ratings after Group Stage
FIFA publishes a rating before the world cup. And another one after the world cup. If we are to take FIFA's rating for the knock-out stage, it does not consider the group-stage performance of the qualified teams. So, if a country played really well in the group stage or was horrible in the group stage, it will not affect their performance in the simulation, which does not happen in the real world.

Also, this year's World Cup was one of the most thrilling tournaments in recent history. There were a lot of 'upsets' in the group stage. That's why I felt teams that advanced from the group stage should get a new rating before the knock-out. My reasoning behind this was to capture the morale of these teams better. Any team that beats a relatively strong team will be high on confidence, and any team that loses to a relatively weak team will be down.

That's why I updated the rating of these teams according to their group-stage matches. After every match, both teams' ratings would update, and after all three matches, they will get a final rating. One thing that's worth mentioning is that I only used the group-stage matches to update their rating and did not take into account the FIFA friendlies and warm-up matches to avoid unnecessary complexities.

Just before the Russia World Cup, FIFA switched to a new rating system. According to [wikipedia](https://en.wikipedia.org/wiki/FIFA_Men%27s_World_Ranking), they now use the following rules to calculate the rating after every game.


![FIFA Rating Rules](https://user-images.githubusercontent.com/72381684/210513257-5541d33c-a112-4633-a413-ac0a413c4d75.png)


Keeping these in mind, we can simplify our equation as:

### $$Rating_{new} = Rating_{old} + 50 \times G \times (W - W_{e})$$


So, did all these troubles have any effect? Well, here's how teams' ratings changed after the group stage:


![Rating Change after the Group-Stage](https://user-images.githubusercontent.com/72381684/210505352-86cb700a-a435-46cb-97dd-f69c9a7aa0dd.png)


Both Brazil and Spain lost ratings because of their loss against Cameroon and Japan, respectively. At the same time, Morocco had the biggest leap with their win against Belgium and Canada and a draw against Croatia.  



Now we have everything to run our simulation.

We input the bracket for the knockout and set N = 14000605, the number of runs. In every run, we keep track of the winner of the tournament. And eventually, we get a likelihood of each team winning the world cup. Here's what we got:

![Winning %](https://user-images.githubusercontent.com/72381684/210518677-5efd0493-9ea5-4a69-bf05-3cec7e04b743.png)


# Comments about the world cup and the simulation
We already know the result of the 2022 Qatar World Cup. Argentina, after 36 long years, finally won the world cup. This campaign has already taken its place in the footballing fairy-tale. Arguably the Greatest Of All Time, winning the Greatest Achievement in Football. 
According to our simulation, Argentina was 2nd-most likely to win the World Cup, only behind Brazil, who unfortunately got knocked out in a penalty shootout from the Quarterfinals.  

![image](https://user-images.githubusercontent.com/72381684/210535655-d2b04114-d0ef-4a74-8f17-1cb6f4988b30.png)


# Final thoughts
7 of the 8 top teams in our simulation qualified for the quarterfinals, with Morocco being the exception, who was the Dark Horse of this tournament. But as my simulation only kept track of tournament wins, we can not determine how accurately the simulation predicted other teams' elimination in different stages.

Also, it was a basic simulation. It simply assumed that a team with higher-ranking has a better chance of winning. This is true, but it is not the only factor. There are so many other aspects of the game that this game simulator needs to consider. A better game simulator that considers more factors would probably have also made the tournament simulator better. We could have used some statistical distributions and considered different variables like the team's football style, attacking play, defensive strategy, squad, coaching staff, you name it. But whatever we do, it will be impossible to predict the result with certainty. Even after considering 100 variables, there will always be some intangible factors for a team's success. We can only make our best guesses. And this is what makes the game so beautiful. 
