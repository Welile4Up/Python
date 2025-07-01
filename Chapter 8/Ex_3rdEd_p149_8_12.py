def make_sandwich(*fillings):
    """Summarize the sandwich we are making."""
    print("\nWe are making your sandwich:")
    for filling in fillings:
        print(f"  ...putting {filling} inside your sandwich.")
    print("Your sandwich is ready for collection.")

make_sandwich('ham', 'cheese sarnie')
make_sandwich('turkey', 'emmental', 'egg')
make_sandwich('steak', 'relish', 'mayo')