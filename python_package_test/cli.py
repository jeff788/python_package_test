"""Console script for python_package_test."""
import sys
import click


@click.command()
def main(args=None):
    """Console script for python_package_test."""
    click.echo("Replace this message by putting your code into "
               "python_package_test.cli.main")
    click.echo("See click documentation at https://click.palletsprojects.com/")
    return 0


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
