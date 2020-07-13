import numpy as np
import pickle

def solve(grid, dictionnary):
    n,m = grid.shape

    all_first_cell_to_explore = [(i,j) for i in range(n) for j in range(m)]
    set_subwords = get_set_subwords(dictionnary)

    possible_words_from_cells = [get_all_words_from_cell(grid, first_cell, set_subwords, dictionnary) for first_cell in all_first_cell_to_explore]
    set_possible_words = set([word for words_from_cell in possible_words_from_cells for word in words_from_cell])

    return set_possible_words

def get_all_words_from_cell(grid, first_cell, set_subwords, dictionnary):
    current_cell = None
    current_subword = ""
    possible_words = set()

    stack_moves = [(first_cell, 0)]

    already_visited_cell = [first_cell]
    while stack_moves != []:
        current_cell, subword_level = stack_moves.pop()
        char_current_cell = grid[current_cell]
        current_subword = current_subword[:subword_level] + char_current_cell
        already_visited_cell = already_visited_cell[:subword_level] + [current_cell]
        if current_subword in dictionnary:
            possible_words.add(current_subword)
        if current_subword in set_subwords:
            possible_moves_from_cell = [(cell, len(current_subword)) for cell in get_cells_can_explore(grid, current_cell) if cell not in already_visited_cell]
            stack_moves = stack_moves + possible_moves_from_cell
        print(possible_words)
    return set(possible_words)

def get_set_subwords(dictionnary):
    set_subwords = set()
    for word in dictionnary:
        for i in range(len(word)):
            set_subwords.add(word[:i])
    return set_subwords

def get_cells_can_explore(grid,current_cell):
    n,m = grid.shape
    possible_moves = []
    i,j = current_cell
    if i-1 >= 0 :
        possible_moves.append((i-1,j))
    if i+1 < n:
        possible_moves.append((i+1,j))
    if j-1 >= 0 :
        possible_moves.append((i,j-1))
    if j+1 < n:
        possible_moves.append((i,j+1))
    if j+1 < n and i+1 < m:
        possible_moves.append((i+1,j+1))
    if j-1 >= 0 and i-1 >= 0:
        possible_moves.append((i-1,j-1))  
    if j-1 >= 0 and i+1 < m:
        possible_moves.append((i+1,j-1))
    if j+1 < n and i-1 >= 0:
        possible_moves.append((i-1,j+1))     
    return possible_moves

def string_to_grid(string):
    n_squared = len(string)
    assert np.sqrt(n_squared) == int(np.sqrt(n_squared)), f"{n_squared}"
    n = int(np.sqrt(n_squared))

    string = string.lower()

    grid = np.array([["" for _ in range(n)] for _ in range(n)])
    for (id_letter, letter) in enumerate(string):
        i = id_letter // n
        j = id_letter % n
        grid[i,j] = letter
    return grid

if __name__ == "__main__" :
    import argparse 
    parser = argparse.ArgumentParser()
    parser.add_argument("--string", "-s", help = "left-top to right-bottom string of the grid")
    parser.add_argument("--language", default="fr", choices=["fr"])
    args = parser.parse_args()
    assert len(args.language) == 2

    grid = string_to_grid(args.string)
    dictionnary = pickle.load(open(f"dict_{args.language}.pckl", "rb"))

    print(solve(grid, dictionnary))