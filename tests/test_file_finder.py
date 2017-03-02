import os

from tvdbnamer.lib import FileFinder
from .base import TVDBNamerTestCase


class TestFileFinder(TVDBNamerTestCase):

    dummy_files = [
        'video.file.avi',
        'video.file.mkv',
        'video.file.mp4',
        'video.file.mpeg',
        'random.file.blah',
        'noextension',
        'video.file2.avi',
        'not.actually.avi.a.video.file',
        'music.file.mp3',
        'music.file.aac',
        'path/to/file',
        'path/to/video/file.avi',
        'path/to/video.file.mp4',
        'different/path/to/video.file.mkv',
    ]

    config = {
        'valid_file_extensions': [],
        'filename_blacklist': []
    }

    def test_valid_file_extensions_empty(self):
        config = dict(self.config)
        finder = FileFinder(config)
        files = finder.find_all_files([self.tmpdir])

        expected_files = [
            'video.file.avi',
            'video.file.mkv',
            'video.file.mp4',
            'video.file.mpeg',
            'random.file.blah',
            'noextension',
            'video.file2.avi',
            'not.actually.avi.a.video.file',
            'music.file.mp3',
            'music.file.aac'
        ]

        self._assert_files_equal(files, expected_files)

    def test_valid_file_extensions_empty_recursive(self):
        config = dict(self.config)
        finder = FileFinder(config)
        files = finder.find_all_files([self.tmpdir], recursive=True)

        expected_files = [
            'video.file.avi',
            'video.file.mkv',
            'video.file.mp4',
            'video.file.mpeg',
            'random.file.blah',
            'noextension',
            'video.file2.avi',
            'not.actually.avi.a.video.file',
            'music.file.mp3',
            'music.file.aac',
            'path/to/file',
            'path/to/video/file.avi',
            'path/to/video.file.mp4',
            'different/path/to/video.file.mkv',
        ]

        self._assert_files_equal(files, expected_files)

    def test_valid_file_extensions_video(self):
        config = dict(self.config)
        config['valid_file_extensions'] = [
            'avi', 'mkv', 'mp4'
        ]
        finder = FileFinder(config)
        files = finder.find_all_files([self.tmpdir])

        expected_files = [
            'video.file.avi',
            'video.file.mkv',
            'video.file.mp4',
            'video.file2.avi'
        ]

        self._assert_files_equal(files, expected_files)

    def test_valid_file_extensions_video_recursive(self):
        config = dict(self.config)
        config['valid_file_extensions'] = [
            'avi', 'mkv', 'mp4'
        ]
        finder = FileFinder(config)
        files = finder.find_all_files([self.tmpdir], recursive=True)

        expected_files = [
            'video.file.avi',
            'video.file.mkv',
            'video.file.mp4',
            'video.file2.avi',
            'path/to/video/file.avi',
            'path/to/video.file.mp4',
            'different/path/to/video.file.mkv'
        ]

        self._assert_files_equal(files, expected_files)

    def test_valid_file_extensions_audio(self):
        config = dict(self.config)
        config['valid_file_extensions'] = [
            'aac', 'mp3'
        ]
        finder = FileFinder(config)
        files = finder.find_all_files([self.tmpdir])

        expected_files = [
            'music.file.mp3',
            'music.file.aac'
        ]

        self._assert_files_equal(files, expected_files)

    def _assert_files_equal(self, actual, expected):
        for i, filename in enumerate(expected):
            expected[i] = os.path.join(self.tmpdir, filename)
        self.assertItemsEqual(actual, expected)
