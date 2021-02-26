# is-it-shuffled
Does shuffling a deck of cards where some of the cards are set aside mean that you can shuffle less if you then add those cards back in? No! This repo explores why.

What is shuffling and why do we do it?
===
[Shuffling](https://en.wikipedia.org/wiki/Shuffling) is a procedure used to randomize a deck of playing cards. In games where chance is involved, shuffling is necessary in order to prevent any party from influencing the outcome of a card draw.

Take this deck of 5 cards as an example:

<img src="images/playing-cards/AS.png" width="10%"/>
<img src="images/playing-cards/2H.png" width="10%"/>
<img src="images/playing-cards/3C.png" width="10%"/>
<img src="images/playing-cards/4D.png" width="10%"/>
<img src="images/playing-cards/5H.png" width="10%"/>

Are these cards sorted in order? Many people would say "yes", though the correct answer is actually "it depends".

Before we can say if a given deck of cards is in order, we need to decide what a sorted deck looks like! For our purposes, the following run of the 52 standard playing cards will be considered fully sorted:

</br>
<img src="images/playing-cards/AS.png" width="5%"/> <img src="images/playing-cards/2S.png" width="5%"/>
<img src="images/playing-cards/3S.png" width="5%"/> <img src="images/playing-cards/4S.png" width="5%"/>
<img src="images/playing-cards/5S.png" width="5%"/> <img src="images/playing-cards/6S.png" width="5%"/>
<img src="images/playing-cards/7S.png" width="5%"/> <img src="images/playing-cards/8S.png" width="5%"/>
<img src="images/playing-cards/9S.png" width="5%"/> <img src="images/playing-cards/10S.png" width="5%"/>
<img src="images/playing-cards/JS.png" width="5%"/> <img src="images/playing-cards/QS.png" width="5%"/>
<img src="images/playing-cards/KS.png" width="5%"/>
</br>
<img src="images/playing-cards/AH.png" width="5%"/> <img src="images/playing-cards/2H.png" width="5%"/>
<img src="images/playing-cards/3H.png" width="5%"/> <img src="images/playing-cards/4H.png" width="5%"/>
<img src="images/playing-cards/5H.png" width="5%"/> <img src="images/playing-cards/6H.png" width="5%"/>
<img src="images/playing-cards/7H.png" width="5%"/> <img src="images/playing-cards/8H.png" width="5%"/>
<img src="images/playing-cards/9H.png" width="5%"/> <img src="images/playing-cards/10H.png" width="5%"/>
<img src="images/playing-cards/JH.png" width="5%"/> <img src="images/playing-cards/QH.png" width="5%"/>
<img src="images/playing-cards/KH.png" width="5%"/>
</br>
<img src="images/playing-cards/AC.png" width="5%"/> <img src="images/playing-cards/2C.png" width="5%"/>
<img src="images/playing-cards/3C.png" width="5%"/> <img src="images/playing-cards/4C.png" width="5%"/>
<img src="images/playing-cards/5C.png" width="5%"/> <img src="images/playing-cards/6C.png" width="5%"/>
<img src="images/playing-cards/7C.png" width="5%"/> <img src="images/playing-cards/8C.png" width="5%"/>
<img src="images/playing-cards/9C.png" width="5%"/> <img src="images/playing-cards/10C.png" width="5%"/>
<img src="images/playing-cards/JC.png" width="5%"/> <img src="images/playing-cards/QC.png" width="5%"/>
<img src="images/playing-cards/KC.png" width="5%"/>
</br>
<img src="images/playing-cards/AD.png" width="5%"/> <img src="images/playing-cards/2D.png" width="5%"/>
<img src="images/playing-cards/3D.png" width="5%"/> <img src="images/playing-cards/4D.png" width="5%"/>
<img src="images/playing-cards/5D.png" width="5%"/> <img src="images/playing-cards/6D.png" width="5%"/>
<img src="images/playing-cards/7D.png" width="5%"/> <img src="images/playing-cards/8D.png" width="5%"/>
<img src="images/playing-cards/9D.png" width="5%"/> <img src="images/playing-cards/10D.png" width="5%"/>
<img src="images/playing-cards/JD.png" width="5%"/> <img src="images/playing-cards/QD.png" width="5%"/>
<img src="images/playing-cards/KD.png" width="5%"/>
</br>
</br>

The shuffle that we will be using is an "Imperfect Riffle". This is one fo the most common methods of shuffling a deck of cards, and involves splitting a deck of cards into two piles, then approximately merging them together with alternating cards from each pile until both piles run out. We say "approximately" because when humans riffle shuffle, they almost always have defects, such splitting the deck unevenly or taking more than one card in a row from the same pile.

Lets take the following deck of cards and give it a few shuffles:

<img src="images/playing-cards/AS.png" width="5%"/> <img src="images/playing-cards/2S.png" width="5%"/>
<img src="images/playing-cards/3S.png" width="5%"/> <img src="images/playing-cards/4S.png" width="5%"/>
<img src="images/playing-cards/5S.png" width="5%"/>
<img src="images/playing-cards/AH.png" width="5%"/> <img src="images/playing-cards/2H.png" width="5%"/>
<img src="images/playing-cards/3H.png" width="5%"/> <img src="images/playing-cards/4H.png" width="5%"/>
<img src="images/playing-cards/5H.png" width="5%"/>