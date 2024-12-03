import psutil
import pathlib
import tempfile


def list_files(directory=tempfile.gettempdir()):
    """list_files should return the list of directories and files hold in directory parameter supplied"""
    directory_path = pathlib.Path(directory)
    print(len(list(directory_path.iterdir())) > 0)


def get_file_content(file=None):
    fd = open(file, "r")
    result = fd.read()
    fd.close()
    return result


def list_process():
    return [psutil.Process(pid).name() for pid in psutil.pids() if pid < 10]


if __name__ == "__main__":
    list_files()
    procs = list_process()
    print(" / ".join(procs))
