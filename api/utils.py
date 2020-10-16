from random import seed, random


def _get_random(min_num, max_num):
    return random() * (max_num - min_num) + min_num


def generate_time_series_data(n):
    data = []
    seed()
    for i in range(n):
        if i == 0:
            y = _get_random(0, 1)
        else:
            y = max(data[i-1]['y'] + _get_random(-1, 1), 0)
        data.append({
            'x': i,
            'y': y
        })

    return data