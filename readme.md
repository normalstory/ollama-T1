# Urls Embedding #
* framework : ollama 
* model 
    * nomic : LLaMA-7B을 fine-tuning한 GPT4All로 비상업적으로만 사용가능
    * mistral : 오픈소스 최강(2023FW기준)

1. 기본 패키지 설치   
   * `pip install langchain langchain-community langchain-core  beautifulsoup4 tiktoken chromadb` 

2. 사용한 모델 설치    
    
   * `ollama pull nomic-embed-text`     
    
   * `ollama pull mistral`    

3. 파이썬 실행     
   * `python3 ui.py` 
