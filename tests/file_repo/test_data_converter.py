from myproj.file_repo.file_reader_factory import JsonData, TextData, ToTextDataConverter, ToJsonDataConverter
import pytest


def test_text_converter_works_correct():
    to_text_converter = ToTextDataConverter()
    result_to_text_converter = to_text_converter.convert(['Alicja,13,Poznan', 'Kazimierz,22,Warszawa'])
    assert TextData([['Alicja','13','Poznan'],['Kazimierz','22','Warszawa']]) == result_to_text_converter
    assert isinstance(result_to_text_converter, TextData)


def test_json_converter_works_correct():
    to_json_converter = ToJsonDataConverter()
    result_to_json_converter = to_json_converter.convert(['Alicja,13,Poznan', 'Kazimierz,22,Warszawa'])
    assert JsonData({0:['Alicja','13','Poznan'],1:['Kazimierz','22','Warszawa']}) == result_to_json_converter
    assert isinstance(result_to_json_converter, JsonData)