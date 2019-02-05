import click

from ruamel import yaml


@click.command(name="create")
@click.option("-o", "--outfile", type=click.Path(), default=None)
@click.argument("name")
@click.argument("includes", nargs=-1)
def command(name, includes, outfile):
    if outfile is None:
        outfile = f"docker-cc.{name}.yml"
    with open(outfile, "wt") as ostream:
        yaml.dump(
            data={"docker-cc": {"name": name, "includes": list(includes)}},
            stream=ostream,
            default_flow_style=False,
        )
