class User:
    """Demonstrating a user profile."""

    def __init__(self, first_name, last_name, email_address, password, language, login_attempts):
        """Initialize the user profile attributes."""
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.email_address = email_address
        self.password = password
        self.language = language.title()
        self.login_attempts = login_attempts

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

    def increment_login_attempts(self):
        """Increment the value of login_attempts."""
        self.login_attempts += 1

    def reset_login_attempts(self):
        """Reset login_attempts to 0."""
        self.login_attempts = 0

john = User('john', 'moshoeu', 'shoes@hotmail.com', 'shoooz', 'sotho', 0)
john.describe_user()
john.greet_user()

print("\nMaking 4 login attempts...")
john.increment_login_attempts()
john.increment_login_attempts()
john.increment_login_attempts()
john.increment_login_attempts()
print(f"Login attempts: {john.login_attempts}")

print("\nResetting login attempts...")
john.reset_login_attempts()
print(f"Login attempts: {john.login_attempts}")