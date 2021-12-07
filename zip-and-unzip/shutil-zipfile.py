import shutil
dir_to_zip = '/Users/abiwardani/Documents/tutorial/python/belajar-python/zip-and-unzip/uncompressed'
output_filename = 'shutil-example'
shutil.make_archive(output_filename, 'zip', dir_to_zip)
shutil.unpack_archive('shutil-example.zip', 'uncompressed-shutil', 'zip')