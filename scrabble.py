letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P",
 "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
points = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10]

letters += [letter.lower() for letter in letters]
points *= 2
# 1. combine these two into a dictionary that would map a letter to its point value
# Using a list comprehension and zip, create a dictionary called letter_to_points that has the elements of letters as 
# the keys and the elements of points as the values.

letter_to_points = {key:value for key, value in sorted(zip(letters, points))}

# Add a 'space' with a score of zer(0) to the new list
letter_to_points[" "] = 0

# Define a function to score a word
def score_word(word):
    point_total = 0
    for letter in word:
        point_total += letter_to_points.get(letter, 0)
    return point_total

# IT WORKS - FUCKING CAPS :D :D :D :D :D 

# New Dictionary that maps multiple players and their played words
player_to_words = {"player1": ["BLUE", "TENNIS", "EXIT"], "wordNerd": ["EARTH", "EYES", "MACHINE"],
 "Lexi Con": ["ERASER", "BELLY", "HUSKY"], "PROF READER": ["ZAP", "COMA", "PERIOD"]}

# New Dictionary - Player to points
player_to_points = {}


def update_points_total():
    for player, words in player_to_words.items():
        player_points = 0
        for word in words:
            player_points += score_word(word)
        player_to_points[player] = player_points

update_points_total()
print(player_to_words)

def play_word(player, word):
    player_to_words[player].append(word)
    update_points_total()

play_word('player1', 'NISETSUMURI')
print(player_to_words)
print(player_to_points)

play_word('PROF READER', 'jurassic park')
print(player_to_words)
print(player_to_points)

