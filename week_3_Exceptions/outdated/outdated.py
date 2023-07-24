months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]


def main():
    m, d, y = get_date()
    print(f"{y}-{m:02}-{d:02}")

def get_date():
    while True:
        s = input("Date: ")
        try:
            if len(s) <= 10:
                m, d, y = s.split(sep="/")
                if int(m) <= 12 and int(d) <= 31:
                    return int(m), int(d), int(y)
            else:
                m, d, y = s.split()
                return convert(m, d, y)
        except ValueError:
            pass


def convert(month, day, year):
    x = months.index(month) + 1
    y = int(day.rstrip(","))
    z = int(year)
    if x <= 12 and y <= 31 and day.endswith(","):
        return x, y, z
    else:
        raise ValueError


main()