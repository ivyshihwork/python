import requests

parameters = {
    'amount'    :   10,
    'type'      :   'boolean',

}
url = 'https://opentdb.com/api.php'
response = requests.get(url, params=parameters)
response.raise_for_status()

question_data = response.json()['results']

### THe data looks like below
# [
#     {
#         "category": "Entertainment: Video Games",
#         "type": "boolean",
#         "difficulty": "medium",
#         "question": "DragonForce&#039;s &#039;Through the Fire and Flames&#039; is widely considered to be the hardest song in the Guitar Hero series.",
#         "correct_answer": "True",
#         "incorrect_answers": [
#             "False"
#         ]
#     },
#     {
#         "category": "Entertainment: Musicals & Theatres",
#         "type": "boolean",
#         "difficulty": "easy",
#         "question": "In the play Oedipus Rex, Oedipus kills his father due to jealousy in loving his mother.",
#         "correct_answer": "False",
#         "incorrect_answers": [
#             "True"
#         ]
#     },
