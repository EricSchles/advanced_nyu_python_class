import click

def add_file():
    pass

@click.command()
@click.argument('subcommand')
def pygit(subcommand):
    if subcommand == 'add':
        pass
    elif subcommand == 'commit':
        pass
    elif subcommand == 'pull':
        pass
    elif subcommand == 'push':
        pass
