def get_competitor_data():
    num_competitors = int(input("Enter the number of competitors: "))
    competitors = []

    for i in range(num_competitors):
        surname = input(f"Enter the surname of competitor {i + 1}: ")
        score = float(input(f"Enter the score of competitor {i + 1}: "))
        competitors.append((surname, score))

    return competitors

def print_results(competitors):
    competitors.sort(key=lambda x: x[1], reverse=True)
    place = 1
    prev_score = None
    prev_place = None
    for i, competitor in enumerate(competitors):
        if competitor[1] != prev_score:
            if prev_place is not None:
                place = prev_place + 1
            else:
                place = i + 1
        print(f"{place}. {competitor[0]} - {competitor[1]}")
        prev_score = competitor[1]
        prev_place = place

competitors = get_competitor_data()
print("Results:")
print_results(competitors)
