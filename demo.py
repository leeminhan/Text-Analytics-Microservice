from sentence_transformers import SentenceTransformer, util
from tqdm import tqdm
model = SentenceTransformer('stsb-roberta-base-v2')

# Two lists of sentences
sentences1 = ['The cat sits outside',
            'A man is playing guitar',
            'The new movie is awesome']

sentences2 = ['The dog plays in the garden',
            'A woman watches TV',
            'The new movie is so great']

#Compute embedding for both lists
embeddings1 = model.encode(sentences1, convert_to_tensor=True)
embeddings2 = model.encode(sentences2, convert_to_tensor=True)

#Compute cosine-similarities
cosine_scores = util.pytorch_cos_sim(embeddings1, embeddings2)
print(cosine_scores)

print("\n========= Demo 1: Example =========")
#Output the pairs with their score
for i in tqdm(range(len(sentences1))):
    print("{} \t\t {} \t\t Score: {:.4f}".format(sentences1[i], sentences2[i], cosine_scores[i][i]))
    
# ============================================================================================================
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


# ============================================================================================================
# Demo 3: Find out the pairs with the highest cosine similarity scores:
sentences = ['The cat sits outside',
            'A man is playing guitar',
            'I love pasta',
            'The new movie is awesome',
            'The cat plays in the garden',
            'A woman watches TV',
            'The new movie is so great',
            'Do you like pizza?']

#Compute embeddings
embeddings = model.encode(sentences, convert_to_tensor=True)

#Compute cosine-similarities for each sentence with each other sentence
cosine_scores = util.pytorch_cos_sim(embeddings, embeddings)

#Find the pairs with the highest cosine similarity scores
pairs = []
for i in range(len(cosine_scores)-1):
    for j in range(i+1, len(cosine_scores)):
        pairs.append({'index': [i, j], 'score': cosine_scores[i][j]})

#Sort scores in decreasing order
pairs = sorted(pairs, key=lambda x: x['score'], reverse=True)

print("\n========= Demo 3: Pairs with the highest cosine similarity scores: =========")
for pair in pairs[0:10]:
    i, j = pair['index']
    print("{} \t\t {} \t\t Score: {:.4f}".format(sentences[i], sentences[j], pair['score']))