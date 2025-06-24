from typing import List, Optional


class File:
    def __init__(self, name: str, directory: Optional["Directory"] = None):
        self.name: str = name
        self.directory: Optional["Directory"] = directory

    def __repr__(self) -> str:
        return f"File({self.name})"


class Directory:
    def __init__(self, name: str, root: Optional["Directory"] = None):
        self.name: str = name
        self.root: Optional["Directory"] = root
        self.files: List[File] = []
        self.sub_directories: List["Directory"] = []

    def add_sub_directory(self, sub_dir: "Directory") -> None:
        sub_dir.root = self
        self.sub_directories.append(sub_dir)

    def remove_sub_directory(self, sub_dir: "Directory") -> None:
        if sub_dir in self.sub_directories:
            self.sub_directories.remove(sub_dir)
            sub_dir.root = None

    def add_file(self, file: File) -> None:
        file.directory = self
        self.files.append(file)

    def remove_file(self, file: File) -> None:
        if file in self.files:
            self.files.remove(file)
            file.directory = None

    def __repr__(self) -> str:
        return f"Directory({self.name})"



root = Directory("root")
docs = Directory("docs")
img = Directory("images")

file1 = File("resume.docx")
file2 = File("photo.jpg")

root.add_sub_directory(docs)
root.add_sub_directory(img)

docs.add_file(file1)
img.add_file(file2)

print("Root contains:", root.sub_directories)
print("Docs files:", docs.files)
print("Img files:", img.files)

# docs.remove_file(file1)
# root.remove_sub_directory(img)
#
# print("Docs after removal:", docs.files)
# print("Root after removal:", root.sub_directories)