#! /usr/bin/env python3

from clyngor import solve

def factify_cellHasDigit(threeple):
    (x, y), d = threeple
    return 'cellHasDigit({}, {}, {}).'.format(x, y, d)

def fset_to_dict(label, fset):
    tuplist = [x[1] for x in list(fset)]
    d = {}
    for (x, y, z) in  tuplist:
        d[(x, y)] = (z, 'answer')
    return d

def maybe_solution(grid, rules_fn):
    rules_fn = rules_fn.decode('utf-8') # bytes to string
    facts = '\n'.join(map(factify_cellHasDigit, grid.items()))
    answers = solve(rules_fn, inline=facts)
    x = next(answers, [])
    if x == []:
        return ('error', {})
    else:
        d = fset_to_dict('cellHasDigit', x)
        for k, v in grid.items():
            d.update({k: (v, 'question')})
        return ('ok', d)

def maybe_valid_grid(grid, rules_fn):
    rules_fn = rules_fn.decode('utf-8') # bytes to string
    facts = '\n'.join(map(factify_cellHasDigit, grid.items()))
    answers = solve(rules_fn, inline=facts, nb_model=100, stats=True)
    nmsf = 0
    for nmsf, model in enumerate(answers, start=1): pass
    nms = answers.statistics.get('Models', None)
    if nms is None: return ('error', 'No solutions found.')
    else: return ('ok', f'{nms} solutions found.')
