class User:
    """Demonstrating a user profile."""

    def __init__(self, first_name, last_name, email_address, password, language):
        """Initialize the user profile attributes."""
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.email_address = email_address
        self.password = password
        self.language = language.title()

    def describe_user(self):
        """Present a summary of the user's information."""
        print(f"\nFirst Name: {self.first_name}")
        print(f"Last Name: {self.last_name}")
        print(f"Email Address: {self.email_address}")
        print(f"Password: {self.password}")
        print(f"Language: {self.language}")

    def greet_user(self):
        """Show a personalized greeting to the user."""
        print(f"\nGood day, {self.first_name}!")

john = User('john', 'moshoeu', 'shoes@hotmail.com', 'shoooz', 'sotho')
john.describe_user()
john.greet_user()

mary = User('mary', 'blige', 'mblige@gmail.com', 'walkandstumble', 'english')
mary.describe_user()
mary.greet_user()