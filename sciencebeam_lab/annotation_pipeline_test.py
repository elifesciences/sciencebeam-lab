import pytest

from sciencebeam_lab.annotation_pipeline import (
  parse_args
)

class TestParseArgs(object):
  def test_should_raise_error_without_arguments(self):
    with pytest.raises(SystemExit):
      parse_args([])

  def test_should_not_raise_error_with_minimum_arguments(self):
    parse_args(['--data-path=test', '--pdf-path=test', '--xml-path=test'])

  def test_should_not_raise_error_with_lxml_path_instead_of_pdf_path(self):
    parse_args(['--data-path=test', '--lxml-path=test', '--xml-path=test'])

  def test_should_raise_error_if_pdf_and_lxml_path_are_specified(self):
    with pytest.raises(SystemExit):
      parse_args(['--data-path=test', '--pdf-path=test', '--lxml-path=test', '--xml-path=test'])

  def test_should_not_raise_error_with_save_lxml_path_together_with_pdf_path(self):
    parse_args(['--data-path=test', '--pdf-path=test', '--save-lxml', '--xml-path=test'])

  def test_should_raise_error_if_save_lxml_specified_without_pdf_path(self):
    with pytest.raises(SystemExit):
      parse_args(['--data-path=test', '--lxml-path=test', '--save-lxml', '--xml-path=test'])