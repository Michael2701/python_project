# TODO Translate this file to C file according:
# https://stackoverflow.com/questions/5081875/ctypes-beginner
import os
from typing import Any


class InterferenceCreator:
    keys_list = ['AAA', 'AAB', 'AAH', 'ABA', 'ABB', 'ABH', 'AHA', 'AHB', 'AHH',
                 'BAA', 'BAB', 'BAH', 'BBA', 'BBB', 'BBH', 'BHA', 'BHB', 'BHH',
                 'HAA', 'HAB', 'HAH', "HBA", "HBB", 'HBH', 'HHA', 'HHB', 'HHH']

    def __init__(self, master: Any = None) -> None:
        self.file_path = "App/triplet_of_genes.csv"
        pass

    def count_N_xx(self):
        """
        count N_xx
        :return:
        """
        marker_differences = []
        N_00 = 0
        N_01 = 0
        N_10 = 0
        N_11 = 0

        if os.path.exists(self.file_path):
            with open(self.file_path) as file:
                for i, line in enumerate(file):
                    if i > 0:
                        split_line = line.split(',')
                        for j, chunk in enumerate(split_line):
                            if j == 5:
                                try:
                                    marker_differences.append([
                                        float(split_line[4]) - float(split_line[3]),
                                        float(split_line[5]) - float(split_line[4])
                                    ])
                                except Exception as e:
                                    print(e)

                            if j > 5:
                                try:
                                    # === COUNTERS ===

                                    # N_00: AAA, BBB
                                    if j == 3 or j == 16:
                                        N_00 += float(chunk)

                                    # N_10: ABB, BAA
                                    if j == 7 or j == 12:
                                        N_10 += float(chunk)

                                    # N_01
                                    if j == 4 or j == 12:  # AAB, BBA
                                        N_01 += float(chunk)

                                    # N_11: ABA, BAB
                                    if j == 6 or j == 13:
                                        N_11 += float(chunk)

                                    # === DISTRIBUTION ===

                                    # AAH, BBH: 00, 01
                                    if j == 5 or j == 17:
                                        N_01 += float(chunk) / 2
                                        N_00 += float(chunk) / 2

                                    # HAA, HBB: 00, 10
                                    if j == 21 or j == 25:
                                        N_00 += float(chunk) / 2
                                        N_10 += float(chunk) / 2

                                    # ABH, BAH: 10, 11
                                    if j == 8 or j == 14:
                                        N_10 += float(chunk) / 2
                                        N_11 += float(chunk) / 2

                                    # AHA, BHB: 00, 11
                                    if j == 9 or j == 19:
                                        N_11 += float(chunk) / 2
                                        N_00 += float(chunk) / 2

                                    # AHB, BHA: 01, 10
                                    if j == 10 or j == 18:
                                        N_01 += float(chunk) / 2
                                        N_10 += float(chunk) / 2

                                    # HAB, HBA: 01, 11
                                    if j == 22 or j == 24:
                                        N_01 += float(chunk) / 2
                                        N_11 += float(chunk) / 2

                                    # HAH, HBH:  00, 01, 11
                                    if j == 23 or j == 26:
                                        N_00 += float(chunk) / 4
                                        N_01 += float(chunk) / 4
                                        N_11 += float(chunk) / 4

                                    # AHH, BHH, HHA, HHB: 00, 01, 10, 11
                                    if j == 11 or j == 20 or j == 21 or j == 28:
                                        N_00 += float(chunk) / 4
                                        N_01 += float(chunk) / 4
                                        N_10 += float(chunk) / 4
                                        N_11 += float(chunk) / 4

                                    # HHH: 00, 01, 10, 11
                                    if j == 29:
                                        N_00 += float(chunk) / 8
                                        N_01 += float(chunk) / 8
                                        N_10 += float(chunk) / 8
                                        N_11 += float(chunk) / 8
                                except Exception as e:
                                    print(e)

        print([N_00, N_01, N_10, N_11])
        print(marker_differences)
















