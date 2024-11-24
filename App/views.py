from django.shortcuts import render
import google.generativeai as genai
api_key = input("Enter your API key: ")
genai.configure(api_key=api_key)
model = genai.GenerativeModel('gemini-1.5-flash',system_instruction="You are an environmentalist and recycling expert")

def check_recyclable(obj_category:str, obj_type:str) -> str:
    prompt = f""" 
                    We have {obj_category} which is {obj_type},
                    Answer as recylable: Yes or no, 
              """
    response = model.generate_content(prompt)
    print(response.text)
    return "Yes" in response.text 

def suggest(is_recyclable,object):
    # TODO: add country guidelines in the prompt
    action = "recyle and re-use at home" if is_recyclable else "dispose"
    print(action)
    prompt = f"""
                  We have {object}, suggest ways to {action} it as 1. 2. 3.
              """
    response = model.generate_content(prompt)
    print(response.text)
    return response.text

category = input("Enter category of object (eg. bottle): ")
type = input("Enter type of waste (dry, wet, hazardeous): ")
# TODO: also fetch country guidelines for this specific object and then send to the function

is_recylable = check_recyclable(category,type)
suggest(is_recylable,category)