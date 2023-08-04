"""
TESTS is a dict with all of your tests.
Keys for this will be the categories' names.
Each test is a dict with
    "input" -- input data for a user function
    "answer" -- your right answer
    "explanation" -- not necessarily a key, it's used for an additional info in animation.
"""


TESTS = {
    "Basics": [
        {
            "input": [21],
            "answer": (0, 6),
        },
        {
            "input": [47],
            "answer": (1, 5),
        },
        {
            "input": [1042],
            "answer": (8, 8),
        },
    ],
    "Extra": [
        {
            "input": [424242],
            "answer": (9030, 6),
        },
        {
            "input": [39088169],
            "answer": (0, 36),
        },
        {
            "input": [39088170],
            "answer": (14930352, 0),
        },
    ]
}
