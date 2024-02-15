Simple Blackjack Game
Description

This is a text-based implementation of the classic casino game Blackjack (also known as 21). The game allows a single player to play against the computer dealer. The objective is to obtain cards whose total value comes closest to 21 without exceeding it. Face cards (Jack, Queen, King) are worth 10 points, Aces can be worth either 1 or 11 points, and the remaining cards are worth their face value.
Features

    Player can hit or stand during their turn.
    Dealer plays according to predefined rules (hits until hand value is at least 17).
    Game declares winner based on standard Blackjack rules.
    Option to restart the game after each round.
    Simple and intuitive user interface.

Getting Started
Prerequisites

    Python 3.x installed on your machine.

Installation

    Clone this repository to your local machine or download the ZIP file.
    Navigate to the directory containing the downloaded files.

Usage

    Open a terminal or command prompt.
    Navigate to the directory containing the game files.
    Run the following command:

bash

python blackjack.py

    Follow the on-screen instructions to play the game.

Game Rules

    The game is played with a standard deck of 52 playing cards.
    The player and the dealer are initially dealt two cards each.
    The player's cards are dealt face up, while only one of the dealer's cards is visible.
    The player can choose to hit (take another card) or stand (keep current hand) during their turn.
    If the player's hand value exceeds 21 points, they bust and lose the game.
    After the player's turn, the dealer reveals their hidden card and continues to hit until their hand value is at least 17.
    If the dealer's hand value exceeds 21 points, they bust and the player wins.
    If neither the player nor the dealer busts, the hand with a total value closest to 21 wins.
    In case of a tie, the game is declared a draw.
