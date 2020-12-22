from datetime import *
import os

images = '20 05 12 11 10 16 07 06 01-1 04 100 110'.split(' ')

for idx, name in enumerate(os.listdir('./posts')):
    file = open('./posts/' + name) 
    content = file.read()
    lines = content.split('\n') 
    title = lines[0][2:].strip()
    date = str(datetime.strptime(lines[2][2:], '%d %B %Y'))
    out_file_name = date[:10] + '-' + title + '.md' 
    out_file_name = out_file_name.replace(' ', '-')
    out_file_name = out_file_name.replace(':', '')

    with open('new_posts/' + out_file_name, 'w') as out:
        out.write('---\n') 
        out.write('layout: post\ntitle: ' + title + '\n')
        out.write('description:\ndate: ' + date + '\nimage: \'/images/' + images[idx % len(images)] + '.jpg\'\n')
        out.write('tags: []\n')
        out.write('---\n')
        for line in lines[3:]:
            out.write(line + '\n')
        out.close()
    file.close()

#d = datetime.strptime(input(), '%d %B %Y')
#print(d)
