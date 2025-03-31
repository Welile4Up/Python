def make_shirt(size, message):
    """Summary of shirt size and message to be printed on it."""
    print(f"\nThis is a size {size} t-shirt.")
    print(f'The printed message will be, "{message}"')

make_shirt('small', 'Coding is great!')
make_shirt(size='large', message="Indentation helps.")