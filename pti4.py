class FileSystem:
    def __init__(self):
        self.files = {}
        
    def create_file(self, filename, content):
        if filename in self.files:
            print(f"File {filename} sudah ada")
        else:
            self.files[filename] = content 
            print(f"File {filename} dibuat")
    
    def read_file(self, filename):
        if filename in self.files:
            print(f"Isi dari {filename}: {self.files[filename]}")
        else:
            print(f"File {filename} tidak ditemukan")

# Contoh penggunaan
fs = FileSystem()
fs.create_file("file1.txt", "Hello, World!")
fs.read_file("file1.txt")
      