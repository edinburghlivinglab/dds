import argparse
from os.path import join, basename



def strip_header(text, verbose=False):
    out = []
    header = False
    meta = {}
    for line in text:
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
                title = meta['title']
                title = title[1:-1]
                out.append('# {} \n'.format(title))
        else:
            out.append(line)
    if verbose:
        print('copied {} lines'.format(len(out)))
    return out



if __name__ == "__main__":
    parser = argparse.ArgumentParser()
#    parser.add_argument('infile', type=argparse.FileType('r', encoding='UTF-8'))
#    parser.add_argument('outfile', type=argparse.FileType('w', encoding='UTF-8'))

    parser.add_argument('-outdir', required=True)
    parser.add_argument('infile', nargs='*')
    parser.add_argument('--verbose', '-v', action='store_true')
    args = parser.parse_args()


    for infile in args.infile:
        with open(infile) as f:

            if args.verbose:
                print('opening file {}'.format(infile))

            headless = strip_header(f, verbose=args.verbose)
            infile = basename(infile)
            outfile = join(args.outdir, infile)

            with open(outfile, "w", encoding='utf8') as outf:
                if args.verbose:
                    print('writing to file {}'.format(outfile))
                for line in headless:
                    outf.write(line + '\n')
                    #args.outfile.write(line + '\n')
