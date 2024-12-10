image_path = "../../frontend/public/ishihara_images/"


img_paths = [[], [], [], [], [], []]

pictures_per_row = 2

for row_idx in range(len(img_paths)):
    for img_idx in range(pictures_per_row):
        img_paths[row_idx].append(
            f"image-{row_idx * pictures_per_row + (img_idx + 1)}.png"
        )

def generate_table_row(row_paths):
    return " | | ".join([
        f'<div style="text-align:center;">'
        f'<img src="{image_path}{path}" style="width:100px;"><br>'
        f'</div>'
        for path in row_paths
    ])

header = "| Bild | Ergebnis | Bild | Ergebnis |"
separator = "|----------|----------|----------|----------|"
rows = [generate_table_row(row) for row in img_paths]

markdown_content = f"""\
# Table with Images and Fonts

This table contains images with captions in a custom font:

{header}
{separator}
{'\n'.join(rows)}
"""

file_path = "table_with_images_and_fonts.md"
with open(file_path, "w") as file:
    file.write(markdown_content)

print(f"Markdown file '{file_path}' with styled fonts and images created successfully!")
