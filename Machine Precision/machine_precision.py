from colors import bcolors


class printColors:
    @staticmethod
    def print_fail_msg(msg):
        print(bcolors.FAIL, msg, bcolors.ENDC)

    @staticmethod
    def print_okgreen_msg(msg):
        print(bcolors.OKGREEN, msg, bcolors.ENDC)

    @staticmethod
    def print_okblue_msg(msg):
        print(bcolors.OKBLUE, msg, bcolors.ENDC)


def get_machine_epsilon():
    eps = 1.0
    while (1.0 + eps) > 1.0:
        eps = eps / 2.0

    eps = eps * 2.0
    return eps


if __name__ == '__main__':
    epsilon = get_machine_epsilon()
    printColors.print_okblue_msg(f"Machine Precision  : {epsilon}")

    expression = abs(3.0 * (4.0 / 3.0 - 1.0) - 1.0)
    print("\nResult of abs(3.0 * (4.0 / 3.0 - 1.0) - 1.0) :")
    printColors.print_fail_msg(f"before using machine epsilon: {format(expression)}")
    printColors.print_okgreen_msg(f"After correcting with machine epsilon: {format(expression - epsilon)}")
