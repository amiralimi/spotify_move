import argparse
from do_export import export
from do_import import import_

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--import_', help='import songs into exported_data.json', action='store_true')
    parser.add_argument('-e', '--export', help='export songs from exported_data.json', action='store_true')
    args = parser.parse_args()
    if args.export:
        export()
    if args.import_:
        import_()
