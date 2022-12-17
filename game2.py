def user_input():
    """Return proper value provided by user.

    :rtype: str
    :return: value provided by user from ("too small", "too big", "you won")
    """
    possible_input = ("too small", "too big", "you won")
    while True:
        user_answer = input().lower()
        if user_answer in possible_input:
            return user_answer
        print(f"Input is not in {possible_input}")


def calculate_guess_num(rmin, rmax, answer=""):
    """
    Calculate range of possible matches depends on user answer and try to guess the number.

    :param int rmin: min range of possible matches
    :param int rmax: max range of possible matches
    :param str answer: user answer for previous guess

    :rtype: tuple
    :return: new min and max of range as well as new proposed number
    """
    def guess(rmin, rmax):
        return int((rmax - rmin) / 2) + rmin
    if answer == "too small":
        rmin = guess(rmin, rmax)            # rmin = previous guess
    elif answer == "too big":
        rmax = guess(rmin, rmax)            # rmax = previous guess
    elif answer == "you won":
        return (guess(rmin, rmax), ) * 3    # rmin = rmax = previous guess
    return rmin, rmax, guess(rmin, rmax)


def guess_the_number():
    """Main function for our game."""
    print("Imagine number between 0 and 1000!")
    print("Press 'Enter' to continue")
    input()
    min_number = 0
    max_number = 1000
    user_answer = ""
    while user_answer != "you won":
        min_number, max_number, guess = calculate_guess_num(min_number,
                                                            max_number,
                                                            user_answer)
        print(f"Your number is: {guess} ???")
        user_answer = user_input()
    print("Hurra! I guess!")


if __name__ == '__main__':
    guess_the_number()
