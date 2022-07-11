# Creating
# file: fileone.txt
# mode: w+
f = open('fileone.txt', 'w+')
f.write('ONE FILE')
f.close()

f = open('filetwo.txt', 'w+')
f.write('TWO FILE')
f.close()


# To zip these files:
import pwd
import zipfile
# Name of the zip file: comp_file.zip
# Mode: w
comp_file = zipfile.ZipFile('comp_file.zip', 'w')
comp_file.write('fileone.txt', compress_type=zipfile.ZIP_DEFLATED)
comp_file.write('filetwo.txt', compress_type=zipfile.ZIP_DEFLATED)
comp_file.close()


# To extract those files FROM the file you want to unzip:
zip_obj = zipfile.ZipFile('comp_file.zip', 'r')
# Create folder where you're going to put all the extracted files:
zip_obj.extractall('extracted_content')


# To find out file or folder path
pwd


# Using shell utilities to zip or compress entire folder instead of one by one single files
import shutil 

directory_to_zip = '/home/loannejee/ZippingPython'
output_filename = 'example'

shutil.make_archive(output_filename, 'zip', directory_to_zip)

# To unzip using shell utilites:
# zip file: 'example.zip'
# folder to keep extracted files: 'final_unzip'
# format: 'zip'
shutil.unpack_archive('example.zip', 'final_unzip', 'zip')

