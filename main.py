from analytics import getLexicalSimilarityScore, getSemanticSimilarityScore, getOverallScore

def lambda_handler(event, context):
    # Compute Lexical Score
    lexical_score = getLexicalSimilarityScore()

    # Compute Semantic Score
    semantic_score = getSemanticSimilarityScore()

    # Compute Overall Score
    overall_score = getOverallScore()

    return {
        "data": "aws lambda"
    }

if __name__ == "__main__":

    # defining the corpus: oth index is model_answer
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
    lexical_score_list = getLexicalSimilarityScore(corpus)
    print(f"\nLexical Text Simillarity Score: {lexical_score_list}")
    print(type(lexical_score_list))
    print(type(lexical_score_list.tolist()))
    print(f"\nLexical Text Simillarity Score: {lexical_score_list}")


    semantic_score_list = getSemanticSimilarityScore(corpus)
    print(f"\nSemantic Text Simillarity Score: {semantic_score_list}")