from sentence_transformers import SentenceTransformer, util
from tqdm import tqdm
model = SentenceTransformer('paraphrase-distilroberta-base-v2')

model_answer_1 = "Turin's theory deuterated acetophenone smells different (from non- deuterated from), \
it deuterated benzaldehyde smells different (from non- deuterated form), structures of deuterated \
acetophenone and benzaldehyde given."

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