class Game:
    def __init__(self, title):
            self.title = title
        
    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, title):
        if hasattr(self, "_title"):
            raise Exception("Alredy has a title attribute")
        if isinstance(title, str) and len(title) > 0:
            self._title = title
        else:
            raise Exception("Title must be a non-empty string.")

    def results(self):
        self._results = []
        for result in Result.all:
            if result.game == self:
                self._results.append(result)
        return self._results

    def players(self):
        self._players = []
        for result in Result.all:
            if result.game == self:
                self._players.append(result.player)
        return list(set(self._players))

    def average_score(self, player):
        score = []
        for result in Result.all:
            if result.player == player and result.game == self:
                score.append(result.score)
        return sum(score)/len(score)


class Player:
    def __init__(self, username):
        self.username = username

    @property
    def username(self):
        return self._username
    
    @username.setter
    def username(self, username):
        if isinstance(username,str) and 2 <= len(username) <= 16:
            self._username = username
        else:
            raise Exception("Username should be a string between 2 and 16 characters, inclusive.")

    def results(self):
        self._results = []
        for result in Result.all:
            if result.player == self:
                self._results.append(result)
        return self._results

    def games_played(self):
        self._games_played = []
        for result in Result.all:
            if result.player == self:
                self._games_played.append(result.game)
        return list(set(self._games_played))
    
    def played_game(self, game):
        for result in Result.all:
            if result.game == game and result.player == self:
                return True
        return False

    def num_times_played(self, game):
        count = 0
        for result in Result.all:
            if result.game == game and result.player == self:
                count += 1
        return count 

class Result:

    all = []

    def __init__(self, player, game, score):
        self.player = player
        self.game = game
        self.score = score
        Result.all.append(self)

    @property
    def score(self):
        return self._score
    
    @score.setter
    def score(self, score):
        if not hasattr(self, "_score") and isinstance(score, int) and 1 <= score <= 5000:
            self._score = score

        
    @property
    def player(self):
        return self._player 
    
    @player.setter
    def player(self, player):
        if isinstance(player, Player):
            self._player = player
        else:
            raise Exception("Player must be of type Player.")
        
    @property
    def game(self):
        return self._game
    
    @game.setter
    def game(self, game):
        if isinstance(game, Game):
            self._game = game
        else:
            raise Exception("Game must be of type Game.")