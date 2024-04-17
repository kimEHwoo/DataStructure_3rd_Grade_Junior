# Storing High Scores for a game
# The objective is to store high score entires for a video game
# Each game entry has a name and a score. [GameEntry] Class.
# To maintain a sequence of high scores, we create another class called [Scoreboard].
# [Scoreboard] can have limited number of entries.
# A new score only qualifies for the scoreboard if it is stictly higher than the lowest of the high scores in the board.

class GameEntry:
  '''
  Represents one entry of a list of high scores
  '''

  def __init__(self, name, score):
    self._name = name
    self._score = score

  def get_name(self):
    return self._name

  def get_score(self):
    return self._score

  def __str__(self):
    return '({0}, {1})'.format(self._name, self._score)


class Scoreboard:
  '''  Fixed-length sequence of high score in nondecreasing order '''
  def __init__(self, capacity=10):
    '''
    Initialize scoreboard with given maximum capacity
    All entries are initially None
    '''
    self._board = [None]*capacity   # reserve space for future scores
    self._n = 0                     # number of actual entries

  def __getitem__(self, k):
    ''' return entry at index k'''
    return self._board[k]

  def __str__(self):
    ''' return string representation of the high score list'''
    return '\n'.join(str(self._board[j]) for j in range(self._n))

  def add(self, entry):
    ''' add new entries to high scores'''
    score = entry.get_score()

    # Does new entry qualify as a high score?
    # answer is yes if board not full or score is higher than the last entry

    good = self._n < len(self._board) or score > self._board[-1].get_score()

    if good:
      if self._n < len(self._board):    # no score drops from list
        self._n += 1                    # overall count increases

      # shift lower scores rightward to make room for new entry
      j = self._n - 1
      while j > 0 and self._board[j-1].get_score() < score:
        self._board[j] = self._board[j-1]   # shift entry from j-1 to J
        j -= 1                              # and decrement j
      self._board[j] = entry              # when done, add new entry


S = Scoreboard()
S.add(GameEntry('Mike',1105))
S.add(GameEntry('Rob',750))
S.add(GameEntry('Paul',720))
S.add(GameEntry('Anna',660))
S.add(GameEntry('Rose',590))
S.add(GameEntry('Jack',510))

print('Entries on the Scoreboard:\n', S)

S.add(GameEntry('Jill', 740))

print('Entries on the Scoreboard:\n', S)