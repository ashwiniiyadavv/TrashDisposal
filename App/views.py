from django.shortcuts import render
import google.generativeai as genai
api_key = input("Enter your API key: ")
genai.configure(api_key=api_key)
model = genai.GenerativeModel('gemini-1.5-flash',system_instruction="You are an environmentalist and recycling expert")


def generate_response(obj_category:str, obj_type:str) -> str:
    prompt = f""" 
                    We have {obj_category} which is {obj_type},
                    if it can be re-used at home, suggest ideas to recyle as 1. 2. 3.
                    also give ways to dispose it off as 1. 2. 3.,
                    
              """
    response = model.generate_content(prompt)
    print(response.text)
    return response.text

category = input("Enter category of object (eg. bottle): ")
type = input("Enter type of waste (dry, wet, hazardeous): ")

generate_response(category,type)

# Create your views here.
def index (request):
    if request.method=="GET":
        return render(request,'index.html')
    elif request.method=="POST":
        return render(request,'response.html')

