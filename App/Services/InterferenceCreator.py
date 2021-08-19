# TODO Translate this file to C file according:
# https://stackoverflow.com/questions/5081875/ctypes-beginner


# import os
# from typing import Any
#
#
# class InterferenceCreator:
#     keys_list = ['AAA', 'AAB', 'AAH', 'ABA', 'ABB', 'ABH', 'AHA', 'AHB', 'AHH',
#                  'BAA', 'BAB', 'BAH', 'BBA', 'BBB', 'BBH', 'BHA', 'BHB', 'BHH',
#                  'HAA', 'HAB', 'HAH', "HBA", "HBB", 'HBH', 'HHA', 'HHB', 'HHH']
#
#     def __init__(self, master: Any = None) -> None:
#         self.file_path = "App/file.csv"
#         pass
#
#     def count_N_xx(self):
#         """
#         count N_xx
#         :return:
#         """
#         triple_gene_name = ''
#         N_00 = 0
#         N_01 = 0
#         N_10 = 0
#         N_11 = 0
#
#         if os.path.exists(self.file_path):
#             with open(self.file_path) as file:
#                 for i, line in enumerate(file):
#                     if i > 0:
#                         split_line = line.split(',')
#
#                         for j in split_line:
#                             if j == 0:
#                                 triple_gene_name = j[0] + j[1] + j[2]  # saving markers name
#
#                             if j > 2:
#                                 if j == 3:  # AAA
#                                     N_00 += float(j)
#                                 if j == 4:  # AAB
#                                     N_01 += float(j)
#                                 if j == 5:  # AAH
#                                     N_01 += float(j) / 2
#                                     N_00 += float(j) / 2
#                                 if j == 6:  # ABA
#                                     N_11 += float(j)
#                                 if j == 7:  # ABB
#                                     N_10 += float(j)
