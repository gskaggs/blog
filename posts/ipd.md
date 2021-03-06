% Genetic Algorithms for the Iterated Prisoner's Dilemma 
% Grant Skaggs 
% 11 August 2020

# Genetic Algorithms for...

<link rel="stylesheet" href="../css/posts.css">
<img src="../resources/ipd/ipd.png" alt="the iterated prisoner's dilemma">

I recently discovered [Evolution of Iterated Prisoner's Dilemma Strategies with Different History Lengths in Static and Cultural Environments](https://www.researchgate.net/publication/220999970_Evolution_of_iterated_prisoner's_dilemma_strategies_with_different_history_lengths_in_static_and_cultural_environments) by Brunauer and Mayer. This paper uses [genetic algorithms](https://towardsdatascience.com/introduction-to-genetic-algorithms-including-example-code-e396e98d8bf3) to produce effective strategies for the *iterated prisoner’s dilemma.*

In economics, the iterated prisoner's dilemma is a game in which players repeatedly engage in episodes of [the classic prisoner’s dilemma](https://en.wikipedia.org/wiki/Prisoner%27s_dilemma). As in [high stakes Uno](https://www.nytimes.com/2016/01/13/sports/basketball/for-some-atlanta-hawks-a-revved-up-game-of-uno-is-diversion-no-1.html), players do well if they navigate the treacherous waters of betrayal and cooperation. Unlike in the original prisoner’s dilemma, an optimal rational strategy here is by no means obvious.

Brunauer and Mayer represent each player as a single chromosome where every “gene” encodes how the agent should act after a particular history of moves played. The length of history used varies from 1 to 6 moves, which in the latter case demands chromosomes containing several thousand genes. To “evolve” these players, the authors test each generation of chromosomes against classic strategies. They make sure chromosomes which perform well are more likely to pass their genes on to subsequent generations—although they also introduce some amount of variation through genetic mutation and crossover. 

After simulating several thousand generations, Brunauer and Mayer demonstrated the dominance of their evolved champions against more traditional static strategies. 

Over the past couple weeks I replicated the experiments of Brunauer and Mayer. My implementation differs from theirs in the parameters used for the genetic algorithms and in the exact adversarial classical strategies used to test the fitness of genetic agents. Additionally, I coded all the tournament and genetic code in Python instead of using external libraries. However, interestingly my results corroborated theirs in that longer history lengths did not necessarily improve performance. 

Feel free to browse my source code and archived results in [the project's public GitHub repository.](https://github.com/gskaggs/iterated-prisoners-dilemma)


And don't forget to try your hand against Loki, the project’s cream of the crop. Click **C** to cooperate and **D** to defect. See how many more points you can earn in an iterated prisoner’s dilemma with the master of mischief.

<img src="../resources/ipd/moves/C.png" alt="player one's moves" onclick="recordMove(0)" style="width: 40%; padding-right:3%; padding-left:5%; float:left; cursor:pointer;">
<img src="../resources/ipd/moves/D.png" alt="player two's moves" onclick="recordMove(1)" style="width: 40%; padding-left:3%; padding-right:5%; float:right; cursor:pointer;">

<br>

<h2 style="text-align:center;">Ready Player One?</h3>
<p style="clear: both;"></p>

<h3 id="player-move" style="text-align:center; color:#011175;"></h3>
<h3 id="loki-move" style="text-align:center;"></h3>

<p style="clear: both;"></p>

<script> 

var scoreLabel = document.getElementById("score");
var playerMoveLabel = document.getElementById("player-move");
var lokiMoveLabel = document.getElementById("loki-move");
var historyLen = 3;
var hist = 0;
var lokiMoveLookUp = [0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1, 1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 1, 1, 0, 0, 0, 1, 1, 1, 0, 1, 0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0, 1, 1, 0, 1, 1, 0]
var scores = [0, 0]

var lokiRewardLookUp = [1, 2, -1, 0]
var playerRewardLookUp = [1, -1, 2, 0]

function recordMove(playerMove) {
    lokiMove = lokiMoveLookUp[hist];
    curMove = playerMove << 1 | lokiMove;
    scores[0] += playerRewardLookUp[curMove];
    scores[1] += lokiRewardLookUp[curMove];

    var bitMask = (1 <<  2 * historyLen) - 1;
    hist = (hist << 2) & bitMask;
    hist |= curMove;

    if (playerMove) {
        playerMoveLabel.innerHTML = "You defected. Your reward: " + playerRewardLookUp[curMove] + " Your score: " + scores[0];
    } else {
        playerMoveLabel.innerHTML = "You cooperated. Your reward: " + playerRewardLookUp[curMove] + " Your score: " + scores[0];
    }

    if (lokiMove) {
        lokiMoveLabel.innerHTML = "Loki defected. Loki's reward: " + lokiRewardLookUp[curMove] + " Loki's score: " + scores[1];
    } else {
        lokiMoveLabel.innerHTML = "Loki cooperated. Loki's reward: " + lokiRewardLookUp[curMove] + " Loki's score: " + scores[1];
    }
}

</script>

### Favorite Resources

Before this summer, I had reasonable familiarity with that classic of game theory—the prisoner's dilemma. However, not until I read Richard Dawkins’ [The Selfish Gene](https://www.amazon.com/Selfish-Gene-Anniversary-Landmark-Paperback/dp/B0722G5V92) did I begin to appreciate the incredible far-reach of this little thought experiment. 

In the book’s twelfth chapter, playfully entitled “Nice Guys Finish First,” Dawkins explains several natural instances of evolved cooperation as the prisoner’s dilemma in disguise. Many commonplace interactions—the grooming habits of birds, how wasps pollinate fig trees, humanity's symbiotic relationship with its gut bacteria—turn out to be games where cooperation and defection may mean life or death for evolutionary players, and the individuals who do best are often those most deftly evolved to navigate the paradoxical dilemma.

The natural world often differs from the dilemma’s usual penal context in an important fundamental way. Unlike prisoners at risk of long jail sentences, two individuals within a bird or chimp population may have the opportunity to mutually cooperate many times. At each meeting they may identify their neighbor and remember his past tendency to betray. Unsurprisingly, we call the resultant strategetic paradigm the iterated prisoner's dilemma.

Researchers have gone to great lengths exploring [strategies for this variant of the classic game.](https://plato.stanford.edu/entries/prisoner-dilemma/strategy-table.html) Stanford’s encyclopedia of philosophy summarizes the literature on this and other variants of the prisoner’s dilemma in [its fascinating entry on the topic.](https://plato.stanford.edu/entries/prisoner-dilemma/) 

Of particular interest to me is the relatively recent research applying machine learning to generate or assess strategies for the iterated prisoner’s dilemma. Martin Kies in his paper [Finding Best Answers for the Iterated Prisoner’s Dilemma Using Improved Q-Learning](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=3556714) provides an excellent literature review in this space. 



 





