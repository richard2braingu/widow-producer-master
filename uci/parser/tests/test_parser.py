"""
Tests for the public classes in `uci.parser.parser.py`
"""
import os

from lxml.etree import XMLSyntaxError

from uci import XMLParser


class TestXMLParserAgainstExamples:
    """
    Given a collection of example XML string byte objects
    When we parse each object
    Then we should receive an object and no error
    """

    # Setup
    example_directory = os.path.join(os.path.dirname(__file__), "example_xml")
    uci_parser = XMLParser()

    def get_example_filepath(self, filename):
        """
        Small helper function to retrieve the example files directory
        """
        return os.path.join(self.example_directory, filename)

    def test_example_directory_should_exist(self):
        """
        Setup test to ensure that the example files directory exists
        """
        # Setup
        assert os.path.exists(self.example_directory), (
            f"{self.example_directory} does not exist."
            "It is required for subsequent tests against example files."
        )

    def test_parser_should_validate_position_report_example(self):
        """
        Given an example file 'positionReportExample.xml'
        When we pass the bytes string to XMLParser.parse_object
        Then we should receive no exception
        """
        filepath = self.get_example_filepath("positionReportExample.xml")
        assert os.path.exists(filepath), f"Unable to find {filepath}"
        try:
            with open(filepath, "rb") as file:
                self.uci_parser.parse_object(file.read())
        except FileNotFoundError as file_not_found_error:
            assert False, f"Unable to find file {filepath}\n{file_not_found_error}"
        except XMLSyntaxError as xml_syntax_error:
            assert False, (
                f"Unable parse file {filepath}\nFailed schema validation.\n" f"{xml_syntax_error}"
            )

    def test_parser_should_validate_sub_system_configuration_example(self):
        """
        Given an example file 'subSystemConfigurationExample.xml'
        When we pass the bytes string to XMLParser.parse_object
        Then we should receive no exception
        """
        filepath = self.get_example_filepath("subSystemConfigurationExample.xml")
        assert os.path.exists(filepath), f"Unable to find {filepath}"
        try:
            with open(filepath, "rb") as file:
                self.uci_parser.parse_object(file.read())
        except FileNotFoundError as file_not_found_error:
            assert False, f"Unable to find file {filepath}\n{file_not_found_error}"
        except XMLSyntaxError as xml_syntax_error:
            assert False, (
                f"Unable parse file {filepath}\nFailed schema validation.\n" f"{xml_syntax_error}"
            )

    def test_parser_should_validate_task_string_example(self):
        """
        Given an example file 'taskStrikeExample.xml'
        When we pass the bytes string to XMLParser.parse_object
        Then we should receive no exception
        """
        filepath = self.get_example_filepath("taskStrikeExample.xml")
        assert os.path.exists(filepath), f"Unable to find {filepath}"
        try:
            with open(filepath, "rb") as file:
                self.uci_parser.parse_object(file.read())
        except FileNotFoundError as file_not_found_error:
            assert False, f"Unable to find file {filepath}\n{file_not_found_error}"
        except XMLSyntaxError as xml_syntax_error:
            assert False, (
                f"Unable parse file {filepath}\nFailed schema validation.\n" f"{xml_syntax_error}"
            )

    def test_parser_should_validate_mission_plan_example(self):
        """
        Given an example file 'missionPlanExample.xml'
        When we pass the bytes string to XMLParser.parse_object
        Then we should receive no exception
        """
        filepath = self.get_example_filepath("missionPlanExample.xml")
        assert os.path.exists(filepath), f"Unable to find {filepath}"
        try:
            with open(filepath, "rb") as file:
                self.uci_parser.parse_object(file.read())
        except FileNotFoundError as file_not_found_error:
            assert False, f"Unable to find file {filepath}\n{file_not_found_error}"
        except XMLSyntaxError as xml_syntax_error:
            assert False, (
                f"Unable parse file {filepath}\nFailed schema validation.\n" f"{xml_syntax_error}"
            )

    def test_parser_should_validate_amti_example(self):
        """
        Given an example file 'amtiExample.xml'
        When we pass the bytes string to XMLParser.parse_object
        Then we should receive no exception
        """
        filepath = self.get_example_filepath("amtiExample.xml")
        assert os.path.exists(filepath), f"Unable to find {filepath}"
        try:
            with open(filepath, "rb") as file:
                self.uci_parser.parse_object(file.read())
        except FileNotFoundError as file_not_found_error:
            assert False, f"Unable to find file {filepath}\n{file_not_found_error}"
        except XMLSyntaxError as xml_syntax_error:
            assert False, (
                f"Unable parse file {filepath}\nFailed schema validation.\n" f"{xml_syntax_error}"
            )

    def test_parser_should_validate_route_plan_example(self):
        """
        Given an example file 'routePlanExample.xml'
        When we pass the bytes string to XMLParser.parse_object
        Then we should receive no exception
        """
        filepath = self.get_example_filepath("routePlanExample.xml")
        assert os.path.exists(filepath), f"Unable to find {filepath}"
        try:
            with open(filepath, "rb") as file:
                self.uci_parser.parse_object(file.read())
        except FileNotFoundError as file_not_found_error:
            assert False, f"Unable to find file {filepath}\n{file_not_found_error}"
        except XMLSyntaxError as xml_syntax_error:
            assert False, (
                f"Unable parse file {filepath}\nFailed schema validation.\n" f"{xml_syntax_error}"
            )

    def test_parser_should_validate_smti_example(self):
        """
        Given an example file 'smtiExample.xml'
        When we pass the bytes string to XMLParser.parse_object
        Then we should receive no exception
        """
        filepath = self.get_example_filepath("smtiExample.xml")
        assert os.path.exists(filepath), f"Unable to find {filepath}"
        try:
            with open(filepath, "rb") as file:
                self.uci_parser.parse_object(file.read())
        except FileNotFoundError as file_not_found_error:
            assert False, f"Unable to find file {filepath}\n{file_not_found_error}"
        except XMLSyntaxError as xml_syntax_error:
            assert False, (
                f"Unable parse file {filepath}\nFailed schema validation.\n" f"{xml_syntax_error}"
            )

    def test_parser_should_validate_strike_example(self):
        """
        Given an example file 'strikeExample.xml'
        When we pass the bytes string to XMLParser.parse_object
        Then we should receive no exception
        """
        filepath = self.get_example_filepath("strikeExample.xml")
        assert os.path.exists(filepath), f"Unable to find {filepath}"
        try:
            with open(filepath, "rb") as file:
                self.uci_parser.parse_object(file.read())
        except FileNotFoundError as file_not_found_error:
            assert False, f"Unable to find file {filepath}\n{file_not_found_error}"
        except XMLSyntaxError as xml_syntax_error:
            assert False, (
                f"Unable parse file {filepath}\nFailed schema validation.\n" f"{xml_syntax_error}"
            )

    def test_parser_should_validate_system_status_example(self):
        """
        Given an example file 'systemStatusExample.xml'
        When we pass the bytes string to XMLParser.parse_object
        Then we should receive no exception
        """
        filepath = self.get_example_filepath("systemStatusExample.xml")
        assert os.path.exists(filepath), f"Unable to find {filepath}"
        try:
            with open(filepath, "rb") as file:
                self.uci_parser.parse_object(file.read())
        except FileNotFoundError as file_not_found_error:
            assert False, f"Unable to find file {filepath}\n{file_not_found_error}"
        except XMLSyntaxError as xml_syntax_error:
            assert False, (
                f"Unable parse file {filepath}\nFailed schema validation.\n" f"{xml_syntax_error}"
            )

    def test_parser_should_validate_position_report(self):
        """
        Given an example file 'position_report.xml'
        When we pass the bytes string to XMLParser.parse_object
        Then we should receive no exception
        """
        filepath = self.get_example_filepath("position_report.xml")
        assert os.path.exists(filepath), f"Unable to find {filepath}"
        try:
            with open(filepath, "rb") as file:
                self.uci_parser.parse_object(file.read())
        except FileNotFoundError as file_not_found_error:
            assert False, f"Unable to find file {filepath}\n{file_not_found_error}"
        except XMLSyntaxError as xml_syntax_error:
            assert False, (
                f"Unable parse file {filepath}\nFailed schema validation.\n" f"{xml_syntax_error}"
            )

    def test_parser_should_validate_op_zone_shape_example(self):
        """
        Given an example file 'opZoneShapeExample.xml'
        When we pass the bytes string to XMLParser.parse_object
        Then we should receive no exception
        """
        filepath = self.get_example_filepath("opZoneShapeExample.xml")
        assert os.path.exists(filepath), f"Unable to find {filepath}"
        try:
            with open(filepath, "rb") as file:
                self.uci_parser.parse_object(file.read())
        except FileNotFoundError as file_not_found_error:
            assert False, f"Unable to find file {filepath}\n{file_not_found_error}"
        except XMLSyntaxError as xml_syntax_error:
            assert False, (
                f"Unable parse file {filepath}\nFailed schema validation.\n" f"{xml_syntax_error}"
            )

    def test_parser_should_validate_task_example(self):
        """
        Given an example file 'taskExample.xml'
        When we pass the bytes string to XMLParser.parse_object
        Then we should receive no exception
        """
        filepath = self.get_example_filepath("taskExample.xml")
        assert os.path.exists(filepath), f"Unable to find {filepath}"
        try:
            with open(filepath, "rb") as file:
                self.uci_parser.parse_object(file.read())
        except FileNotFoundError as file_not_found_error:
            assert False, f"Unable to find file {filepath}\n{file_not_found_error}"
        except XMLSyntaxError as xml_syntax_error:
            assert False, (
                f"Unable parse file {filepath}\nFailed schema validation.\n" f"{xml_syntax_error}"
            )

    def test_parser_should_validate_strike_capability_status_example(self):
        """
        Given an example file 'strikeCapabilityStatusExample.xml'
        When we pass the bytes string to XMLParser.parse_object
        Then we should receive no exception
        """
        filepath = self.get_example_filepath("strikeCapabilityStatusExample.xml")
        assert os.path.exists(filepath), f"Unable to find {filepath}"
        try:
            with open(filepath, "rb") as file:
                self.uci_parser.parse_object(file.read())
        except FileNotFoundError as file_not_found_error:
            assert False, f"Unable to find file {filepath}\n{file_not_found_error}"
        except XMLSyntaxError as xml_syntax_error:
            assert False, (
                f"Unable parse file {filepath}\nFailed schema validation.\n" f"{xml_syntax_error}"
            )

    def test_parser_should_validate_op_zone_polygon_example(self):
        """
        Given an example file 'opZonePolygonExample.xml'
        When we pass the bytes string to XMLParser.parse_object
        Then we should receive no exception
        """
        filepath = self.get_example_filepath("opZonePolygonExample.xml")
        assert os.path.exists(filepath), f"Unable to find {filepath}"
        try:
            with open(filepath, "rb") as file:
                self.uci_parser.parse_object(file.read())
        except FileNotFoundError as file_not_found_error:
            assert False, f"Unable to find file {filepath}\n{file_not_found_error}"
        except XMLSyntaxError as xml_syntax_error:
            assert False, (
                f"Unable parse file {filepath}\nFailed schema validation.\n" f"{xml_syntax_error}"
            )

    def test_parser_should_validate_sub_system_status_example(self):
        """
        Given an example file 'subSystemStatusExample.xml'
        When we pass the bytes string to XMLParser.parse_object
        Then we should receive no exception
        """
        filepath = self.get_example_filepath("subSystemStatusExample.xml")
        assert os.path.exists(filepath), f"Unable to find {filepath}"
        try:
            with open(filepath, "rb") as file:
                self.uci_parser.parse_object(file.read())
        except FileNotFoundError as file_not_found_error:
            assert False, f"Unable to find file {filepath}\n{file_not_found_error}"
        except XMLSyntaxError as xml_syntax_error:
            assert False, (
                f"Unable parse file {filepath}\nFailed schema validation.\n" f"{xml_syntax_error}"
            )
