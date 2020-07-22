import os

os.path.join('folder1', 'subfolder', 'pic.png')
# print(os.sep)
# print(os.getcwd())
# print(os.path.abspath('pikachu.jpg'))
# print(os.path.abspath('..\\..\\pikachu.jpg'))
path='..\\..\\pikachu.jpg'
print(os.path.isabs(path))
