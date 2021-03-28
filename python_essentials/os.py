import os.path

dirs_with_python_files = set()

for current_dir, dirs, files in os.walk('main'):
    for file in files:
        if '.py' in file:
            dirs_with_python_files.add(current_dir)
    print(current_dir, dirs, files)

dirs_with_python_files = "\n".join(sorted(dirs_with_python_files))
with open('answer.txt', 'w') as ans:
    ans.write(dirs_with_python_files)
