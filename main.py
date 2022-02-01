"""
main.py
    Main thread of execution

    @author: Nicholas Nordstrom
"""

import data_loader


def main():
    """
    Main thread of execution
    :return: 0 if no error, non-zero otherwise
    """

    dataset = data_loader.read_excel('Data/Dataset.xlsx')

    return 0


if __name__ == "__main__":
    main()
