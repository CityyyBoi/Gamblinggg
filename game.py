import secrets
balance = 100 # virtual credits

def flip():
    return secrets.choice(["heads", "tails"])

while balance > 0:
    print(f"\nBalance: {balance}")
    bet = input("Bet Amount (or 'q' to quit): ")
    if bet == "q":
        break
    if not bet.isdigit() or not (1 <= int(bet) <= balance):
        print("Enter a whole number up to your balance.")
        continue
    bet = int(bet)

    guess = input("heads or tails? ").lower()
    if guess not in ("heads", "tails"):
        print("Type heads or tails.")
        continue

    result = flip()
    print("Result:", result)
    if guess == result:
        balance += bet
        print("You win!")
    else:
        balance -= bet
        print("You lose.")

print("Game over. Final balance:", balance)
