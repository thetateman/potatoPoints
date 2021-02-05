# PotatoPoints
Potato Points is a card game I invented a few years ago, and decided to make into a computer game to get some experience using Python.

### Rules
Potato Points can be played with 2-4 players. The game is played a deck of forty cards, made by removing the face cards from a standard 52-card deck,
leaving the cards 2-10 and aces. The objective of the game is to accumulate points by winning tricks. At the beginning of a round a dealer
deals each player 2 distinct sets of 5 cards - one set face up, visible to all players (this set of cards is called a player's "field"),
and one set face down (called a player's hand). The player with the high card in their field starts the first trick by playing a card from either their
hand or their field. Play then moves clockwise with each player playing a card from their hand or field. Players do not have to follow suit, but they must
play a card of the same **color** as the card that led the trick, if they are able. After everyone has played a card the player who played the 
highest card **of the same color as the leading card** wins the trick. The order of the cards being, from highest to lowest: Ace, 10, 9, ... 2. The winning player takes
the cards of the trick and sets them aside to tally at the end of the game. A new trick begins with the winner of the last trick playing first. Thus the game continues 
until all players have played every card in their hands and fields. Then the points are tallyed in the following manner. The Ace and odd numbered cards
are worth zero points, all other cards are worth the the same number of points as the value of the card (so a 2 is worth 2 points, an 8 is worth 8 points).
The player with the highest number of points wins the round.

### Computer Game
The Python code in this repository allows four players to play Potato points by interacting through the terminal. Cards are generated and dealt to each player,
and players can type the card they want to play into the terminal. The program will determine the winner of each trick and add the appropriate number of points
to the winner's total, then at the end of the game, the program will display the scores of all players.
