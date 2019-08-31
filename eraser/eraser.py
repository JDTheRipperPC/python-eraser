import os
import logging
import shutil


def erase_file(path):
    try:
        os.remove(path)
    except:
        logging.error("Exception trying to remove the file: {}".format(path))


def erase_dir(path):
    shutil.rmtree(path)

