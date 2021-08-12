from io import BytesIO
from typing import Dict, List, Any
import concurrent.futures


class AbstractMapReduce:

    __slots__ = ["metadata", "output_path"]

    def __init__(self, metadata: Dict[str, Any], output_file: str):
        self.output_path = output_file

    def partition(self, input_stream: BytesIO) -> BytesIO:
        raise NotImplementedError()

    def map(self, input_stream: BytesIO) -> BytesIO:
        raise NotImplementedError()

    def reduce(self, input_stream: List[BytesIO], output_stream: BytesIO):
        raise NotImplementedError()

    def run(self, input_file):
        with open(input_file, "rb") as file:
            input_data = BytesIO(file.read())

        mapped_data = []
        for part in self.partition(input_data):
            data = self.map(part)
            mapped_data.append(data)

        output = BytesIO()
        self.reduce(mapped_data, output)

        with open(self.output_path, "w") as file:
            file.write(output.getvalue().decode("UTF-8"))
