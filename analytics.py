from tqdm import tqdm
from typing import List
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import TfidfVectorizer
from sentence_transformers import SentenceTransformer, util
model = SentenceTransformer('./serverless-bert/stsb-roberta-base-v2')

# defining the corpus: oth index is model_answer
# ensure corpus mock data has not indentation on the left
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

def getLexicalSimilarityScore(corpus:List[str]):
    """Compute Lexical Text Similarity Score For 1 Question
        1. Vectorize the entire corpus
        2. Perform cosine similarity
        Args:
            corpus (List[str]): A list of 1 model_ans followed by many student_res of for this question
            i.e. [model_ans, student_res_1, student_res_2, ..., student_res_n]
        Return:
            lexical_score (List[int]): Lexical score of each student's response
    """

    # Generate the tf-idf vectors for the corpus
    tfidf = TfidfVectorizer()
    X = tfidf.fit_transform(corpus)

    # Compute cosine similarity score
    cosine_sim_score = cosine_similarity(X, X) # 2d matrix of scores, each vector against all other vector
    
    # return student's scores only
    return cosine_sim_score[0][1:]

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
            semantic_score (List[int]): Semantic score of each student's response
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

def getOverallScore(lexical_score, semantic_score, alpha=0.2, beta=0.8):
    overall_score_store = []
    for i in range(len(lexical_score)):
        overall_score = alpha*lexical_score[i] + beta*semantic_score[i]
        overall_score_store.append(overall_score)
    return overall_score_store