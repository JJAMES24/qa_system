import faiss
import numpy as np

# Load the document embeddings
document_embeddings = np.load('document_embeddings.npy')

# Build FAISS index
dimension = document_embeddings.shape[1]
index = faiss.IndexFlatL2(dimension)
index.add(document_embeddings)

def retrieve_documents(query, top_k=5):
    query_embedding = rag_retriever.embed_text(rag_tokenizer(query, return_tensors="pt", padding=True, truncation=True)["input_ids"])
    distances, indices = index.search(query_embedding.detach().cpu().numpy(), top_k)
    return indices
