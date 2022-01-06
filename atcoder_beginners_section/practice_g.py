N = int(input())
a = list(map(int, input().split()))


allice_cards = []
bob_cards = []

for i, a_i in enumerate(reversed(sorted(a))):
    if i % 2 == 0:
        allice_cards.append(a_i)
    else:
        bob_cards.append(a_i)
print(sum(allice_cards) - sum(bob_cards))
