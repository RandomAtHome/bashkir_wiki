So far, we have 3 versions.
1) web_parser.py
It parsers whole wiki, but keeps all results of all pages in memory, thus using an immerse amount of memory space.
Though it's the original, it's unlikely to use. Checked twice.
2) web_light.py
Light version of previous, it remembers only the best result, taking times less space, but shows only it.
You are more like to use it.
3) web_out_file_gen.py
Modification of the original, it intends to first write all data to a specific file, then extract it from there,
and then sort out. In theory it will work better.

All this files, but web_light.py use params.txt, where is written how much results we must show. It must lay in the same directory.

If it is, then launch the .py and wait for result.