def hangman():
    import random
    challenges = 0

    aLists = ["apple", "pineapple", "lemon", "orange", "peach",
    "kiwifruit", "grapes", "muscat", "raspberry", "strawberry"]

    stages = ["",
    "_______         ",
    "|      |         ",
    "|      |        ",
    "|      O        ",
    "|     /|\       ",
    "|     / \       ",
    "|               "
    ]
    index = random.randint(0, len(aLists)-1)
    ans = aLists[index]
    letters = list(ans)
    board = ["_"] * len(ans)
    win = False
    print("ハングマンへようこそ！")

    while challenges < len(stages):
        print("\n")
        msg = "一文字を予想してね"
        char = input(msg)
        if char in letters:
            order = letters.index(char)
            letters[order] = "$"
            board[order] = char
        else:
            challenges += 1
        print(" ".join(board))
        print("\n".join(stages[0:challenges]))

        if "_" not in board:
            print("あなたの勝ち！")
            print(" ".join(board))
            win = True
            break
    if not win:
        print("\n".join(stages))
        print("あなたの負け！正解は {}。".format(ans))


hangman() 
