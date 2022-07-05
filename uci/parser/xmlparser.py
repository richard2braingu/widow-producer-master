"""XMLParser module for parsing objects and validating against XSD"""
import os
from urllib.request import pathname2url

from lxml import etree

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


# pylint: disable=too-few-public-methods  # Remove this when another public function is added
class XMLParser:
    """
    XML parser that validates XML objects against a given schema (XSD)
    """

    def __init__(self, root_path: str = None, catalog_path: str = None, schema_path: str = None):
        """
        Initialize Parser default settings if none given.

        :param root_path: Absolute path to project root.
        :param catalog_path: Relative path to XML catalog for schemas.
        :param schema_path: Relative path to XSD file.
        """
        if not root_path:
            root_path = ROOT

        if not catalog_path:
            catalog_path = self._get_catalog_path(root_path)

        if not schema_path:
            schema_path = self._get_schema_path(root_path)

        self._catalog_path = catalog_path
        self._load_catalog_path(self._catalog_path)
        self._schema_path = schema_path
        self._schema = self._get_schema(self._schema_path)
        self._parser = etree.XMLParser(schema=self._schema)

    @staticmethod
    def _load_catalog_path(catalog_path: str):
        """
        Loads the required catalog url into environment variables for use by the lxml library
        to find corresponding schemas by relative path.

        :param catalog_path: Absolute path to catalog XML file
        :return: None
        """
        xml_catalog_var_name = "XML_CATALOG_FILES"
        if not os.getenv(xml_catalog_var_name):
            catalog_url = f"file:{pathname2url(catalog_path)}"
            os.environ[xml_catalog_var_name] = catalog_url

    @staticmethod
    def _get_catalog_path(root_path: str):
        """
        Returns the absolute catalog path using environment variables or default config

        :param root_path: Absolute path to root of project
        :return: Full catalog file path
        """
        catalog_relative_path = os.getenv("CATLOG_RELATIVE_PATH", "catalog.xml")
        return os.path.join(root_path, catalog_relative_path)

    @staticmethod
    def _get_schema_path(root_path: str) -> str:
        """
        Returns the absolute schema path using environment variables or default config.

        :param root_path: Absolute path to root of project
        :return: Full schema file path
        """
        schema_relative_path = os.getenv("SCHEMA_RELATIVE_PATH", "uci_v2_schemas")
        schema_filename = os.getenv("SCHEMA_FILENAME", "UCI_MessageDefinitions_v2_0_Errata_1.xsd")
        return os.path.join(root_path, schema_relative_path, schema_filename)

    @staticmethod
    def _get_schema(schema_path: str) -> etree.XMLSchema:
        """
        Returns an XMLSchema object representing the schema at the given path

        :param schema_path: Full or relative schema filepath
        :return: lxml.etree.XMLSchema object loaded from the XML file
        """
        with open(schema_path, "rb") as schema_file:
            schema_root = etree.XML(schema_file.read())

        return etree.XMLSchema(schema_root)

    def parse_object(self, xml_string: bytes) -> etree._Element:
        """
        Parses and validates an XML object against the given or default schema

        :param xml_string: Full XML object as bytes string
        :return: Root node of resulting Element Tree
        """
        return etree.fromstring(xml_string, parser=self._parser)


if __name__ == "__main__":
    example_file = os.path.join(
        os.path.dirname(__file__), "tests", "example_xml", "smtiExample.xml"
    )
    uci_parser = XMLParser()
    with open(example_file, "rb") as file:
        root = uci_parser.parse_object(file.read())

    second_example_file = os.path.join(
        os.path.dirname(__file__), "tests", "example_xml", "missionPlanExample.xml"
    )
    with open(second_example_file, "rb") as file:
        second_root = uci_parser.parse_object(file.read())

    print(root)
    print(second_root)
