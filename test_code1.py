import random
from data import data
from art_logo import art_logo

def play_game():
    print("\nWelcome to the Higher - Lower Game!")

    random_values = random.sample(data, 2)
    first_random_value = random_values[0]["name"]
    second_random_value = random_values[1]["name"]

    first_follower_count = next(item["follower_count"] for item in data if item["name"] == first_random_value)
    second_follower_count = next(item["follower_count"] for item in data if item["name"] == second_random_value)

    print(f"The two things that you need to compare is: {first_random_value} and {second_random_value}\n")
    print(f"Is {second_random_value} higher or lower than {first_random_value}?")
    print("\nChoose:")
    print("1) Higher\n2) Lower")
    option = int(input("--> "))

    if (second_follower_count > first_follower_count) and (option == 1):
        print(f"The {first_random_value} has {first_follower_count} followers and the {second_random_value} has {second_follower_count} followers")
        print("You won")
    elif (second_follower_count < first_follower_count) and (option == 1):
        print(f"The {first_random_value} has {first_follower_count} and the {second_random_value} has {second_follower_count} followers")
        print("You lost")
    elif (second_follower_count > first_follower_count) and (option == 2):
        print(f"The {first_random_value} has {first_follower_count} and the {second_random_value} has {second_follower_count} followers")
        print("You lost")
    elif (second_follower_count < first_follower_count) and (option == 2):
        print(f"The {first_random_value} has {first_follower_count} followers and the {second_random_value} has {second_follower_count} followers")
        print("You won")

# Game loop
while True:
    play_game()

    choice = input("\nDo you want to play again? (yes/no): ")
    if choice.lower() != "yes":
        break

print("Thank you for playing!")
