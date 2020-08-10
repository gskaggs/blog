% Genetic Algorithms for the Iterated Prisoner's Dilemma 
% Grant Skaggs 
% 9 August 2020

# Genetic Algorithms for the Iterated Prisoner's Dilemma

I recently discovered [Evolution of iterated prisoner's dilemma strategies with different history lengths in static and cultural environments](https://www.researchgate.net/publication/220999970_Evolution_of_iterated_prisoner's_dilemma_strategies_with_different_history_lengths_in_static_and_cultural_environments) by Brunauer and Mayer. This paper uses [genetic algorithms](https://towardsdatascience.com/introduction-to-genetic-algorithms-including-example-code-e396e98d8bf3) to produce effective strategies for the *iterated prisoner’s dilemma* problem.

Brunauer and Mayer represent each genetic agent as a single chromosome where every “gene” encodes how the agent should act for a particular history of moves played. The length of history used varies from 1 to 6 actions, which in the latter case demands chromosomes containing several thousand genes.

Over the past couple weeks I replicated the experiments of Brunauer and Mayer. My implementation differs from theirs in the parameters used for the genetic algorithms and in the exact classical strategies used as opponents for the fitness function. Additionally, I coded all the tournament and genetic code myself in Python instead of using external libraries. However, interestingly my results corroborated theirs in that longer history lengths did not necessarily improve performance. 

Feel free to browse my source code and archived results on [the project's public GitHub page.](https://github.com/gskaggs/iterated-prisoners-dilemma)


### Background Info

Before this summer, I had reasonable familiarity with that classic of game theory—[the prisoner’s dilemma](). However, not until I read Richard Dawkins’ [The Selfish Gene](https://www.amazon.com/Selfish-Gene-Anniversary-Landmark-Paperback/dp/B0722G5V92) did I begin to appreciate the incredibly far-reach of this little thought experiment. 

In the book’s twelfth chapter, playfully entitled “Nice Guys Finish First,” Dawkins explains several natural phenomena as examples of prisoner’s dilemma in disguise. Many commonplace interactions—the grooming habits of birds, how wasps pollinate fig trees, our symbiotic relationship with gut bacteria—turn out to be games where cooperation and defection may mean life or death for evolutionary players, and the individuals who do best are often those most deftly evolved to navigate the dilemma's paradoxical paradigm.

The natural world often differs from the dilemma’s usual penal context in an important fundamental way. Unlike prisoners at risk of long prison sentences, two members of a bird population may have a chance to cooperate with each other many times. At each meeting they may identify their neighbor and remember his past tendencies to cooperate or defect. Here, the birds’ strategies will likely depend heavily on the past behavior of their community members.

We call this variation of the classic game the iterated prisoner’s dilemma. Strategies do well if they avoid being betrayed and either cooperate with or take advantage of cooperative agents. Unlike the original prisoner’s dilemma, an optimal strategy is by no means obvious and success depends on the strategies which compose an individual’s population. 

Researchers have gone to great lengths exploring [the various possible strategies for the iterated prisoner’s dilemma.](https://plato.stanford.edu/entries/prisoner-dilemma/strategy-table.html) Stanford’s encyclopedia of philosophy summarizes the literature on this and other variations of the prisoner’s dilemma in [its fascinating entry on the topic.](https://plato.stanford.edu/entries/prisoner-dilemma/) 

Of particular interest to me is the relatively recent research applying machine learning to generate or assess strategies for the iterated prisoner’s dilemma. Martin Kies in his paper [Finding Best Answers for the Iterated Prisoner’s Dilemma Using Improved Q-Learning](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=3556714) provides an excellent literature review in this space. 



 





