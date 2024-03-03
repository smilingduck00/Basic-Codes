def convert_to_octal(number):
    return oct(number)[2:]

def compare_digits(player1_octal, player2_octal):
    score_player1 = 0
    score_player2 = 0
    
    # Adding leading zeros if necessary to make the lengths equal
    max_length = max(len(player1_octal), len(player2_octal))
    player1_octal = player1_octal.zfill(max_length)
    player2_octal = player2_octal.zfill(max_length)
    print("Player 1 octal: ", player1_octal)
    print("Player 2 octal: ", player2_octal)

    for digit1, digit2 in zip(player1_octal, player2_octal):
        if digit1 > digit2:
            score_player1 += 1
        elif digit2 > digit1:
            score_player2 += 1
    
    return score_player1, score_player2

# Input for player 1
player1_number = 123

# Input for player 2
player2_number = int(input("Enter the number for player 2: "))

# Conversion to octal
player1_octal = convert_to_octal(player1_number)
# print("Player 1 octal: ", player1_octal)
player2_octal = convert_to_octal(player2_number)
# print("Player 1 octal: ", player1_octal)


# Comparing digits
player1_score, player2_score = compare_digits(player1_octal, player2_octal)

# Displaying scores
print(f"Player 1 score: {player1_score}")
print(f"Player 2 score: {player2_score}")
