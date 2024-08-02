from transformers import RagTokenizer, RagRetriever, RagSequenceForGeneration

# Initialize RAG model and tokenizer
rag_tokenizer = RagTokenizer.from_pretrained("facebook/rag-sequence-nq")
rag_retriever = RagRetriever.from_pretrained("facebook/rag-sequence-nq", index_name="exact", use_dummy_dataset=True)
rag_model = RagSequenceForGeneration.from_pretrained("facebook/rag-sequence-nq", retriever=rag_retriever)

# Export the model components
__all__ = ['rag_tokenizer', 'rag_model']