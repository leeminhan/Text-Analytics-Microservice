
from sentence_transformers import SentenceTransformer, util
from tqdm import tqdm
from typing import List
model = SentenceTransformer('stsb-roberta-base-v2')

# defining the corpus
# oth index is model_answer
corpus = [
"Turin's theory deuterated acetophenone smells different (from non- deuterated from), \
it deuterated benzaldehyde smells different (from non- deuterated form), structures of deuterated \
acetophenone and benzaldehyde given.",
"Molecules have very different shapes so the lock and key theory suggests they would smell different \
but in fact they smell similar. By contrast, diols like ethylere glycol smell completely different to \
dithols despite very similar shapes.",
"Ethylene glycol and ethane clithicl have very dimilar structure but very different smellsin the lock and \
key theory, these two molecules would have very similar smells as both molecules could fit in the same lock. \
When atoms were replaced with their ixtopeom moleculea there was a subtle change in smell in the lock and \
key theory. This would indicate that the massed the banded atoms does affect smell, as predicted by Turin Timber."
]

def getSemanticSimilarityScore(corpus:List[str]):
    """Compute Semantic Text Similarity Score For 1 Question
        1. Computes model_ans word embeddings
        2. Computes student_res word embeddings
        3. Compare semantic text similarity between model_ans and student_res
        4. Repeat for all other students responses
        Args:
            corpus (List[str]): A list of 1 model_ans followed by many student_res of for this question
            i.e. [model_ans, student_res_1, student_res_2, ..., student_res_n]
        Return:
            semantic_score (List[int]): semantic score of each student's response
    """

    model_ans = corpus[0]
    model_ans_embedding = model.encode(model_ans, convert_to_tensor=True)

    student_responses = corpus[1:]
    semantic_score = []

    for student_res in student_responses:
        student_res_embedding = model.encode(student_res, convert_to_tensor=True)

        #Compute semantic cosine-similarity
        cosine_score = util.pytorch_cos_sim(model_ans_embedding, student_res_embedding) # cosine_score is a 2D tensor object
        semantic_score.append(cosine_score.item())
    return semantic_score