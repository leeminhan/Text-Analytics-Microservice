# utility function to evaluate jaccard similarity
def jaccard_similarity(doc_1, doc_2):
    a = set(doc_1.split())
    b = set(doc_2.split())
    c = a.intersection(b)
    return float(len(c)) / (len(a) + len(b) - len(c))
    
# print(f"Jaccard Simiarity: {jaccard_similarity(corpus[0], corpus[1])}")