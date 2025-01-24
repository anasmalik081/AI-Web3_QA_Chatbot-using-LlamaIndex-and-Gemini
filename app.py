import streamlit as st
from QAWithDoc.data_ingestion import load_data
from QAWithDoc.embeddings import download_gemini_embedding
from QAWithDoc.model_api import load_model

    
def main():
    st.set_page_config("AI & Web3 Knowledge Hub: Your Questions Answered")
    
    # doc=st.file_uploader("upload your document")
    
    st.header("Ask Anything About AI and Web3")
    
    user_question= st.text_input("Ask your question")
    
    if st.button("submit & process"):
        with st.spinner("Processing..."):
            document=load_data()
            model=load_model()
            query_engine=download_gemini_embedding(model,document)
                
            response = query_engine.query(user_question)
                
            st.write(response.response)
                
                
if __name__=="__main__":
    main()      