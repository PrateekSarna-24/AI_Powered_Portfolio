from langchain.prompts import load_prompt
from langchain_core.messages import SystemMessage, HumanMessage
from langchain_together import ChatTogether
from pydantic import BaseModel, Field
from typing import Annotated
from fastapi import FastAPI, Query, HTTPException
from fastapi.responses import JSONResponse
from dotenv import load_dotenv
import os
import torch

load_dotenv()

template = load_prompt("D:/AI_Powered_Portfolio/Backend/portfolio_template.json")


model = ChatTogether(
    model="openai/gpt-oss-20b",
    max_tokens=100
)


class UserPrompt(BaseModel) :
    
    user_query : Annotated[str, Field(..., description="Ask anything to learn about Prateek Sarna's skillset and talent", examples=["Summarize portfolio.", "What Projects has he worked on.", "List the skillset of this person"])]

app = FastAPI()

@app.get("/")
def root() :
    return JSONResponse(status_code=200, content={"message": "Welcome to Prateek Sarna Portfolio Root"})

@app.post("/invoke")
def invoke_query(user_prompt : UserPrompt) :
    user_query = user_prompt.user_query
    chatHistory = [
        SystemMessage(content = template.template),
        HumanMessage(content = user_query)
    ]
    try :
        result=model.invoke(chatHistory)

        return JSONResponse(status_code=201, content={"response" : result.content})

    except Exception as e:
        
        raise HTTPException(status_code=503, detail="No API tokens left :(")
    