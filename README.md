# bball

Run "generate brackets.py" to randomly generate your own men's and women's brackets from the FiveThirtyEight probabilities.

Run "simulate_until_cats_s16.py" to keep simulating until you get a men's bracket where the Vermont Catamounts make the Sweet 16 (~3% probability)

Requirments:
numpy
pandas
scipy
matplotlib if you want to see the reverse-engineering of the 538 probability distribution (add a 2nd argument, True, to the import_538 function)
