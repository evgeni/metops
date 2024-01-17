import random

import click

from mastodon import Mastodon

@click.group
def cli():
    pass

@cli.command
def toot():
    with open('posts.txt') as posts_file:
        all_posts = [p.strip() for p in posts_file.readlines()]
    try:
        with open('done.txt') as done_file:
            done_posts = [p.strip() for p in done_file.readlines()]
    except FileNotFoundError:
        done_posts = []
    posts = list(set(all_posts) - set(done_posts))
    post = random.choice(posts)
    with open('done.txt', 'a') as done_file:
        done_file.write(f'{post}\n')
    mastodon = Mastodon(access_token = 'pytooter_usercred.secret')
    mastodon.toot(post)
    print(post)

@cli.command
def register():
    Mastodon.create_app(
        'MetOps',
        api_base_url='https://botsin.space',
        to_file = 'pytooter_clientcred.secret'
    )

@cli.command
def login():
    mastodon = Mastodon(client_id = 'pytooter_clientcred.secret')
    mastodon.log_in(
        'user@example.com',
        'password',
        to_file = 'pytooter_usercred.secret'
    )

if __name__ == '__main__':
    cli()
