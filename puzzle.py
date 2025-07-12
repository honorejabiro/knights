from logic import *

AKnight = Symbol("A is a Knight")
AKnave = Symbol("A is a Knave")

BKnight = Symbol("B is a Knight")
BKnave = Symbol("B is a Knave")

CKnight = Symbol("C is a Knight")
CKnave = Symbol("C is a Knave")

# Puzzle 0
# A says "I am both a knight and a knave."
knowledge0 = And(
    # TODO
    #A can be a knight or a Knave but not both
    And(Or(AKnight, AKnave), Not(And(AKnave, AKnight))),
    Implication(AKnight, And(AKnight, AKnave)),
    Implication(AKnave, Not(And(AKnave, AKnight)))
)

# Puzzle 1
# A says "We are both knaves."
# B says nothing.
knowledge1 = And(
    # TODO
    #A can be a knight or a Knave but not both
    And(Or(AKnight, AKnave), Not(And(AKnave, AKnight))),
    #B can be a Knight or Knave but not both
    And(Or(BKnight, BKnave), Not(And(BKnave, BKnight))),
    #if A is a Knave then the statement is false
    Implication(AKnave, Not(And(AKnave, BKnave))),
    #if A is knight then the sentence is True
    Implication(AKnight, And(AKnave, BKnave))

)

# Puzzle 2
# A says "We are the same kind."
# B says "We are of different kinds."
knowledge2 = And(
    # TODO
    #A can be a knight or a Knave but not both
    And(Or(AKnight, AKnave), Not(And(AKnave, AKnight))),
    #B can be a Knight or Knave but not both
    And(Or(BKnight, BKnave), Not(And(BKnave, BKnight))),
    #If A is a knight then the statement is true
    Implication(AKnight, Or(And(AKnight, BKnight), And(AKnave, BKnave))),
    #If A knave then the statement is false
    Implication(AKnave, Not(Or(And(AKnight, BKnight), And(AKnave, BKnave)))),
    #If B is a knight then the statement is true
    Implication(BKnight, Or(And(AKnave, BKnight), And(AKnight, BKnave))),
    #If B knave then the statement is false
    Implication(BKnave, Not(Or(And(AKnave, BKnight), And(AKnight, BKnave))))
)

# Puzzle 3
# A says either "I am a knight." or "I am a knave.", but you don't know which.
# B says "A said 'I am a knave'."
# B says "C is a knave."
# C says "A is a knight."
knowledge3 = And(
    # TODO
    #A can be a knight or a Knave but not both
    And(Or(AKnight, AKnave), Not(And(AKnave, AKnight))),
    #B can be a Knight or Knave but not both
    And(Or(BKnight, BKnave), Not(And(BKnave, BKnight))),
    #C can be a Knight or knave but not both
    And(Or(CKnight, CKnave), Not(And(CKnave, CKnight))),
    #If B is a Knight then A said he is a Knave
    Implication(BKnight, And(
            #If A is a knight then he is telling the truth
            Implication(AKnight, AKnave),
            #If A is a Knave then he is not telling the truth
            Implication(AKnave, Not(AKnave)))),
    #If B is a Knight then C is a Knave
    Implication(BKnight, CKnave),
    #If B is a Knave then A said I am a knight and C is a Knave
    Implication(BKnave, And(
        #If A is a Knight then the statement is True
        Implication(AKnight, AKnight),
        Implication(AKnave, Not(AKnight))
    )),
    Implication(BKnave, CKnight),
    #If C is a Knight then A is a Knight
    Implication(CKnight, AKnight),
    #If C is a Knave then A is a Knight
    Implication(CKnave, AKnave)
    
)


def main():
    symbols = [AKnight, AKnave, BKnight, BKnave, CKnight, CKnave]
    puzzles = [
        ("Puzzle 0", knowledge0),
        ("Puzzle 1", knowledge1),
        ("Puzzle 2", knowledge2),
        ("Puzzle 3", knowledge3)
    ]
    for puzzle, knowledge in puzzles:
        print(puzzle)
        if len(knowledge.conjuncts) == 0:
            print("    Not yet implemented.")
        else:
            for symbol in symbols:
                if model_check(knowledge, symbol):
                    print(f"    {symbol}")


if __name__ == "__main__":
    main()
