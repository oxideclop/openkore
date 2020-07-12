import os
import gzip

if __name__ == "__main__":
    for dispath, dirname, filenames in os.walk(r'.'):
        for filename in filenames:
            if '.fld' in filename:
                file_name_read = os.path.join(dispath,filename)
                file_name_write = os.path.join(dispath, filename + '.gz')
                with open(file_name_read, "rb") as file_read, gzip.open(file_name_write, "wb") as file_write:
                    file_write.write(file_read.read())
                print(file_name_read + '\t-->\t' + file_name_write)     
    print('Done')
