import os
from App.Models.GeneModel import GeneModel 


class FileUploader:
    file_path = None

    def __init__(self, file_path: str, file_id: str) -> None:
        """
        
        :param file_path: Files path in OS 
        :param file_id: 
        """
        self.file_id = file_id
        self.file_path = file_path
        self.line_number = 0
        self.line = ""

        self.file = open(self.file_path)

    def upload_file(self) -> None:
        """
        send lines of Gene from file to GeneModel
        :return: None
        """
        if os.path.exists(self.file_path):
            with(open(self.file_path)) as file:
                for i, line in enumerate(file):
                    if i > 0:
                        split_line = line.split(',,')
                        GeneModel(
                            file_id=self.file_id,
                            name=split_line[1],
                            distance=split_line[0],
                            successors=split_line[2]
                        )

    def next(self) -> str:
        return self.file.readline()
