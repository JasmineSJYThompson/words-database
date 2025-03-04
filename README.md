The purpose of this is to create a set of functions which takes the text of a book and extracts
1. The main character's first name
2. The names of the top characters in the book
3. Any unique sets of names that are specific to the book

This has been achieved currently here for
- Do Androids Dream of Electric Sheep (Blade Runner book) by Phillip K. Dick
- Brave New World by Aldous Huxley
- Alice's Adventures in Wonderland (Alice in Wonderland) by Lewis Carroll

The main character's first name:
- Rick
- The (The Savage)
- Alice

The names of the top characters in the book (ordered by importance, using a cut off of over 30 mentions):
- 'Rick Deckard', 'Rachael Rosen', 'John Isidore', 'Phil Resch', 'Pris Stratton', 'Roy Baty', 'Wilbur Mercer', 'Luba Luft', 'Inspector Garland', 'Irmgard Baty', 'Iran Deckard', 'Inspector Bryant', 'Miss Luft'
-- (Miss Luft is an error as already included in Luba Luft)
- 'The Savage', 'Bernard Marx', 'Lenina Crowne', 'The Director', 'Poor Linda' (an error, The Savage's mum is called only Linda), 'Helmholtz Watson'
- 'Alice', 'Mock', 'The' (some expected issues from unconventional character names in Alice in Wonderland)
-- Alternative: 'Alice', 'Mock', 'The', 'Turtle', 'March', 'Queen', 'Rabbit', 'King', 'Hatter', 'Dormouse', 'Gryphon', 'White', 'Mouse', 'Hare', 'Duchess' (modified cut off to over 10 mentions)

Note: Part of the purpose of this project was seeing how easy it is to make an alternative to AI which is able to extract important features from text
Note 2: I consider some of the failures or kinks of this approach to have been due to the methods used and did not expect a perfect result instead hoping for a reasonable result given limited resources

Main data sources used:
- The books listed
- https://norvig.com/ngrams/ (A set of 333,333 most common words in the English language and 250,000 most common sets of two words together from Google Web Trillion Word Corpus)
-- (extracted and ordered by Peter Norvig in 2009)
- https://www.ssa.gov/oact/babynames/limits.html (The top baby names 1880 to 2023 based off of social security number applications in the US)
-- (extracted and ordered by me in 2025)
