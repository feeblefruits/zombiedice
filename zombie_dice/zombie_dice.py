import random

class Zombiedice:
    
    def __init__(self, player_int):
        
        '''
        To initiate player, include player int
        
        STEP 1: Once initialised, players are required to pick 3 dice from the bucket by running pick_dice()
        
        STEP 2: After they've picked the dice with specific colours,
        players are required to roll the dice by running roll_dice()
        
        STEP 3: Player can pick more dice and re-roll if they choose to
        - remember footprints are included in the re-pick and re-throw, so keep in mind of the colours
        
        STEP 4: Player can keep pick and roll untill the 13 dice are exhausted and the round finished
        or player can end the round when they feel like they've amounted enough points.
        
        Run end_round() to end the round and the next player can continue
        
        The first player to reach a total of 13 points wins the game
        
        '''
        
        self.player_int = player_int
        self.pick_results = []
        self.footprints = []
        self.total_score = []
        self.round_score = 0
        
    def pick_dice(self, show_print=True):
        
        '''
        Run to pick three dice from the bucket of 13 dice
        
        A complete bucket consists of the following colours:
        
        - 6 green dice
        - 4 yellow dice
        - 3 red dice
        
        INPUT: optional show_print boolean to include helper text output
        OUTPUT: three dice colours picked at random
        
        '''
                
        picked_results_show = []
        footprint_results_show = []

        # define the remaining_dice in bucket to pick from (excluding the ones you've already picked)
        remaining_dice = range(1, 14)
        remaining_dice = [x for x in remaining_dice if x not in self.pick_results]

        try:
            # pick three dice minus the number of footprints dice
            for dice_pick in range(0, (3 - len(self.footprints))):

                dice_pick = random.choice(remaining_dice)

                if dice_pick in [1, 2, 3, 4, 5, 6]:
                    result = dice_pick
                    result_show = 'Green'

                elif dice_pick in [7, 8, 9, 10]:
                    result = dice_pick
                    result_show = 'Yellow'

                elif dice_pick in [11, 12, 13]:
                    result = dice_pick
                    result_show = 'Red'

                self.pick_results.append(result)

                picked_results_show.append(result_show)
                
        except IndexError:
            print('There are no more dice left in the bucket')
            picked_results_show = []
            
        # include footprints dice with pick_results
        for die in self.footprints:
            self.pick_results.append(die)

        # if there are footprints dice then append colour and include in picked_results_show
        if len(self.footprints) > 0:

            for footprint_die in self.footprints:
                if footprint_die in [1, 2, 3, 4, 5, 6]:
                    footprint_result_show = 'Green'

                elif footprint_die in [7, 8, 9, 10]:
                    footprint_result_show = 'Yellow'

                elif footprint_die in [11, 12, 13]:
                    footprint_result_show = 'Red'

                footprint_results_show.append(footprint_result_show)

            # include footprints dice with picked_results_show
            picked_results_show = picked_results_show + footprint_results_show

        else:
            pass
        
        if show_print is True:
            print("You have the following dice to roll:")
            print('')
            for die in picked_results_show[-3:]:
                print(die)
            print('')

            if len(self.footprints) > 0:
                print("The footprints dice from the previous roll is:")
                for die in footprint_results_show:
                    print(die)
            else:
                pass
        else:
            pass
            
    def roll_dice(self, show_print=True):
        
        '''
        Run to roll the three dice picked up with pick_dice()
        
        Die icons include:
        
        - Brains
        - Shotgun
        - Footprints
        
        INPUT: optional show_print boolean to include helper text output
        OUTPUT: The colour and 'icon' of each rolled die
        
        '''        
        
        roll_results_dict = {}
        
        die_number = 0
        
        footprints = []
                
        # roll last three dice of picked dice
        for die in self.pick_results[-3:]:
            
            die_number += 1
            
            if die in [1, 2, 3, 4, 5, 6]:
                
                die_roll = random.randint(1, 6)
                
                roll_result_colour = 'Green'

                if die_roll in [1, 2, 3]:
                    roll_result = 'Brain'
                    self.round_score += 1
                    
                elif die_roll in [4, 5]:
                    roll_result = 'Footprints'
                    footprints.append(die)
                    
                elif die_roll in [6]:
                    roll_result = 'Shotgun'
                    self.round_score -= 1
                                        
                roll_results_dict.update({'Die ' + str(die_number) + ': Green' : roll_result})
                    
            elif die in [7, 8, 9, 10]:
                
                die_roll = random.randint(1, 6)

                roll_result_colour = 'Yellow'

                if die_roll in [1, 2]:
                    roll_result = 'Brain'
                    self.round_score += 1

                elif die_roll in [3, 4]:
                    roll_result = 'Footprints'
                    footprints.append(die)
                    
                elif die_roll in [5, 6]:
                    roll_result = 'Shotgun'
                    self.round_score -= 1
                                    
                roll_results_dict.update({'Die ' + str(die_number) + ': Yellow' : roll_result})
                    
            elif die in [11, 12, 13]:
                
                die_roll = random.randint(1, 6)

                roll_result_colour = 'Red'

                if die_roll in [1]:
                    roll_result = 'Brain'
                    self.round_score += 1
                    
                elif die_roll in [2, 3]:
                    roll_result = 'Footprints'
                    footprints.append(die)

                elif die_roll in [4, 5, 6]:
                    roll_result = 'Shotgun'
                    self.round_score -= 1
                
                roll_results_dict.update({'Die ' + str(die_number) + ': Red' : roll_result})
        
        # only remaining footprints after roll_dice should be included in next pick_dice
        self.footprints = footprints
                
        for key, value in roll_results_dict.items():
            print(key, value)
            
        if show_print is True:
            print('')
            print("You're score this round so far is " + str(self.round_score) + "!")

            if len(self.footprints) > 0:
                print("You've rolled " + str(len(self.footprints)) + " footprint(s).")
                print("Do you wanna pick more dice to re-roll?")
                print('')
                print("Remember, you can only pick three dice including one of the footprints.")
            else:
                pass
        else:
            pass
                  
    def end_round(self):
        
        '''
        Run end_round() to end the round and the next player can continue
        
        INPUT: None
        OUTPUT: player's total score - a sum of all rounds played so far
        
        '''
        
        # tally round score
        self.total_score.append(self.round_score)
        
        # reset all round variables
        self.pick_results = []
        self.footprints = []
        self.round_score = 0
        
        print("You're total score currently is: " + str(sum(self.total_score)))