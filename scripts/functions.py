from doctest import Example
from typing import Callable, Iterator

import spacy
from spacy.language import Language
from spacy.training import Example


@spacy.registry.readers("text_reader.v1")
def read_text(source: str) -> Callable[[Language], Iterator[Example]]:
    def generate_stream(nlp):
        with open(source) as f:
            for line in f:
                if len(line.strip()) == 0:
                    continue

                doc = nlp.make_doc(line)
                example = Example.from_dict(doc, {})
                yield example
    return generate_stream
