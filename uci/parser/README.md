# Using uci.parser.Parser

Example:

```python
(venv) ➜  widow-producer % python
Python 3.9.12 (main, Mar 26 2022, 15:52:10) 
[Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> from uci import XMLParser
>>> with open("uci/parser/tests/example_xml/amtiExample.xml", "rb") as f:
...     root = XMLParser().parse_object(f.read())
... 
>>> root
<Element {https://www.vdl.afrl.af.mil/programs/oam}AMTI_Capability at 0x106d7a740>
```