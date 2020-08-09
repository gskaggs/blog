% Genetic Algorithms for the Iterated Prisoner's Dilemma 
% Grant Skaggs 
% 9 August 2020

# Genetic Algorithms for the Iterated Prisoner's Dilemma

Before this summer, I had reasonable familiarity with that classic of game theory—[the prisoner’s dilemma](). However, not until I read Richard Dawkins’ [The Selfish Gene]() did I begin to appreciate the incredibly far-reach of this little thought experiment. 

Dawkins abandons the usual penal context, considering instead the grooming behavior of a hypothetical bird species. When two of these hypothetical birds meet, they both have a subtle choice. Each can either help the other groom or refuse to do so. 

In this scenario, mutual cooperation means a body free of leaches in those places your own beak can’t reach. Nonetheless, a particularly selfish bird might let his friend groom him and then refuse to reciprocate the help. In doing so, he increases his own chance of survival at the cost of the betrayed bird. Indeed, we could imagine that two cynical birds crossing paths may both refuse to cooperate, neither one willing to risk being a sucker. 

Framed in this way, the grooming habits of these birds is the prisoner’s dilemma in disguise. It differs however from the original game in a fundamental way. Unlike prisoners at risk of long sentences, the birds in our example will likely see each other many times. At each meeting they have the opportunity to identify their opponent and remember his past behavior. In this game, players’ strategies may depend heavily on the past behavior of their opponents.

We call this variation the iterated prisoner’s dilemma. 
