import re
import pandas as pd

# Read the PlantUML file content
file_path = '/mnt/data/full_logical_erd.wsd'
with open(file_path, 'r') as file:
    plantuml_content = file.read()

# Regex patterns to extract entities and attributes
entity_pattern = r"entity\s+(\w+)\s*\{([^}]+)\}"
attribute_pattern = r"([\w_]+)\s*:\s*([\w<>]+(?:\(\d+\))?),?\s*(.*)"

# Extract entities and attributes
entities_data = []
attributes_data = []
relationships_data = []

entities = re.findall(entity_pattern, plantuml_content, re.DOTALL)
for entity_name, entity_body in entities:
    entities_data.append({"Entity Name": entity_name})
    # Parse attributes within the entity body
    attributes = entity_body.split('\n')
    for attribute in attributes:
        attribute = attribute.strip()
        if attribute.startswith("+"):  # Primary Key
            attr_match = re.match(r"\+\s*PRIMARY_KEY\((\w+)\)", attribute)
            if attr_match:
                attributes_data.append({
                    "Entity Name": entity_name,
                    "Attribute Name": attr_match.group(1),
                    "Data Type": "Primary Key",
                    "Constraint": "PK"
                })
        elif attribute.startswith("-"):  # Foreign Key or other comments
            continue
        else:
            attr_match = re.match(attribute_pattern, attribute)
            if attr_match:
                attr_name = attr_match.group(1)
                attr_type = attr_match.group(2)
                attr_constraints = attr_match.group(3)
                attributes_data.append({
                    "Entity Name": entity_name,
                    "Attribute Name": attr_name,
                    "Data Type": attr_type,
                    "Constraint": attr_constraints
                })
                # Identify foreign keys for relationships
                if "FOREIGN_KEY" in attr_constraints:
                    fk_target_match = re.search(r"FOREIGN_KEY\((\w+)\)", attr_constraints)
                    if fk_target_match:
                        relationships_data.append({
                            "Parent Entity": fk_target_match.group(1),
                            "Child Entity": entity_name,
                            "Parent Attribute": attr_name,  # Placeholder, improve logic if needed
                            "Child Attribute": attr_name
                        })

# Convert parsed data to dataframes
entities_df = pd.DataFrame(entities_data)
attributes_df = pd.DataFrame(attributes_data)
relationships_df = pd.DataFrame(relationships_data)

# Save dataframes to an Excel file
output_file = '/mnt/data/plantuml_to_erwin.xlsx'
with pd.ExcelWriter(output_file) as writer:
    entities_df.to_excel(writer, sheet_name='Entities', index=False)
    attributes_df.to_excel(writer, sheet_name='Attributes', index=False)
    relationships_df.to_excel(writer, sheet_name='Relationships', index=False)

output_file
