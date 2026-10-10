class Note:
    def __init__(self, note_title, note_category, note_content, note_visibility):
        self.note_title = note_title
        self.note_category = note_category
        self.note_content = note_content
        self.note_visibility = note_visibility

    def to_dict(self):
        return {
            "note_title": self.note_title,
            "note_category": self.note_category,
            "note_content": self.note_content,
            "note_visibility": self.note_visibility
        }

        