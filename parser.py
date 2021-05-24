import argparse
import textwrap

def read_parser():
    parser = argparse.ArgumentParser(
        formatter_class=argparse.RawDescriptionHelpFormatter,
        description=textwrap.dedent('''\
        Run scenarios of varous management practices
         '''))

    parser.add_argument(
        '-tsc',
        '--table_scenarios',
        help='csv table where the scenarios are specified',
        type=str,
        required=True
    )

    parser.add_argument(
        '-bm',
        '--benchmark_model',
        help='prepared H1D benchmark model',
        type=str,
        required=True
    )

    parser.add_argument(
        '-line',
        '--line',
        help='line where the parameters has to be changed',
        type=str,
        required=True
    )

    parser.add_argument(
        '-o',
        '--output_dir',
        help='outout directory',
        type=str,
        required=True
    )

    return parser.parse_args()
