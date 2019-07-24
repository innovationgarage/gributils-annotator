Service example for docker stack:

    annotator:
      image: innovationgarage/gributils-annotator
      environment:
        CONFIG: |
          {
              "index": "http://gribindexer:1028",
              "connections": [
                  {"handler": "source", "type": "listen", "address": "tcp:1024"},
                  {"handler": "destination", "type": "listen", "address": "tcp:1025"}
              ]
          }
      ports:
        - "7024:1024"
        - "7025:1025"
