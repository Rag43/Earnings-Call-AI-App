from llama_index.core import SimpleDirectoryReader, VectorStoreIndex, StorageContext, load_index_from_storage
import os

TRANSCRIPTS_DIR = "app/data/transcripts"
PERSIST_DIR = "app/data/index"

def build_index():
    print("📚 Loading transcripts...")
    documents = SimpleDirectoryReader(TRANSCRIPTS_DIR).load_data()

    print("🔍 Building index...")
    index = VectorStoreIndex.from_documents(documents)
    index.storage_context.persist(persist_dir=PERSIST_DIR)

    print(f"✅ Index saved to {PERSIST_DIR}")
    return index

def load_index():
    if not os.path.exists(PERSIST_DIR):
        raise ValueError("❌ Index not found. Please run build_index() first.")
    
    print("📦 Loading index from storage...")
    storage_context = StorageContext.from_defaults(persist_dir=PERSIST_DIR)
    return load_index_from_storage(storage_context)
