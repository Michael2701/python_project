import csv
from os import path


class FileHelper:

    @staticmethod
    def read_csv(file_path: str) -> list:
        """
        read csv file into list of dicts
        :param file_path:string path to file
        :return: list of dicts
        """
        result = []

        if path.exists(file_path) and path.isfile(file_path):
            with open(file_path, 'r', newline='') as csv_file:
                reader = csv.DictReader(csv_file)

                for row in reader:
                    result.append(row)

        return result

    @staticmethod
    def write_csv(file_path: str, data: list, field_names: list) -> bool:
        """
        write list of dicts in csv format
        :param file_path: string
        :param data: list of dicts
        :param field_names: list of strings column names
        :return: True on success and False otherwise
        """
        if path.exists(file_path) and path.isfile(file_path):
            try:
                with open(file_path, 'w', newline='') as csv_file:
                    writer = csv.DictWriter(csv_file, fieldnames=field_names)
                    writer.writeheader()

                    for row in data:
                        writer.writerow(row)
                return True
            except Exception as e:
                print(e)
        return  False
