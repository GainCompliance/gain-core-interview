import io
from pydantic import BaseModel

from MapReduce.map_reduce import AbstractMapReduce


class metadata_dto(BaseModel):
    padding: str


"""
This is an example of how to use the AbstractMapReduce class.

This particular example takes a file containing text and adds
buffer text defined in the metadata_dto to the beginning and ending 
of every line.
"""


class ExampleMapReducer(AbstractMapReduce):
    def __init__(self, metadata, output):
        super().__init__(metadata, output)
        self.metadata = metadata_dto(**metadata)

    def partition(self, input_stream):
        for line in input_stream.getvalue().decode("UTF-8").split("\n"):
            yield io.BytesIO(line.strip().encode("UTF-8"))

    def map(self, input_stream):
        return io.BytesIO(
            f"{self.metadata.padding}{input_stream.getvalue().decode('UTF-8')}{self.metadata.padding}\n".encode("UTF-8")
        )

    def reduce(self, input_stream, output_stream):
        for input_data in input_stream:
            output_stream.write(input_data.getvalue())
            output_stream.flush()


if __name__ == "__main__":
    mr = ExampleMapReducer({"padding": " # "}, "example_out")
    mr.run("example.txt")
