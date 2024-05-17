 Flowise, iniciar:
            - Acessar instruções no GitHub: https://github.com/FlowiseAI/Flowise
            - Em "Quick Start", seguir passos para abrir a ferramenta no computador.
            - Carregar o chatflow:
                   - necessário ter o arquivo "MedicalAI Chatflow.json" no computador.
                   - no Flowise, em "chatflows", clicar em "+ ADD NEW",
                   - na página que se abriu, clicar em "settings" e em "Load Chatflow", carregando o "MedicalAI Chatflow.json".
            - Inicialmente foram criadas credenciais para uso dos módulos que compoem o chatflow, mas se houver necessidade de novas ou 
              recriá-las,seguir o seguinte:
                   -selecionar "Credentials" e "+ Add Credential" para criar credenciais para uso de módulos que exigem credenciais:
                   - selecionar fabricante, conforme módulo a ser usado e criar um nome de livre escolha para a credencial e
                     copiar e colar a "Api Key" correspondente, obtida diretamente nos sites dos fabricantes (nesse caso, OpenAI, 
                     HuggingFace e Pinecone).
                   - quando for montar o chatflow, colar o "nome" da credencial nos módulos em "connect Credential".
                   - no site do Pinecone, além de obter a Api Key, criar um "índice" para armazenar os vetores do carregamento de documentos,
                     e inserir o nome do índice nos módulos Pinecone em "Pinecone Index".
            - Os módulos de carregamento de documentos precisam ser conectados entre si e aos demais módulos para funcionarem:

                                                        Pdf File -------------|              ChatHuggingFace --------------|
                    Recursive Character Text Splitter -----|       Pinecone Upsert Document ------------- Conversational Retrievel QA Chain
                                                        Text File ------------|      |       BufferMemory -----------------|
                                                              OpenAI Embeddings -----|

            - Após carregamento dos documentos, para não repetir o carregamento a cada interação no chat, mudar as ligações dos módulos:

                                                       ChatHuggingFace ----------------------|
                    OpenAI Embeddings ----- Pinecone Load Existing Index ----- Conversational Retrievel QA Chain
                                                       BufferMemory -------------------------|

            - Para testar o modelo, após alterações, se houver, salvá-las antes de abrir o "chat".

