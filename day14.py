from data import data
import random

score = 0;
game_should_continue = True;

def format_data(account):
    """Takes the account data and returns the printable format"""
    account_name = account["name"]
    account_descrt = account["description"]
    account_country = account["country"]
    return (f"{account_name}, a {account_descrt}, from {account_country}")


def check_answer(guess, a_followers, b_followers):
    """Take the user guess and follower counts and retusn if they got it right"""
    if a_followers > b_followers:
        return guess == 'a'; # return True
    else:
        return guess == 'b'; # return False

while game_should_continue:

    # generate a random account from the data
    account_a = random.choice(data)
    account_b = random.choice(data)

    if account_a == account_b:
        account_b == random.choice(data)

    print(f"Compare A: {format_data(account_a)}")
    print(f"Againt B: {format_data(account_b)}")

    guess = input("Who has more followers? 'A' or 'B': ").lower();

    a_follower_count = account_a["follower_count"]
    b_follower_count = account_b["follower_count"]
    is_correct = check_answer(guess, a_follower_count, b_follower_count)

    if is_correct:
        score += 1
        print(f"You are right! The curremt score is: {score}")
    else:
        game_should_continue = False;
        print(f"Sorry, that's wrong. Final score: {score}")