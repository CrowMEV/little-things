from contextlib import contextmanager


class MyOpen:
    def __init__(self, file_path) -> None:
        self.file_path = file_path

    def __enter__(self):
        self.file = open(self.file_path)
        return self

    def __exit__(self, ext_type, ext_val, ext_tb):
        self.file.close()


@contextmanager
def my_open(file_path):
    try:
        file = open(file_path)
        yield file
    finally:
        file.close()
