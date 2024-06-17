from colors import bcolors


def print_with_colors(color, msg):
    print(color, msg, bcolors.ENDC)


def get_machine_epsilon():
    eps = 1.0
    while (1.0 + eps) > 1.0:
        eps = eps / 2.0

    eps = eps * 2.0
    return eps


if __name__ == '__main__':
    epsilon = get_machine_epsilon()
    print_with_colors(bcolors.OKBLUE, f"Machine Precision  : {epsilon}")

    expression = abs(3.0 * (4.0 / 3.0 - 1.0) - 1.0)
    print("\nResult of abs(3.0 * (4.0 / 3.0 - 1.0) - 1.0) :")
    print_with_colors(bcolors.FAIL, f"before using machine epsilon: {format(expression)}")
    print_with_colors(bcolors.OKGREEN, f"After correcting with machine epsilon: {format(expression - epsilon)}")
