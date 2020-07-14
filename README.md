# Zombie Dice

This package is based on Zombie Dice - a popular dice-rolling, push-your-luck boardgame by Steve Jackson.

By running a series of simple functions within a Python environment, you can push your luck to get the most BRAAAAIINS!! 🧠 as possible. At the same time you need to avoid shotgun blasts 💥 while pushing your luck whether to pursue survivors 👣

You can also analyse your results by checking out the logs of your rounds and overall game.

- STEP 1: Once initialised, players are required to pick 3 dice from the bucket by running ```pick_dice()```
- STEP 2: After they've picked the dice with specific colours, players are required to roll the dice by running ```roll_dice()```
- STEP 3: Player can pick more dice and re-roll if they choose to - remember footprints are included in the re-pick and re-throw, so keep in mind of the colours
- STEP 4: Player can keep pick and roll untill the 13 dice are exhausted and the round finished or player can end the round when they feel like they've amounted enough points. Run ```end_round()``` to end the round and the next player can continue

The first player to reach a total of 13 points wins the game!

![zombiedice_pic](https://thebigbox.co.za/wp-content/uploads/2017/08/ZombieDice2.jpg)

For a formal how-to-play guide, check out the [original website](http://www.sjgames.com/dice/zombiedice/) or [BGG here](https://boardgamegeek.com/boardgame/62871/zombie-dice).

### Initiate in terminal

```
pip install zombie-dice
```

### Play example

```
import zombie_dice

player_one = zombie_dice.Zombiedice(1)

player_one.pick_dice()

You have the following dice to roll:

Yellow
Green
Green
player_one.roll_dice()

Die 1: Yellow Brain
Die 2: Green Footprints
Die 3: Green Brain

You're score this round so far is 2!
You've rolled 1 footprint(s).
Do you wanna pick more dice to re-roll?
Remember, you can only pick three dice including one of the footprints.

player_one.roll_dice()

You have the following dice to roll:

Green
Yellow
Green

The footprints dice from the previous roll is:
Green

player_one.roll_dice()

Die 1: Green Footprints
Die 2: Yellow Footprints
Die 3: Green Shotgun

You're score this round so far is 1!
You've rolled 2 footprint(s).
Do you wanna pick more dice to re-roll?
Remember, you can only pick three dice including one of the footprints.

player_one.roll_dice()

Die 1: Red Shotgun
Die 2: Red Footprints
Die 3: Green Brain

You're score this round so far is 1!
You've rolled 1 footprint(s).
Do you wanna pick more dice to re-roll?

Remember, you can only pick three dice including one of the footprints.

player_one.end_round()

You're total score is: 1
```

Enjoy!
