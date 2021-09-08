N = int(input())
for _ in range(N): # 3
    preference_list = []
    people, _ = map(int, input().split()) # 4 4
    for _ in range(people):
        preference = input() # 1 4 1 4 
        preference_list.append(preference) # [1, 4, 1, 4]

        preference_set = set(preference_list) # [1, 4]

    print(people - len(preference_set))
