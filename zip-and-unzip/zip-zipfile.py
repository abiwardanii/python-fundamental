import zipfile
# membuat objek zipfile file 1 dan 2
f = open('one.txt', 'w+')
f.write('Hello one')
f.close()

f = open('two.txt', 'w+')
f.write('Hello two')
f.close()

# membuat file zip(bukan compress)
comp_file = zipfile.ZipFile('compressed.zip', 'w')

# compress file 1 dan 2 menjadi file zip
comp_file.write('one.txt', compress_type=zipfile.ZIP_DEFLATED)
comp_file.write('two.txt', compress_type=zipfile.ZIP_DEFLATED)
comp_file.close()

# unzip
uncomp_file = zipfile.ZipFile('compressed.zip', 'r')

# membuat nama folder pada sat unzip file
uncomp_file.extractall('uncompressed')