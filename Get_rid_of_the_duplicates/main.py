student_data={
    "id1": {"name": "Anika", "class": "VII", "subject_integration": "English, Math, Science"},
    "id2": {"name": "Lihan", "class": "VII", "subject_integration": "English, Math, Science"},
    "id3": {"name": "Anika", "class": "VII", "subject_integration": "English, Math, Science"},
    "id4": {"name": "Merisha", "class": "VII", "subject_integration": "English, Math, Science"},
}
result = {}
seen=set()

for student_id, details in student_data.items():
    unique_key = (details["name"], details["class"], details["subject_integration"])
    if unique_key not in seen:
        seen.add(unique_key)
        result[student_id] = details
        
for k, v in result.items():
    print(k, ":", v)