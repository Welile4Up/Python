import printing_functions as pf

# Designs that need to be printed
unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []

# Call printing_functions
pf.print_models(unprinted_designs, completed_models)
pf.show_completed_models(completed_models)