# oponents_move is ether 'stay silent' or 'testify'
def play(oponents_last_move: str) -> str:
    # here implement your strategy
    # example strategy is to stay silent unless the other player testifies
    if oponents_last_move == 'none':
        # this is the first move
        return 'stay silent'

    if oponents_last_move == 'stay silent':
        return 'stay silent'

    # by elimination oponents_last_move must be 'testify'
    return 'testify'
