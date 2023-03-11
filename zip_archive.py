import shutil
import os
import zipfile

if __name__ == '__main__': 
    #shutil.make_archive('lambda_function', 'zip', r'C:\Users\z0049ufx\SMO Software Projects\AMA Cloud\API\FastAPI Lambda\lib')

    zip = zipfile.ZipFile(r'C:\Users\z0049ufx\SMO Software Projects\AMA Cloud\API\FastAPI Lambda\lambda_function.zip','a')
    zip.write(
        r'C:\Users\z0049ufx\SMO Software Projects\AMA Cloud\API\FastAPI Lambda\books.json', 
        os.path.basename(r'C:\Users\z0049ufx\SMO Software Projects\AMA Cloud\API\FastAPI Lambda\books.json'))
    zip.close()