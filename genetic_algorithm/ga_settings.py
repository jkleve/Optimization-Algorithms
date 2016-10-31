settings = {
    'population_size': 20, # number of organisms
    'number_of_dimensions': 2,
    'bounds': [ # this must have 1 pair per dimension
        (-10,10),
        (-10,10)
    ],
    'selection_multiplier': 0.85,
    'selection_cutoff': 0.5,
    'mutation_rate': 0.02, # how often a mutation happens (between 0 and 1)
    'mutation_amount': 0.4, # how large of a mutation is allowed (between 0 and 1)
    'step_through': False, # TODO not implemented. whether it should pause after each iteration
    'plot': True, # whether we should plot each iteration
    'debug': True # whether we should print each iteration
}
