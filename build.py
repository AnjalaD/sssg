import json
import re
from staticjinja import Site
from os import listdir
from os.path import isfile, join, splitext

template_path = 'src/views'
data_path = 'src/data'
output_path = 'dist'

context = {}
for f in listdir(data_path):
    if isfile(join(data_path, f)):
        json_data = json.load(open(join(data_path, f)))
        name = re.sub(r'[^a-zA-Z]+', '_', splitext(f)[0])
        context[name] = json_data
print(context)

site = Site.make_site(
    searchpath=template_path,
    outpath=output_path,
    contexts=[('.*.html', context)],
)
site.render(use_reloader=False)
