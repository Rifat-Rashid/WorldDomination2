import sys

if __name__ == '__main__':
    if '--legacy-ui' in sys.argv:
        sys.argv.remove('--legacy-ui')
        from wd2.desktop import main
    else:
        if '--original-menu' in sys.argv:
            sys.argv.remove('--original-menu')
        from wd2.setup_menu import main
    main()
