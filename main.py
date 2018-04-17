import sys
import mts


def main():
    if len(sys.argv) != 1:
        try:
            mts.select_theme(sys.argv[1])
            exit(0)
        except mts.NoMatchingThemeFoundException:
            sys.stderr.write('No matching theme found\n')
            exit(2)
    else:
        sys.stderr.write('Must specify one argument\n')
        exit(1)


if __name__ == '__main__':
    main()
