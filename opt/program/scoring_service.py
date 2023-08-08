# A singleton for holding the model. This simply loads the model and holds it.
# It has a predict function that does a prediction based on the model and the input data.


import gensim

from opt.program.common import app_logger, settings


class ScoringService:
    model_path = f"{settings.BASE_DIR}ml/model/model.vec"

    model = None  # Where we keep the model when it's loaded

    @classmethod
    def get_model(cls) -> gensim.models.KeyedVectors:
        """Get the model object for this instance, loading it if it's not already loaded."""
        if cls.model is None:
            cls.model = gensim.models.KeyedVectors.load_word2vec_format(
                cls.model_path, binary=False
            )
            app_logger.info("model loaded successfully")
        return cls.model

    @classmethod
    def predict(cls, input: str) -> list[tuple[str, float]]:
        """For the input, do the predictions and return them.

        Args:
            input (a pandas dataframe): The data on which to do the predictions. There will be
                one prediction per row in the dataframe"""
        clf = cls.get_model()
        return clf.most_similar(input)
