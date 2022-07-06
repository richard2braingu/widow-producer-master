import json
from jinja2 import Template
from uci import XMLParser


def main():
    # Open Widow Data and mapping file
    # Build a mapped data dict
    # Open Jinja2 template
    # Render the Jinja2 template with the mapped data dict
    # Write the rendered template to a file
    # Validate the written file with XMLParser

    mapped_data = {}

    with open("amtiWidowData.json") as file:
        widow_data = json.load(file)

    with open("amtiExampleMapping.json") as file:
        mapping = json.load(file)

    for key in widow_data:
        mapped_data[mapping[key]] = widow_data[key]

    with open("amtiExample.j2") as file:
        template = Template(file.read())
    
    rendered_template = template.render(mapped_data)

    with open("amtiExampleRendered.xml", "w") as file:
        file.write(rendered_template)

    with open("amtiExampleRendered.xml", "rb") as file:
        root = XMLParser().parse_object(file.read())
        print(root)


if __name__ == "__main__":
    main()
