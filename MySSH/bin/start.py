import os
import sys

BASE_DIR = os.path.normpath(os.path.join(
    os.path.abspath(__file__),
    os.pardir,
    os.pardir
))
sys.path.append(BASE_DIR)

if __name__ == '__main__':
    from core.src import run
    run()