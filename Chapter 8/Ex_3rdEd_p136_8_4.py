def make_shirt(size='large', message='I love Python!'):
    """Summary of shirt size and message to be printed on it."""
    print(f"\nThis is a size {size} t-shirt.")
    print(f'The printed message will be, "{message}"')

make_shirt()
make_shirt(size='medium')
make_shirt(size='extra small', message='Software developers are creative.')