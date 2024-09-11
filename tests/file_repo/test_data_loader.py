from myproj.file_repo.file_reader_factory import JsonDataLoader, TextDataLoader
import pytest

class TestDataLoaderPathNotCorrect:
    def test_when_json_path_has_incorrect_extension(self, bad_extension_path):
        with pytest.raises(AttributeError) as e:
            json = JsonDataLoader()
            json.load(bad_extension_path)
        assert 'File has incorrect extension' == str(e.value)

    def test_when_json_file_not_found(self):
        with pytest.raises(FileNotFoundError) as e:
            json = JsonDataLoader()
            json.load('data_test/not_found.json')
        assert str(e.value).startswith('File not found')

    def test_when_text_path_has_incorrect_extension(self, bad_extension_path):
        with pytest.raises(AttributeError) as e:
            txt = TextDataLoader()
            txt.load(bad_extension_path)
        assert 'File has incorrect extension' == str(e.value)

    def test_when_text_file_not_found(self):
        with pytest.raises(FileNotFoundError) as e:
            txt = TextDataLoader()
            txt.load('data_test/not_found.csv')
        assert str(e.value).startswith('File not found')

class TestDataLoaderContentNotCorrect:
    def test_when_csv_file_has_no_content(self, empty_csv_file_path):
        txt = TextDataLoader()
        result = txt.load(empty_csv_file_path)
        assert 0 == len(result)

    def test_when_json_file_has_no_content(self, empty_json_file_path):
        json = JsonDataLoader()
        result = json.load(empty_json_file_path)
        assert 0 == len(result)


    def test_when_csv_file_content_is_present(self, good_csv_file_path):
        txt = TextDataLoader()
        result = txt.load(good_csv_file_path)
        assert 2 == len(result)
        assert result[0].startswith('1')
        assert result[-1].endswith('99')
        assert '\n' not in ''.join(result)

    def test_when_json_file_content_is_present(self, good_json_file_path):
        json = JsonDataLoader()
        result = json.load(good_json_file_path)
        assert 2 == len(result)
        assert result[0].startswith('1')
        assert result[-1].endswith('99')
        assert '\n' not in ''.join(result)