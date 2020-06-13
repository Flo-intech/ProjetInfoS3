from sports import *

class Sports:

    def sportslive():

        #Live Matched
        all_matches = sports.all_matches()
        baseball = all_matches['cricket']
        print(baseball)
        
        
        #Live Matched
        matches = sports.get_sport(sports.CRICKET)
        print(matches)
        
        #Football Live
        football = sports.get_sport(sports.FOOTBALL)
        print(football)
        
        
        #basketabbl
        
        basktetball = sports.get_sport(sports.BASKETBALL)
        print(basktetball)