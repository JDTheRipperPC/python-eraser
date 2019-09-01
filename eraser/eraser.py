import csv
import os
import logging
import shutil
import time

LOGGER = logging.getLogger(__name__)


class EraserStats:

    error_files = []
    error_directories = []

    def append_file(self, path):
        LOGGER.error('Error file: {}'.format(path))
        self.error_file.append(path)

    def append_directory(self, path):
        LOGGER.error('Error directory: {}'.format(path))
        self.error_directories.append(path)

    def clean(self):
        self.error_files = []
        self.error_directories = []

    def load_csv(self, path):
        with open(path) as csvfile:
            reader = csv.reader(csvfile)
            for row in csv_reader:
                if row[0] == 'file':
                    self.error_files.append(row[1])
                else:
                    self.error_directories.append(row[1])

    def save_csv(self, path):
        with open(path, 'w') as csvfile:
            writer = csv.writer(csvfile)
            for efile in self.error_files:
                writer.writerow(['file', efile])
            for edirectory in self.error_directories:
                writer.writerow(['directory', edirectory])

    def __str__(self):
        return 'Eraser Stats:\nError files: {}\nError directories: {}'.format(
            len(self.error_files), len(self.error_directories))


class Eraser:

    files = []
    directories = []
    stats = {
        'files_error': [],
        'dirs_error': [],
    }

    def targets(self, targets):
        """Load targets to the files and directories lists."""
        for target in targets:
            if os.path.isfile(target):
                self.files.append(target)
            else:
                self.directories.append(target)

    def _rmtree_onerror(self, function, path, excinfo):
        LOGGER.error('Error erasing path: "{}"'.format(path))
        LOGGER.error('Error function: {}'.format(function))
        LOGGER.error('Error excinfo:  {}'.format(excinfo))
        self.stats['dirs_error'].append(path)

    def _erase_file(self):
        for f in self.files:
            LOGGER.info('Erasing file: "{}" ...'.format(f))
            try:
                os.remove(f)
                self.files.pop(f)
            except:  # TODO: specify the exception
                LOGGER.error('Error erasing file: "{}"'.format(f))
                pass

    def _erase_dir(self):
        for dir in self.directories:
            shutil.rmtree(dir, onerror=self._rmtree_onerror)

    def erase(self):
        self._erase_file()
        self._erase_dir()
