import click


@click.command()
@click.option('--as-cowboy', '-c', is_flag=True, help='Greet as a cowboy.')
@click.argument('name', default='world', required=False, help='Name of person to greet')
def main(name, as_cowboy):
    """{{ cookiecutter.project_short_description }}"""
    greet = 'Howdy' if as_cowboy else 'Hello'
    click.echo('{0}, {1}.'.format(greet, name))
