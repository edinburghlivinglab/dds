infile = "../pages/project_success.md"
outfile = "temp.md"

out = []

with open(infile, encoding='utf8') as f:
    header = False
    meta = {}
    for line in f:
        line = line[:-1]
        if line.startswith("---") and not header:
            header = True
            continue
        if header:
            try:
                k, v = line.split(':')
                meta[k] = v.strip()
            except ValueError:
                pass
            if line.startswith("---"):
                header=False
                out.append('# {}\n'.format(meta['title']))
        else:
            out.append(line)

with open(outfile, 'w', encoding='utf8') as f:
    for line in out:
        f.write(line + '\n')




