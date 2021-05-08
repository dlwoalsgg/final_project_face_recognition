from contextlib import contextmanager
import tempfile
import os


@contextmanager
def atomic_write(file, mode="w", as_file=True, **kwargs):
    """Write a file atomically

    :param file: str or :class:`os.PathLike` target to write

    :param bool as_file:  if True, the yielded object is a :class:File.
        (eg, what you get with `open(...)`).  Otherwise, it will be the
        temporary file path string

    :param kwargs: anything else needed to open the file

    :raises: FileExistsError if target exists

    Example::

        with atomic_write("hello.txt") as f:
            f.write("world!")

    """
    if os.path.exists(file):
        raise FileExistsError

    # initialize flag variable with default set to False, if write is successful will change to True
    write_successful = False
    try:
        filename, file_extension = os.path.splitext(file)
        # Uses tempfile module to create temporary file
        # Default temporary file folders have to be on same filesystem for rename operation to be atomic
        with tempfile.NamedTemporaryFile(
            mode=mode, suffix=file_extension, delete=False
        ) as fo:
            if as_file:
                yield fo
            else:
                yield fo.name

        # rename temp to target and change flag to True if write operation completed successfully
        os.rename(fo.name, file)
        write_successful = True

    finally:
        # Delete temporary and target file if writing code fails
        if not write_successful:
            if os.path.exists(fo.name):
                os.remove(fo.name)
            if os.path.exists(file):
                os.remove(file)
