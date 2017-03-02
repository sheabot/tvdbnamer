import os


class FileFinder(object):

    def __init__(self, config):
        # Parse config
        self._config = config
        try:
            self._valid_file_extensions = self._config['valid_file_extensions']
            self._filename_blacklist = self._config['filename_blacklist']
        except:
            raise Exception('Failed to parse config')

    def find_all_files(self, paths, recursive=False):
        valid_files = []
        for path in paths:
            if os.path.isfile(path):
                path = os.path.abspath(path)
                if self._is_filename_valid(path):
                    return valid_files.append(path)
                else:
                    continue
            elif os.path.isdir(path):
                valid_files += self._find_files_in_dir(path, recursive)
            else:
                raise Exception("%s is not a valid file/directory" % path)
        # Return list of valid files with duplicates removed
        return list(set(valid_files))

    def _find_files_in_dir(self, path, recursive):
        valid_files = []
        if not recursive:
            for filename in os.listdir(path):
                filepath = os.path.join(path, filename)
                if not os.path.isfile(filepath):
                    continue
                if self._is_filename_valid(filepath):
                    valid_files.append(filepath)
            return valid_files

        # Recursive
        for root, dirs, files in os.walk(path):
            for filename in files:
                filepath = os.path.join(root, filename)
                if self._is_filename_valid(filepath):
                    valid_files.append(filepath)
        return valid_files

    def _is_filename_valid(self, path):
        return (
            self._is_extension_valid(path)
            and not self._is_filename_blacklisted(path)
        )

    def _is_extension_valid(self, path):
        if len(self._valid_file_extensions) == 0:
            # All file extensions are valid
            return True

        # Get extension and remove period
        _, extension = os.path.splitext(path)
        extension = extension[1:]
        if not extension:
            # File has no extension
            return False

        # Validate extension
        return extension in self._valid_file_extensions

    def _is_filename_blacklisted(self, path):
        # TODO: Implement this
        return False
