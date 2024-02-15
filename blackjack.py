import random

# Function to initialize a deck of cards
def initialize_deck():
    # Define ranks, suits, and their corresponding values
    ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
    values = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 10, 'Q': 10, 'K': 10, 'A': 11}
    
    # Create the deck by combining ranks, suits, and values
    deck = [{'rank': rank, 'suit': suit, 'value': values[rank]} for rank in ranks for suit in suits]
    
    # Shuffle the deck
    random.shuffle(deck)
    
    return deck

# Function to deal a card from the deck
def deal_card(deck):
    return deck.pop()

# Function to calculate the total value of a hand
def calculate_hand_value(hand):
    total_value = sum(card['value'] for card in hand)
    
    # Adjust for Aces if the total value exceeds 21
    for card in hand:
        if card['rank'] == 'A' and total_value > 21:
            total_value -= 10
    
    return total_value

# Function to display a player's hand
def display_hand(player, hand):
    print(f"{player}'s Hand:")
    for card in hand:
        print(f"{card['rank']} of {card['suit']}")
    print(f"Total Value: {calculate_hand_value(hand)}")

# Function to check if a player has busted (exceeded 21)
def is_bust(hand):
    return calculate_hand_value(hand) > 21

# Function to determine the winner
def determine_winner(player_hand, dealer_hand):
    player_value = calculate_hand_value(player_hand)
    dealer_value = calculate_hand_value(dealer_hand)
    
    if is_bust(player_hand):
        return "Dealer"
    elif is_bust(dealer_hand):
        return "Player"
    elif player_value > dealer_value:
        return "Player"
    elif player_value < dealer_value:
        return "Dealer"
    else:
        return "Tie"

# Function to play the game
def play_game():
    while True:
        # Initialize deck and hands
        deck = initialize_deck()
        player_hand = [deal_card(deck), deal_card(deck)]
        dealer_hand = [deal_card(deck), deal_card(deck)]
        
        # Display initial hands
        display_hand("Player", player_hand)
        display_hand("Dealer", [dealer_hand[0]])
        
        # Player's turn
        while input("Do you want to hit? (y/n): ").lower() == 'y':
            player_hand.append(deal_card(deck))
            display_hand("Player", player_hand)
            
            if is_bust(player_hand):
                print("Player busts! Dealer wins.")
                break
        
        # Dealer's turn
        while calculate_hand_value(dealer_hand) < 17:
            dealer_hand.append(deal_card(deck))
            display_hand("Dealer", dealer_hand)
            
            if is_bust(dealer_hand):
                print("Dealer busts! Player wins.")
                break
        
        # Determine the winner
        winner = determine_winner(player_hand, dealer_hand)
        print(f"The winner is: {winner}")
        
        # Ask if the player wants to play again
        play_again = input("Do you want to play again? (y/n): ").lower()
        if play_again != 'y':
            break

# Main function to start the game
def main():
    play_game()

if __name__ == "__main__":
    main()
