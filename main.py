from js import document

def generate_message(event=None):
    output = document.getElementById("output")
    output.innerText = ""  # Clear previous message

    # Get input values
    name = document.getElementById("name").value.strip()
    age = document.getElementById("age").value.strip()
    school = document.getElementById("school").value.strip()

    # Check if any field is empty
    if not name or not age or not school:
        output.innerText = "⚠️ Please fill out all fields before generating the message."
        return

    # Multiline string with escape characters
    message = f"""
📘 Student Profile
Name\t: {name}
Age\t: {age}
School\t: {school}

🖊 Notes:
{name} is currently {age} years old and studies at {school}.
This information was gathered through input fields and displayed
using a multiline string in Python via PyScript.
"""

    output.innerText = message
