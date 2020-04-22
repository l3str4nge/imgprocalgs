""" Main module which is responsible for validating parameters and also running specific algorithms """

from imgprocalgs import algorithms


class AlgorithmNotFound(Exception):
    pass


def validate_algorithm_name(name: str):
    if name not in algorithms.__ALGORITHMS__:
        raise AlgorithmNotFound(f"Algorithm with name {name} is not defined!")

    return True


def run(parsed_args):
    print(parsed_args.src)
