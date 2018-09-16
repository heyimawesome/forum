import click

from app import create_app
from app import db
from app.auth.user import User

app = create_app()
db.app = app


@click.group()
def cli():
    pass


@click.command()
def init():
    print('Dropping db..')
    db.drop_all()

    print('Creating db..')
    db.create_all()


@click.command()
def seed():
    print('Creating seed user..')
    u = User(username='james')
    u.set_password('pass')

    return u.save()


@click.command()
@click.pass_context
def reset(ctx):
    ctx.invoke(init)
    ctx.invoke(seed)


cli.add_command(init)
cli.add_command(seed)
cli.add_command(reset)
