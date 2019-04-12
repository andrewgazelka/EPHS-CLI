#!/bin/env python3

import datetime

from prettytable import PrettyTable


def get_info():
    today = datetime.datetime.today()
    weekday = today.weekday()
    if weekday in {0, 2, 3, 4}:
        return {
            "1st": {
                "range": ("7:50", "9:18")
            },
            "2nd": {
                "range": ("9:25", "10:53")
            },
            "3rd": {
                "range": ("11:00", "1:00")
            },
            "4th": {
                "range": ("1:08", "2:35")
            }
        }
    elif weekday == 1:  # Tuesday
        return {
            "0": {
                "range": ("7:15", "8:15")
            },
            "1st": {
                "range": ("8:20", "9:33")
            },
            "Connections": {
                "range": ("9:40", "10:00")
            },
            "2nd": {
                "range": ("10:07", "11:21")
            },
            "3rd": {
                "range": ("11:28", "1:16")
            },
            "4th": {
                "range": ("1:22", "2:35")
            }
        }


if __name__ == "__main__":
    info = get_info()
    table = PrettyTable(['Period', 'Start', 'End'], border=False, header=True)
    for k, v in info.items():
        time_range = v["range"]
        table.add_row([k, time_range[0], time_range[1]])
    print(table)
