import os
from contextlib import contextmanager
from typing import ContextManager, Union
import tempfile

@contextmanager
def atomic_write(
    file: Union[str, os.PathLike], mode: str = "w", as_file: bool = True, **kwargs
) -> ContextManager:
    #   check if the file exists
    if os.path.exists(file):
        raise FileExistsError

    #    flag to verify whether the conversion works
    convertSuccess = False
    #   try to convert file format
    try:
        # for extension
        fileChuckList = os.path.splitext(file)
        # last elem of the list is the extension
        extension = fileChuckList[-1]
        # as file, return file. Otherwise, return filename str
        with tempfile.NamedTemporaryFile(mode=mode, suffix=extension, delete=False) as f:
            if as_file:
                yield f
            else:
                yield f.name
        # rename the temp file to final output file name
        print(f.name)
        print(file)
        os.rename(f.name,file)
        # change the flag to True since the process has been succeeded
        convertSuccess = True
        print("conversion success!!")
    # finally, the temp file has to be removed if the conversion process has been failed.
    finally:
        # if the conversion has been failed
        if convertSuccess == False:
            # remove the incomplete temp files
            f.close()
            os.path.exists(f.name) and os.remove(f.name)
            # os.path.exists(f) and os.remove(f)
            print("temp file removed!")

    """Write a file atomically

    :param file: str or :class:`os.PathLike` target to write
    :param mode: the mode in which the file is opened, defaults to "w" (writing in text mode)
    :param bool as_file:  if True, the yielded object is a :class:File.
        (eg, what you get with `open(...)`).  Otherwise, it will be the
        temporary file path string

    :param kwargs: anything else needed to open the file

    :raises: FileExistsError if target exists

    Example::

        with atomic_write("hello.txt") as f:
            f.write("world!")

    """
    # raise NotImplementedError()
