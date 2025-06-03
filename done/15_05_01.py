class Editor:
    def view_document(self):
        print("Перегляд документа доступний.")

    def edit_document(self):
        print("Редагування доступне лише у версії Pro.")


class ProEditor(Editor):
    def edit_document(self):
        print("Редагування документа...")


LICENSE_KEY = "12345-PRO"

user_key = input("Введіть ліцензійний ключ: ")

if user_key == LICENSE_KEY:
    editor = ProEditor()
    print("Активовано версію Pro.")
else:
    editor = Editor()
    print("Активовано безкоштовну версію.")

editor.view_document()
editor.edit_document()
