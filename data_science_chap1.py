from collections import defaultdict
from collections import Counter  # Pakiet ten nie jest ładowany domyślnie.

users = [
    {"id": 0, "name": "Hero"},
    {"id": 1, "name": "Dunn"},
    {"id": 2, "name": "Sue"},
    {"id": 3, "name": "Chi"},
    {"id": 4, "name": "Thor"},
    {"id": 5, "name": "Clive"},
    {"id": 6, "name": "Hicks"},
    {"id": 7, "name": "Devin"},
    {"id": 8, "name": "Kate"},
    {"id": 9, "name": "Klein"},
]

friendship_pairs = [(0, 1), (0, 2), (1, 2), (1, 3), (2, 3), (3, 4),
                    (4, 5), (5, 6), (5, 7), (6, 8), (7, 8), (8, 9)]

# Inicjalizowanie słownika pustymi listami dla każdego użytkownika:
friendships = {user["id"]: [] for user in users}

# Zapełnienie słownika danymi z wszystkich par znajomości
for i, j in friendship_pairs:
    friendships[i].append(j)  # dodaje j do listy przyjaciół i
    friendships[j].append(i)  # dodaje i do listy przyjaciół j


def number_of_friends(user):
    """Ilu znajomych ma użytkownik?"""
    user_id = user["id"]
    friend_ids = friendships[user_id]
    return len(friend_ids)


total_connections = sum(number_of_friends(user)
                        for user in users)  # 24
# print(total_connections)

################# sorting #################################################################################
sortedCollection = [1, 2, 3, 11]
# sortedCollection.sort(key= lambda a: a, reverse=True)


def selfSort(a):
    return a


sortedCollection.sort(key=selfSort, reverse=True)
# print(sortedCollection)
############################################################################################################

# Utwórz listę (user_id, number_of_friends).
num_friends_by_id = [(user["id"], number_of_friends(user)) for user in users]

num_friends_by_id.sort(  # Sortuj
    key=lambda id_and_friends: id_and_friends[1],  # według number_of_friends
    reverse=True)  # w kolejności malejącej.

# print(num_friends_by_id)


def foaf_ids_bad(user):
    """ Przyjaciół znajomych oznaczamy akronimem foaf. """
    return [foaf_id
            for friend_id in friendships[user["id"]]
            for foaf_id in friendships[friend_id]]

# print("friends of friends: " + str(foaf_ids_bad(users[1])))


def friends_of_friend_ids(user):
    user_id = user["id"]
    return Counter(
        foaf_id
        for friend_id in friendships[user_id]  # Dla każdego z moich przyjaciół
        for foaf_id in friendships[friend_id]  # wybierz ich znajomych,
        if foaf_id != user_id  # którzy nie są mną
        and foaf_id not in friendships[user_id]  # i nie są moimi znajomymi.
    )

# print(friends_of_friend_ids(users[3]))  # userid: occurances count = Counter ({0: 2, 5: 1})


interests = [
    (0, "Hadoop"), (0, "Big Data"), (0, "HBase"), (0, "Java"),
    (0, "Spark"), (0, "Storm"), (0, "Cassandra"),
    (1, "NoSQL"), (1, "MongoDB"), (1, "Cassandra"), (1, "HBase"),
    (1, "Postgres"), (2, "Python"), (2, "scikit-learn"), (2, "scipy"),
    (2, "numpy"), (2, "statsmodels"), (2, "pandas"), (3, "R"), (3, "Python"),
    (3, "statistics"), (3, "regression"), (3, "probability"),
    (4, "machine learning"), (4, "regression"), (4, "decision trees"),
    (4, "libsvm"), (5, "Python"), (5, "R"), (5, "Java"), (5, "C++"),
    (5, "Haskell"), (5, "programming languages"), (6, "statistics"),
    (6, "probability"), (6, "mathematics"), (6, "theory"),
    (7, "machine learning"), (7, "scikit-learn"), (7, "Mahout"),
    (7, "neural networks"), (8, "neural networks"), (8, "deep learning"),
    (8, "Big Data"), (8, "artificial intelligence"), (9, "Hadoop"),
    (9, "Java"), (9, "MapReduce"), (9, "Big Data")
]


def analysts_who_like(target_interest):
    return [user_id
            for user_id, user_interest in interests
            if user_interest == target_interest
            ]

# print(analysts_who_like("regression")) # [3, 4]


user_ids_by_interest = defaultdict(list)

for user_id, interest in interests:
    user_ids_by_interest[interest].append(user_id)

# print(user_ids_by_interest["regression"])

# Klucze są identyfikatorami użytkowników, wartości są listami zainteresowań danego użytkownika.
interests_by_user_id = defaultdict(list)
for user_id, interest in interests:
    interests_by_user_id[user_id].append(interest)

# print("interest by user 3:" + str(interests_by_user_id[3]))

salaries_and_tenures = [(83000, 8.7), (88000, 8.1),
                        (48000, 0.7), (76000, 6),
                        (69000, 6.5), (76000, 7.5),
                        (60000, 2.5), (83000, 10),
                        (48000, 1.9), (63000, 4.2)]


def tenure_bucket(tenure):
    if tenure < 2:
        return "mniej niz 2"
    elif tenure < 5:
        return "miedzy 2 a 5"
    else:
        return "wiecej niz 5"

# Klucze są zakresami wynagrodzeń, wartości są listami wynagrodzeń należących do danego zakresu.
salary_by_tenure_bucket = defaultdict(list)
for salary, tenure in salaries_and_tenures:
    salary_by_tenure_bucket[tenure_bucket(tenure)].append(salary)

# print("salary by tenure:" + str(salary_by_tenure_bucket.items()))

# Klucze są zakresami wynagrodzeń, wartości określają średnie wynagrodzenie w danym zakresie
average_salary_by_bucket = {
    tenure: sum(salaries) / len(salaries)
    for tenure, salaries in salary_by_tenure_bucket.items()
}

# print("average salary by tenure:" + str(average_salary_by_bucket))