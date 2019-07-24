import click
import socket_tentacles
import gributils_annotator.annotator
import json

@click.command()
@click.option('--config', default="config.json")
@click.pass_context
def main(ctx, config):
    with open(config) as f:
        config = json.load(f)
    gributils_annotator.annotator.annotator(config)
