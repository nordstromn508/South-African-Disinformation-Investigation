"""
main.py
    Main thread of execution

    @author: Nicholas Nordstrom
"""

import data_loader
import analysis


def main():
    """
    Main thread of execution
    :return: 0 if no error, non-zero otherwise
    """

    dataset = data_loader.read_excel('Data/Dataset.xlsx')
    analysis.VERBOSE = 1
    analysis.analyze(dataset)

    return 0


if __name__ == "__main__":
    main()
