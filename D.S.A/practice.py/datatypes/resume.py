import base64
from reportlab.lib.pagesizes import LETTER, inch
from reportlab.pdfgen import canvas


def generate_resume_pdf(filename, data):
    c = canvas.Canvas(filename, pagesize=LETTER)
    width, height = LETTER
    text = c.beginText(1 * inch, height - 1 * inch)
    text.setFont("Helvetica-Bold", 20)
    text.textLine(data["name"])

    text.setFont("Helvetica", 12)
    text.textLine(data["email"])
    text.textLine(data["phone"])
    text.textLine(data["linkedin"])
    text.textLine(" ")

    # Summary
    text.setFont("Helvetica-Bold", 14)
    text.textLine("Summary")
    text.setFont("Helvetica", 12)
    for line in data["summary"].split('\n'):
        text.textLine(line)
    text.textLine(" ")

    # Education
    text.setFont("Helvetica-Bold", 14)
    text.textLine("Education")
    text.setFont("Helvetica", 12)
    for edu in data["education"]:
        text.textLine(f"{edu['degree']} - {edu['institution']} ({edu['year']})")
    text.textLine(" ")

    # Experience
    text.setFont("Helvetica-Bold", 14)
    text.textLine("Experience")
    text.setFont("Helvetica", 12)
    for exp in data["experience"]:
        text.textLine(f"{exp['title']} - {exp['company']} ({exp['year']})")
        for duty in exp["details"]:
            text.textLine(f"  - {duty}")
    text.textLine(" ")

    # Skills
    text.setFont("Helvetica-Bold", 14)
    text.textLine("Skills")
    text.setFont("Helvetica", 12)
    text.textLine(", ".join(data["skills"]))

    c.drawText(text)
    c.showPage()
    c.save()
    print(f"[✓] Resume saved as {filename}")


def encode_file_to_base64(input_file):
    with open(input_file, "rb") as f:
        encoded = base64.b64encode(f.read())
    print("[✓] File encoded to Base64.")
    return encoded


def decode_base64_to_file(encoded_data, output_file):
    with open(output_file, "wb") as f:
        f.write(base64.b64decode(encoded_data))
    print(f"[✓] File decoded and saved as {output_file}")


# === Sample Resume Data ===
resume_data = {
    "name": "John Doe",
    "email": "john.doe@example.com",
    "phone": "(123) 456-7890",
    "linkedin": "linkedin.com/in/johndoe",
    "summary": "Experienced software engineer with strong background in Python.\nSkilled in web apps and automation.",
    "education": [
        {"degree": "B.Sc. Computer Science", "institution": "XYZ University", "year": "2020"},
    ],
    "experience": [
        {
            "title": "Software Engineer",
            "company": "Tech Corp",
            "year": "2020–2023",
            "details": [
                "Built REST APIs with Django.",
                "Developed frontends with React.",
            ],
        },
    ],
    "skills": ["Python", "Django", "JavaScript", "React", "SQL"],
}

# === Step 1: Generate Resume ===
pdf_filename = "resume.pdf"
generate_resume_pdf(pdf_filename, resume_data)

# === Step 2: Encode PDF to Base64 ===
encoded_resume = encode_file_to_base64(pdf_filename)

# === Step 3: Decode Base64 back to PDF ===
decoded_filename = "resume_decoded.pdf"
decode_base64_to_file(encoded_resume, decoded_filename)
