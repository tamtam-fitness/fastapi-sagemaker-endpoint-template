from pydantic import BaseModel


# schema for word2vec
class WordSimilarity(BaseModel):
    word: str
    similarity: float


class Result(BaseModel):
    word_similarities: list[WordSimilarity]
