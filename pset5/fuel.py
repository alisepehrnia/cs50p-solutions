def main():
    fraction = input("Enter the fuel fraction: ")
    gauge = gauge(fraction)
    print(gauge)


def convert(fraction):
    try:
        x, y = fraction.split('/')
        x = int(x)
        y = int(y)
        if (y == 0):
            raise ZeroDivisionError
        percentage = round(x / y * 100)
        return percentage
    except:
        raise ValueError


def gauge(percentage):
    if percentage <= 1:
        return("E")
    elif percentage >= 99:
        return("F")
    else:
        return(f"{percentage}%")


if __name__ == "__main__":
    main()
