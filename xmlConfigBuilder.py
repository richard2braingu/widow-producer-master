import json
from jinja2 import Template
from uci import XMLParser


def main(xml_template, widow_data, output_file):
    with open(widow_data) as file:
        data = json.load(file)
    
    with open(xml_template) as file:
        template = Template(file.read())

    # root = XMLParser().parse_object(f.read())

    with open(output_file, "w") as rendered_template:
        rendered_template.write(
            template.render(template_mapping(data))
        )


def template_mapping(data):
    return {
        "capability_id_uuid": data["capability_id"],
        "capability_type": data["capability_product_type"],
        "sub_capability_type": data["sub_capability_123_type"],
        "accepted_interface": data["interface"],
        "interrupt_other_activities": data["interrupt_activities"],
        "collection_policy": data["collection_111_policy"],
        "current_ops_supported": data["concurrency-supported"],
        "supp_freq_min": data["minimum_frequency"],
        "supp_freq_max": data["maximum_frequency"]
    }


if __name__ == "__main__":
    main("amtiExample.j2", "amtiWidowData.json", "amtiExampleRendered.xml")
