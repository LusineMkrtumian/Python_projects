from natasha import (
    Segmenter,
    MorphVocab,

    NewsEmbedding,
    NewsMorphTagger,
    NewsSyntaxParser,
    NewsNERTagger,

    PER,
    NamesExtractor,

    Doc
)

segmenter = Segmenter()
morph_vocab = MorphVocab()

emb = NewsEmbedding()
morph_tagger = NewsMorphTagger(emb)
syntax_parser = NewsSyntaxParser(emb)
ner_tagger = NewsNERTagger(emb)

names_extractor = NamesExtractor(morph_vocab)

text = 'В четверг 22.06.2023 работник Павлов Семен Андреевич поджег кресло и устроил пожар на рабочем месте'
doc = Doc(text)

doc.segment(segmenter)
print(doc.tokens[:5])
print(doc.sents[:5])

doc.tag_morph(morph_tagger)
print(doc.tokens[:5])
doc.sents[0].morph.print()

for token in doc.tokens:
    token.lemmatize(morph_vocab)

print(doc.tokens[:5])
{_.text: _.lemma for _ in doc.tokens}

doc.tag_ner(ner_tagger)
print(doc.spans[:5])
doc.ner.print()

print("**************************************")

for span in doc.spans:
    span.normalize(morph_vocab)
print(doc.spans[:5])
