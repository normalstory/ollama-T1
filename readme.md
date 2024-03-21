# 1. Urls Embedding #
* framework : ollama 
* model 
    * nomic : LLaMA-7B을 fine-tuning한 GPT4All로 비상업적으로만 사용가능
    * mistral : 오픈소스 최강(2023FW기준)

1. 기본 패키지 설치   
   * `pip install langchain langchain-community langchain-core  beautifulsoup4 tiktoken chromadb` 

2. 사용할 모델 추가    
    
   * `ollama pull nomic-embed-text`     
    
   * `ollama pull mistral`    

3. 파이썬 실행     
   * `python3 ui.py` 



# 2. image annotator #   

1. 기본 폴더 구성  

   * `/images` 폴더 생성 후 인식하고자하는 이미지 파일 첨부   

2. 사용할 모델 추가  

   * `ollama pull llava:13b` - llava:7b는 성능이 애매할 수 있다 

3. 파이썬 실행     
   * `python3 ollama_scshot_annotator.py` 
   