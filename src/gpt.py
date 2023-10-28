import os
import sys
import constants

from langchain.document_loaders import TextLoader
from langchain.document_loaders import DirectoryLoader
from langchain.indexes import VectorstoreIndexCreator
from langchain.llms import OpenAI
from langchain.chat_models import ChatOpenAI

os.environ["OPENAI_API_KEY"] = constants.API_KEY 


def print_chat_completion(vid_id):
  query = input()
  # print(query)
  path = "data/" + vid_id
  loader = TextLoader(path)
  # loader = DirectoryLoader('./data', glob='*.txt')
  index = VectorstoreIndexCreator().from_loaders([loader])

  print(index.query(query, llm=ChatOpenAI()))
  # print(index.query(query))

