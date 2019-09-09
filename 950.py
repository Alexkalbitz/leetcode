# In a deck of cards, every card has a unique integer.  You can order the deck in any order you want.
#
# Initially, all the cards start face down (unrevealed) in one deck.
#
# Now, you do the following steps repeatedly, until all cards are revealed:
#
#     Take the top card of the deck, reveal it, and take it out of the deck.
#     If there are still cards in the deck, put the next top card of the deck at the bottom of the deck.
#     If there are still unrevealed cards, go back to step 1.  Otherwise, stop.
#
# Return an ordering of the deck that would reveal the cards in increasing order.
#
# The first entry in the answer is considered to be the top of the deck.
#
# Input: [17,13,11,2,3,5,7]
# Output: [2,13,3,11,5,17,7]
# Explanation:
# We get the deck in the order [17,13,11,2,3,5,7] (this order doesn't matter), and reorder it.
# After reordering, the deck starts as [2,13,3,11,5,17,7], where 2 is the top of the deck.
# We reveal 2, and move 13 to the bottom.  The deck is now [3,11,5,17,7,13].
# We reveal 3, and move 11 to the bottom.  The deck is now [5,17,7,13,11].
# We reveal 5, and move 17 to the bottom.  The deck is now [7,13,11,17].
# We reveal 7, and move 13 to the bottom.  The deck is now [11,17,13].
# We reveal 11, and move 17 to the bottom.  The deck is now [13,17].
# We reveal 13, and move 17 to the bottom.  The deck is now [17].
# We reveal 17.
# Since all the cards revealed are in increasing order, the answer is correct.

class Solution:
    def deckRevealedIncreasing(self, deck):
        deck.sort()
        indexes = [n for n in range(len(deck))]
        indexes = self.apply(indexes)
        return self.transform(deck, indexes)

    def transform(self, deck, indexes):
        t = list.copy(deck)
        counter = 0
        for i in indexes:
            t[i] = deck[counter]
            counter += 1
        return t

    def apply(self, i):
        new = []
        while i:
            new.append(i.pop(0))
            if len(i) < 1:
                break
            i.append(i.pop(0))
        return new


test1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15] 
      # [1, 12, 2, 9, 3, 14, 4, 10, 5, 13, 6, 11, 7, 15, 8]
test2 = [1, 2, 3, 4, 5, 6] 
      # [1, 4, 2, 6, 3, 5]
test3 = [17, 13, 11, 2, 3, 5, 7] 
      # [2, 13, 3, 11, 5, 17, 7]

s = Solution()
print(s.deckRevealedIncreasing(test1))
print(s.deckRevealedIncreasing(test2))
print(s.deckRevealedIncreasing(test3))

