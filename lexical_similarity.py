# importing libraries
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import TfidfVectorizer
from sentence_transformers import SentenceTransformer, util
from tqdm import tqdm
model = SentenceTransformer('stsb-roberta-base-v2')

model_answer_1 = "Turin's theory deuterated acetophenone smells different (from non- deuterated from), \
it deuterated benzaldehyde smells different (from non- deuterated form), structures of deuterated \
acetophenone and benzaldehyde given."

# model_answer_2 = "Loading is to load  into companion cells; location of companion cells at a source \
# or named source active loading of sucrose (using ATP); mitochondria presence in companion cells; description \
# of mechanism of H gradient and cotransport; movement via plasmodesmata into sieve tube elements.Movement is \
# mass flow from source to sink; ref to high hydrostatic pressure at source; ref to inflow of water by osmosis \
# at the source (creating the pressure); ref to passage through sieve plates or cytoplasmic connections; ref to \
# low hydrostatic pressure at the sink; ref to unloading at the sink."

student_res_1 =  "Molecules have very different shapes so the lock and key theory suggests they would smell different \
but in fact they smell similar. By contrast, diols like ethylere glycol smell completely different to \
dithols despite very similar shapes."

student_res_2 = "Ethylene glycol and ethane clithicl have very dimilar structure but very different smellsin the lock and \
    key theory, these two molecules would have very similar smells as both molecules could fit in the same lock. \
    When atoms were replaced with their ixtopeom moleculea there was a subtle change in smell in the lock and \
    key theory. This would indicate that the massed the banded atoms does affect smell, as predicted by Turin Timber."

#Compute embedding for both model answer & student response
model_ans_embeddings_1 = model.encode(model_answer_1, convert_to_tensor=True)
student_res_embeddings_1 = model.encode(student_res_1, convert_to_tensor=True)
student_res_embeddings_2 = model.encode(student_res_2, convert_to_tensor=True)

#Compute cosine-similarits
cosine_score_1 = util.pytorch_cos_sim(model_ans_embeddings_1, student_res_embeddings_1)
cosine_score_2 = util.pytorch_cos_sim(model_ans_embeddings_1, student_res_embeddings_2)

print("\n========= Demo 2: Comparing Student's Responses to Model Answer =========")
print(f"student response 1 score: {cosine_score_1[0][0]}")
print(f"student response 2 score: {cosine_score_2[0][0]}")

# utility function to evaluate jaccard similarity
def jaccard_similarity(doc_1, doc_2):
    a = set(doc_1.split())
    b = set(doc_2.split())
    c = a.intersection(b)
    return float(len(c)) / (len(a) + len(b) - len(c))

# corpus = ['The sun is the largest celestial body in the solar system', 
#         'The solar system consists of the sun and eight revolving planets', 
#         'Ra was the Egyptian Sun God', 
#         'The Pyramids were the pinnacle of Egyptian architecture', 
#         'The quick brown fox jumps over the lazy dog'
#     ]

# defining the corpus
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

# Generate the tf-idf vectors for the corpus
tfidf = TfidfVectorizer()
X = tfidf.fit_transform(corpus)

# print(f"Jaccard Simiarity: {jaccard_similarity(corpus[0], corpus[1])}")
cosine_sim_score = cosine_similarity(X, X)
print(f"\nCosine Similarity Score Matrix: \n{cosine_sim_score}")
print(f"\nCosine Similarity Score of Teacher against student: \n{cosine_sim_score[0]}")
