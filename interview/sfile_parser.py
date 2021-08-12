import io
from pydantic import BaseModel

from MapReduce.map_reduce import AbstractMapReduce


class metadata_dto(BaseModel):
    pass


class SFileParser(AbstractMapReduce):
    def __init__(self, metadata, output_file):
        pass

    def partition(self, input_stream):
        pass

    def map(self, input_stream):
        pass

    def reduce(self, input_stream, output_stream):
        pass


if __name__ == "__main__":
    mr = SFileParser({}, "parsed_sfile")
    mr.run("P2020sfile.txt")
