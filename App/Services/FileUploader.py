import os
from App.Models.GeneModel import GeneModel 

class FileUploader:
    file_path = None

    def __init__(self, file_path: str, file_id: str) -> None:
        self.file_id = file_id
        self.file_path = file_path
        self.line_number = 0
        self.line = ""

        self.file = open(self.file_path)

    def upload_file(self) -> None:
        if os.path.exists(self.file_path):
            with(open(self.file_path)) as file:
                for i, line in enumerate(file):
                    if i > 0:
                        splited_line = line.split(',,')
                        GeneModel(
                            file_id=self.file_id,
                            name=splited_line[1],
                            distance=splited_line[0],
                            successors=splited_line[2]
                        )

    def next(self) -> str:
        return self.file.readline()


