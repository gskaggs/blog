% Genetic Algorithms for the Iterated Prisoner's Dilemma 
% Grant Skaggs 
% 9 August 2020

# Genetic Algorithms for the Iterated Prisoner's Dilemma

Before this summer, I had reasonable familiarity with that classic of game theory—[the prisoner’s dilemma](). However, not until I read Richard Dawkins’ [The Selfish Gene]() did I begin to appreciate the incredibly far-reach of this little thought experiment. 

In the book’s twelfth chapter, playfully entitled “Nice Guys Finish First,” Dawkins explains several natural phenomena as examples of prisoner’s dilemma in disguise. Many commonplace interactions—the grooming habits of birds, how wasps pollinate fig trees, the symbiotic bacteria in our guts—turn out to be games where cooperation and defection can mean life or death for evolutionary players, and the individuals which do best are often those most deftly evolved to navigate the paradoxical paradigm.

The natural world often differs from the dilemma’s usual penal context in an important fundamental way. Unlike prisoners at risk of long jail sentences, the two members of a bird population may interact with each other many times. At each meeting they may identify their neighbor and remember his past tendencies to cooperate or defect. Here, the birds’ strategies may depend heavily on the past behavior of their community members.

We call this variation the classic game the iterated prisoner’s dilemma. Strategies do well if they avoid being betrayed and either cooperate with or take advantage of cooperative agents. Unlike the original prisoner’s dilemma, an optimal strategy is by no means obvious and success depends on the strategies which compose an individual’s population. 

Beginning famously with [the work of Axelrod in …](), researchers have gone to great lengths exploring [the various possible strategies for the iterated prisoner’s dilemma.]() Stanford’s encyclopedia of philosophy summarizes the literature on this and other variations of the prisoner’s dilemma in [its fascinating entry on the topic.]() 

Of particular interest to me is research applying machine learning to generate or assess strategies for the iterated prisoner’s dilemma. Martin Kies in his recent paper [Finding Best Answers for the Iterated Prisoner’s Dilemma Using Improved Q-Learning]() provides an excellent review of the literature in this space. 

In Kies’ literature review I discovered [Evolution of iterated prisoner's dilemma strategies with different history lengths in static and cultural environments]() by Brunauer and Mayer. This paper uses [genetic algorithms]() to produce effective strategies to the iterated prisoner’s dilemma. They represent each genetic agent as a single chromosome where each “gene” encodes how the agent should act for a particular history of its moves played. The length of history used varies from 1 to 6 actions, which in the latter case demands chromosomes containing several thousand genes.

Over the past couple weeks I replicated the experiments of Brunauer and Mayer. My implementation differed from theirs in the exact parameters used for the genetic algorithms and in the classical strategies used as opponents for the fitness function. Additionally, I coded all the tournament and genetic code myself in Python instead of using external libraries. However, interestingly my results corroborated theirs in that longer history lengths didn’t necessarily improve performance. 

Feel free to browse the source code on [its GitHub page.]()


 




