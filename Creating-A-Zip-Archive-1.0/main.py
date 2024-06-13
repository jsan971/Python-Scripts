# Import the zipfile module
import zipfile

filesToZip = ['Creating-A-Zip-Archive/test_file.csv' , 'Creating-A-Zip-Archive/test_file.txt'] # This is our array of the files we would like to archive

def create_zip(zipf, files, opt):
    with zipfile.ZipFile(zipf, opt, allowZip64=True) as archive:
        for f in files:
            archive.write(f)


create_zip('./files.zip', filesToZip, 'w') # What we would like to name the archive, passing the list and the operation mode

