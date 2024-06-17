from colors import bcolors


def print_with_colors(color, msg):
    print(color, msg, bcolors.ENDC)


def get_machine_epsilon():
    eps = 1.0
    while (1.0 + eps) > 1.0:
        eps = eps / 2.0
    eps = eps * 2.0
    return eps


def run_on_expression(expr):
    print(f"\nResult of {expr} :")
    eval_expr = eval(expr)
    print_with_colors(bcolors.FAIL, f"before using machine epsilon: {format(eval_expr)}")
    print_with_colors(bcolors.OKGREEN, f"After correcting with machine epsilon: {format(eval_expr - epsilon)}")


if __name__ == '__main__':
    epsilon = get_machine_epsilon()
    print_with_colors(bcolors.OKBLUE, f"Machine Precision  : {epsilon}")
    run_on_expression("abs(3.0 * (4.0 / 3.0 - 1.0) - 1.0)")
