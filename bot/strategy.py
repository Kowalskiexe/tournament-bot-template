# opponents_last_move is ether 'stay silent', 'testify', 'none' if it's the first round
def play(opponents_last_move: str) -> str:
    # here implement your strategy
    # example strategy is to stay silent unless the other player testifies
    if opponents_last_move == 'none':
        # this is the first move
        return 'stay silent'

    if opponents_last_move == 'stay silent':
        return 'stay silent'

    # by elimination opponents_last_move must be 'testify'
    return 'testify'
