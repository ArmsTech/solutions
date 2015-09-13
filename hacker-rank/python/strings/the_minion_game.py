# The Minion Game Challenge
"""
Rules
The game is a two player game. Players are given a string S.
Both the players have to make words using the letters of string S.
Player 1 has to make words starting with consonants.
Player 2 has to make words starting with vowels.
Game ends when both players have made all possible substrings.

Scoring
Player get +1 Point for each occurence of the word in the string S.
Example:
If string S = BANANA
Word made by Player 2 = ANA
'ANA' is occuring twice in 'BANANA'. Hence, Player 2 will get 2 Points.
"""

PLAYER1 = 'Stuart'
PLAYER2 = 'Kevin'
VOWELS = ('A', 'E', 'I', 'O', 'U')

player1_points = 0
player2_points = 0
word = raw_input().upper()

for index, character in enumerate(word):
    points = len(word) - index
    if character in VOWELS:
        player2_points += points
    else:
        player1_points += points

if player1_points > player2_points:
    print ' '.join([PLAYER1, str(player1_points)])
elif player1_points < player2_points:
    print ' '.join([PLAYER2, str(player2_points)])
else:
    print 'Draw'
