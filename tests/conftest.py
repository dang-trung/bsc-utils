def pytest_addoption(parser):
    parser.addoption(
        '--nonskip',
        action='store_true',
        dest='nonskip',
        default=False,
        help='run all the tests even the default skipped ones'
    )
