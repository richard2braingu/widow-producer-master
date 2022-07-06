import json
from jinja2 import Template
from uci import XMLParser


def main():
    # Open Widow Data and mapping file
    # Build a mapped data dict
    # Open Jinja2 template
    # Render the Jinja2 template with the mapped data dict
    # Validate the rendered template with XMLParser
    # Write the rendered template to a file

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

    # Check that the rendered template passes validation before writing
    root = XMLParser().parse_object(rendered_template.encode('utf-8'))
    print(root)

    with open("amtiExampleRendered.xml", "w") as file:
        file.write(rendered_template)



if __name__ == "__main__":
    main()
