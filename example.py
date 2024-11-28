
#  ////////////////////////////////////////////////////////////////////////////////////////////
# from parcv import parcv

# # Initialize parser
# parser = parcv.Parser(pickle=True, load_pickled=True)

# # Parse the resume
# json_output = parser.parse('cvjake.pdf')
# print("\n--- JSON Output ---\n")
# print(json_output)  # Display the raw JSON output if necessary

# # Get resume lines and print them neatly
# lines = parser.get_resume_lines()
# print("\n--- Resume Lines ---\n")
# for line in lines:
#     print(f"{line}")

# # Get resume segments and print them in a formatted manner
# segments = parser.get_resume_segments()

# print("\n--- Resume Segments ---\n")

# # Print each segment with alignment
# for section, content in segments.items():
#     print(f"\n\033[1m{section.upper()}:\033[0m")  # Make section name bold
#     if isinstance(content, list):  # If it's a list of strings
#         for item in content:
#             print(f"  - {item}")
#     elif isinstance(content, dict):  # If it's a dictionary of sub-sections
#         for sub_section, details in content.items():
#             print(f"  \033[4m{sub_section}\033[0m:")  # Underlined sub-section
#             if details:
#                 for detail in details:
#                     print(f"    • {detail}")
#             else:
#                 print("    • No details available.")
#     else:
#         print(f"  {content}")

# # Save the parsed content as a JSON file
# file_name = "output.json"
# parser.save_as_json(file_name)

# /////////////////////////////////////////////////////////////////////////////////////////
from parcv import parcv
import json

# Initialize parser
parser = parcv.Parser(pickle=True, load_pickled=True)

# Parse the resume
parsed_data = parser.parse('yourcv.pdf')
print(parsed_data)
# # Fetch detailed segments
segments = parser.get_resume_segments()
# print("++++++"+segments)
# Remove redundant or repeated fields
def clean_segments(segments):
    cleaned = {}
    for section, content in segments.items():
        if isinstance(content, list):  # Handle lists
            cleaned[section] = list(dict.fromkeys(content))  # Remove duplicates while maintaining order
        elif isinstance(content, dict):  # Handle nested dictionaries
            cleaned[section] = {
                sub_section: list(dict.fromkeys(details)) if isinstance(details, list) else details
                for sub_section, details in content.items()
            }
        else:
            cleaned[section] = content
    return cleaned

cleaned_segments = clean_segments(segments)

# Merge parsed JSON data and cleaned segments
final_output = {
    "Basic Details": parsed_data,
    "Detailed Segments": cleaned_segments
}

# Convert to JSON format and display
formatted_json = json.dumps(final_output, indent=4, ensure_ascii=False)
print("\n--- Final JSON Output ---\n")
print(formatted_json)

# Save the cleaned and formatted JSON to a file
output_file = "formatted_output.json"
with open(output_file, "w", encoding="utf-8") as f:
    f.write(formatted_json)

print(f"\nFormatted JSON has been saved to {output_file}")
