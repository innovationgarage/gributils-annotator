#! /bin/sh

echo "$CONFIG" > config.json
gributils-annotator --config config.json
