import google.generativeai as genai
import os

GOOGLE_API_KEY = ""  
genai.configure(api_key=GOOGLE_API_KEY)

# #genterate text from text input

def get_gemini_response(question):
    
    model = genai.GenerativeModel('gemini-pro')
    
    try:
       
        response = model.generate_content(question)
        # for chunk in response:
            # print(chunk.text)
            # print("_" * 80)
        return response.text
    except Exception as e:
        return f"An error occurred: {str(e)}"

def main():
    print("Welcome to Gemini AI Assistant! (Type 'quit' to exit)")
    
    while True:
        
        user_question = input("\nYour question: ")
        
        
        if user_question.lower() in ['quit', 'exit']:
            print("Goodbye!")
            break
            
        
        response = get_gemini_response(user_question)
        print("\nGemini's response:")
        print(response)

if __name__ == "__main__":
    main()

# #generate text from text and image input


# import PIL.Image

# model = genai.GenerativeModel("gemini-1.5-flash")
# organ = PIL.Image.open("wallpaper.jpg")
# response = model.generate_content(["Tell me about this image", organ])
# print(response.text) 

# #build an interactive chat

# def start_gemini_chat():
#     # Initialize the chat model
#     model = genai.GenerativeModel('gemini-pro')
#     chat = model.start_chat(history=[])
    
#     print("Welcome to Gemini AI Chat! (Type 'quit' to exit)")
    
#     while True:
#         user_input = input("\nYou: ").strip()
        
#         if user_input.lower() in ['quit', 'exit']:
#             print("Goodbye!")
#             break
        
#         try:
#             response = chat.send_message(user_input)
#             print("\nGemini:", response.text)
#         except Exception as e:
#             print(f"\nAn error occurred: {str(e)}")

# if __name__ == "__main__":
#     start_gemini_chat()

# #generate response using https urls multiple images

# import os
# import base64
# import httpx

# model = genai.GenerativeModel(model_name = "gemini-1.5-pro")
# image_path_1 = "https://upload.wikimedia.org/wikipedia/commons/4/43/Cute_dog.jpg" 
# image_path_2 = "https://upload.wikimedia.org/wikipedia/commons/f/f9/Phoenicopterus_ruber_in_S%C3%A3o_Paulo_Zoo.jpg"

# image_1 = httpx.get(image_path_1)
# image_2 = httpx.get(image_path_2)

# prompt = "Generate a list of all the objects contained in both images."

# response = model.generate_content([
# {'mime_type':'image/jpg', 'data': base64.b64encode(image_1.content).decode('utf-8')},
# {'mime_type':'image/jpg', 'data': base64.b64encode(image_2.content).decode('utf-8')}, prompt])

# print(response.text)


# #function calling

# # Define the function schema with proper type definitions
# set_light_values_schema = {
#     "name": "set_light_values",
#     "description": "Set the brightness and color temperature of a room light",
#     "parameters": {
#         "type": "object",
#         "properties": {
#             "brightness": {
#                 "type": "integer",
#                 "description": "Light level from 0 to 100. Zero is off and 100 is full brightness"
                
#             },
#             "color_temp": {
#                 "type": "string",
#                 "description": "Color temperature of the light fixture",
#                 "enum": ["daylight", "cool", "warm"]
#             }
#         },
#         "required": ["brightness", "color_temp"]
#     }
# }

# model = genai.GenerativeModel(
#     model_name='gemini-1.5-flash',
#     tools=[{
#         "function_declarations": [set_light_values_schema]
#     }]
# )

# chat = model.start_chat()
# response = chat.send_message('Dim the lights so the room feels cozy and warm.')

# # Add error handling and response processing
# try:
#     if response.candidates:
#         for candidate in response.candidates:
#             if candidate.content.parts:
#                 for part in candidate.content.parts:
#                     if hasattr(part, 'function_call'):
#                         function_call = part.function_call
#                         print(f"Function call: {function_call}")
#                     else:
#                         print(part.text)
#     else:
#         print("No response generated")
# except Exception as e:
#     print(f"Error processing response: {e}")
# print(response.text) #this line gives error


