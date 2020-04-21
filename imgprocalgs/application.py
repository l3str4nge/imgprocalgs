""" Main module which is responsible for validating parameters and also running specific algorithms """


# TODO: automate it
DEFINED_ALGORITHMS = [
    'sepia',
    'nearest_neighbour',
    'bilinear_interpolation',
    'bicubic_interpolation',
    'negative'
]


class AlgorithmNotFound(Exception):
    pass


def validate_algorithm_name(name: str):
    if name not in DEFINED_ALGORITHMS:
        raise AlgorithmNotFound(f"Algorithm with name {name} is not defined!")

    return True


def run(parsed_args):
    print(parsed_args.src)
