from pydantic import BaseModel


# schema for word2vec
class WordSimilarity(BaseModel):
    word: str
    similarity: float


class InvocationRequest(BaseModel):
    word: str


class InvocationResponse(BaseModel):
    word_similarities: list[WordSimilarity]
