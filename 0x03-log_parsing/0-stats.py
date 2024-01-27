#!/usr/bin/python3

"""
Module that contains script that reads stdin line and computes metrics.
For every 10 lines:
    - print the status code and the number of times it appears
    - print the sum of the files sizes
"""
import sys  # for sys.stdin


if __name__ == '__main__':  # if this is the main module

    c = fileSize = 0  # initialize counters and file size to 0
    statCount = {  # initialize a dictionary to store the status code and count
        '200': 0, '301': 0, '400': 0, '401': 0,
        '403': 0, '404': 0, '405': 0, '500': 0
    }

    # handle input from stdin line by line
    def handle_input(statCount, fileSize):
        print('File size: {}'.format(fileSize))
        for key in sorted(statCount.keys()):
            if statCount[key] == 0:
                continue
            # print status code and number of times it appears
            print('{}: {}'.format(key, statCount[key]))

    try:  # read stdin line by line and compute metrics
        for line in sys.stdin:
            c += 1
            split = line.split(" ")  # split line by space
            try:
                # get status code and convert to int if possible
                status = split[-2]
                # get file size and convert to int if possible
                fileSize += int(split[-1])

                if status in statCount:
                    statCount[status] += 1
            # if any exception occurs, ignore the line and continue
            except Exception:
                pass

            if c % 10 == 0:  # handle every 10 lines
                handle_input(statCount, fileSize)

        else:  # handle last 10 lines if there are less than 10 lines
            handle_input(statCount, fileSize)
    # handle keyboard interrupt and system exit
    except (KeyboardInterrupt, SystemExit):
        handle_input(statCount, fileSize)
        raise  # raise exception to exit program
