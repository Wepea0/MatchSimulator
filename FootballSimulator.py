'''This is a football game simulator that calculates the score of a game and assigns it as a win, draw or loss to the two participating
teams. This is done by using the probability that a team scores a certain number of goals. Currently the model works with the probability
of 1, 2 or 3 goals. The program uses three classes, the team class which stores info about each team, the SimOneGame class which
simulates one game and the MatchReport class which collates and returns the results. Extra information about each class(the various
attributes and methods) are included below'''


# Class Team - name, prob1, score, win, loss, draw - [incscore, incwin, incloss, incdraw]
# Class SimGame - team1, team2 - [play, getwinner]
# Class MatchReport - init(team1, team2, results = {}, record = []) - [update, printresults]


from random import random
from tabulate import tabulate

class Team:
    def __init__(self, name, prob1, prob2, prob3):
        self.name = name
        self.prob1 = prob1
        self.prob2 = prob2
        self.prob3 = prob3
        self.score = 0
        self.wins = 0
        self.losses = 0
        self.draws = 0
    
    def IncScore(self, goals):
        self.score += goals
    
    def IncWins(self):
        self.wins += 1
    
    def IncLosses(self):
        self.losses += 1
    
    def IncDraws(self):
        self.draws += 1
    
    def __str__(self): 
        return f"This team is called {self.name} and has a probability of {self.prob1} of scoring one goal in a game, {self.prob2} of scoring two goals in a game and {self.prob3} of scoring 3 goals in a game. {self.name} has won {self.wins} games, lost {self.losses} games and drawn {self.draws} games."
    
    def ClearScore(self):
        self.score = 0


class SimOneGame:
    def __init__(self, TeamA, TeamB):
        self.TeamA = TeamA
        self.TeamB = TeamB
        
    def Play(self):
        game_prob = random()
        if game_prob < self.TeamA.prob3:
            self.TeamA.IncScore(3)
        elif game_prob < self.TeamA.prob2:
            self.TeamA.IncScore(2)
        elif game_prob < self.TeamA.prob1:
            self.TeamA.IncScore(1)
        if game_prob < self.TeamB.prob3:
            self.TeamB.IncScore(3)
        elif game_prob < self.TeamB.prob2:
            self.TeamB.IncScore(2)
        elif game_prob < self.TeamB.prob1:
            self.TeamB.IncScore(1)

        
    def GetWinner(self):
        if self.TeamA.score > self.TeamB.score:
            self.TeamA.IncWins()
            self.TeamB.IncLosses()
            
        elif self.TeamB.score > self.TeamA.score:
            self.TeamB.IncWins()
            self.TeamA.IncLosses()
            
        else:
            self.TeamA.IncDraws()
            self.TeamB.IncDraws()
            
        return self.TeamA, self.TeamB
    

class MatchReport:
    def __init__(self, TeamI, TeamII):
        self.TeamI = TeamI
        self.TeamII = TeamII
        self.results = {}
        self.record = []
        
    def Update(self):
        TeamI_name = str(self.TeamI.name)
        TeamII_name = str(self.TeamII.name)
        TeamI_score = str(self.TeamI.score)
        TeamII_score = str(self.TeamII.score)
        
        matchup = TeamI_name + " vs " + TeamII_name
        final_score = "Final Score " + TeamI_score + " - " + TeamII_score
        full_time = matchup + " " +  final_score
        
        self.results[matchup] = final_score
        for team in [self.TeamI, self.TeamII]:
            self.record.append([team.name, team.wins, team.draws, team.losses])
        
        #This clears both teams' scores so the next game's score does not get added to that of the previous game
        self.TeamI.ClearScore()
        self.TeamII.ClearScore()
        
        return full_time
            
    def PrintResults(self):
        header_list = ["Team", "Wins", "Draws", "Losses"]
        print(tabulate(self.record, header_list))
        
    

def get_input():
    print("Welcome to the football match simulator! You can simulate a match based on the probability each team has of scoring a certain"
    " number of goals. Kindly use probabilities between 0 and 1. \n\nClick Enter to continue")
    
    try:
        Team1 = input("Enter the name of the first team >> ")
        Team1prob1 = float(input(f"Enter {Team1}'s probability of scoring one goal in a game >> "))
        Team1prob2 = float(input(f"Enter {Team1}'s probability of scoring two goals in a game >> "))
        Team1prob3 = float(input(f"Enter {Team1}'s probability of scoring three goals in a game >> "))
        Team2 = input("Enter the name of the second team >> ")
        Team2prob1 = float(input(f"Enter {Team2}'s probability of scoring one goal in a game >> "))
        Team2prob2 = float(input(f"Enter {Team2}'s probability of scoring two goals in a game >> "))
        Team2prob3 = float(input(f"Enter {Team2}'s probability of scoring three goals in a game >> "))
        No_games = int(input("How many games would you like to simulate >> "))
    except:
        print("Please enter a valid input")
        get_input()
    
    return Team1, Team1prob1, Team1prob2, Team1prob3, Team2, Team2prob1, Team2prob2, Team2prob3, No_games
        

        
def SimulateMatch():
    Team1, Team1prob1, Team1prob2, Team1prob3, Team2, Team2prob1, Team2prob2, Team2prob3, No_games =  get_input()
    Team1 = Team(Team1, Team1prob1, Team1prob2, Team1prob3)
    Team2 = Team(Team2, Team2prob1, Team2prob2, Team2prob3)
    Game1 = SimOneGame(Team1, Team2)
    list1 = []
    for game in range(No_games):
        Game1.Play()
        Game1.GetWinner()
        Game1_Report = MatchReport(Team1, Team2)
        scores = Game1_Report.Update()
        list1.append(scores)
    Game1_Report.PrintResults()
    for result in list1:
        print(result)
    

if __name__ == "__main__":
    SimulateMatch()
    



            
            
