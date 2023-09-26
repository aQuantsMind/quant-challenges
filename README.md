# quant_challenges
------------------
------------------

I. drawing_cards_optimally.py
-----------------------------
The Challenge. Imagine you have a deck of 52 cards, 26 of them are black, the other 26 are red. 
The game involves drawing cards. If you draw a black card, you gain 1$; if you draw a red card, you loose 1$.
You can draw as many cards as you want to from this deck. At the same time, you can also stopp at each point and decide not to draw another card; in this case you take home the gains/losses you've accumulated thusfar.

The Objective. What is the expected payoff from this game if we play the game optimally?

Note... that at the beginning of the game (when we have the whole deck of 52 cards in front of us), we have equal chances of drawing a black card (making a gain of 1$) or drawing a red card (making a loss of 1$)
Also note that if we draw all 52 cards, we end up with a payoff of 0 with certainty.

Trading strategy.
Rough logic behind gaming strategy. If we draw a black card, we gain 1$, but at the same time our chances of drawing another black card are smaller in the next round. (The problem is therefor recursive in nature.)
Accordingly, we need to decide in each node when to walk away with our accumulated returns, and when to keep playing. One can approximate the latter with the expected return we would get in each node.

Model and code.
the expected value is given in each node by the max(accumulated return, expected return). If accumulated return > expected return, we stopp drawing cards.
