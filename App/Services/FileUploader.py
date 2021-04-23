import os


class FileUploader:
    file_path = None

    def __init__(self, file_path: str) -> None:
        self.file_path = file_path
        self.line_number = 0
        self.line = ""

        self.file = open(self.file_path)

    def open_file(self) -> None:
        pass
        # if(os.path.exists(self.file_path)):
        #     with(open(self.file_path)) as file:
        #         for line in file:
        #             print(line)

    def next(self) -> str:
        return self.file.readline()


