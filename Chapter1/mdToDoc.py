import os  
def auto_md_to_docx(file_dir):
    all_whole_path_files = []
    for root, dirs, files in os.walk(file_dir):
        for file in files:
            try:
                if file[-3:] == ".md":
                    file_info = [root+'/', file]
                    all_whole_path_files.append(file_info)
            except Exception as e:
                print(e)
    print("==>", all_whole_path_files)

    for file_info in all_whole_path_files:
        md_file_path_file = file_info[0] + file_info[1]
        docx_file_name = file_info[1][:-3] + '.docx'
        docx_file_path_file = file_info[0] + docx_file_name
        new_command = 'pandoc ' + md_file_path_file + ' -o ' + docx_file_path_file

        try:
            result = os.popen(new_command).readlines()
            if len(result) == 0:
                print(md_file_path_file, "Converted:", docx_file_path_file)
        except Exception as e:
            print(e)

def main():
    auto_md_to_docx('.')

if __name__ == '__main__':
    main()