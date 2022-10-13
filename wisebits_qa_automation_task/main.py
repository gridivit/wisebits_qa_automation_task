import os
import pathlib

import pytest

current_path = pathlib.Path(__file__).parent.resolve()
os.chdir(current_path)

def main():
    pytest.main()


if __name__ == "__main__":
    main()
