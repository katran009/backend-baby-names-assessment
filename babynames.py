import sys
import re
from glob import glob


def main():
    # This command-line parsing code is provided.
    # Make a list of command line arguments, omitting the [0] element
    # which is the script itself.
    args = sys.argv[1:]

    if not args:
        print("usage: [--summaryfile] file [file ...]")
        sys.exit(1)

    # Notice the summary flag and remove it from args if it is present.
    summary = False

    if args[0] == '--summaryfile':
        summary = True
        del args[0]

    # +++your code here+++
    # For each filename, get the names, then either print the text output
    # or write it to a summary file
    files = glob(args[0])

    for file in files:
        matches = linearize(extract_names(file))

        if summary:
            filename = file + ".summary"

            summary_file = open(filename, "w")
            summary_file.write(matches)
            print(filename)
        else:
            print(matches)


def linearize(match):
    """
    Given a list it, return a string separated by a new line
    2006
    Aaliyah 91
    Aaron 57
    Abagail 895
    """
    return '\n'.join(match)


def extract_names(filename):

    """
    Given a file name for baby.html, returns a list starting with
    the year string
    followed by the name-rank strings in alphabetical order.
    ['2006', 'Aaliyah 91', Aaron 57', 'Abagail 895', ' ...]
    """
    # +++your code here+++
    frequency = []
    names = {}

    for line in open(filename):
        rank_male_female = re.findall
        ("<td>(/d*)</td><td>(/S*?)</td><td>(/S*?)</td>", line)
        # since each line in html file is not of <td></td> format some tuples
        # will be empty but if not then
        if rank_male_female:
            # register male and female rank
            rank = rank_male_female[0][0]
            male = rank_male_female[0][1]
            female = rank_male_female[0][2]

            names[male] = rank
            names[female] = rank

        # while we are checking each line let's get the year value
        year = re.findall('Popularity in (/d*)', line)
        if year:
            frequency.append(year[0])

    for v, k in names.items():
        frequency.append(v + " " + k)

    return sorted(frequency)


if __name__ == '__main__':
    main()
