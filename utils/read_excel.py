usr_email={
    'John':'john@john.com',  
}
import pandas as pd
from transformers import MarianMTModel, MarianTokenizer

class ExcelTranslator:
    def __init__(self):
        self.df = pd.read_excel('utils\\Feedbacks.xlsx')
        # Load the pre-trained translation model and tokenizer
        self.model_name = "Helsinki-NLP/opus-mt-nl-en"  # Dutch to English
        self.tokenizer = MarianTokenizer.from_pretrained(self.model_name)
        self.model = MarianMTModel.from_pretrained(self.model_name)

    def translate_to_english(self, text_list):
        # # Tokenize the input text
        # inputs = self.tokenizer(text_list, return_tensors="pt", padding=True, truncation=True, max_length=512, return_attention_mask=False)

        # # Perform translation
        # translated = self.model.generate(**inputs)

        # # Decode the translated text
        # translated_text = self.tokenizer.batch_decode(translated, skip_special_tokens=True)

        result_text='\n '.join(text_list)
        # print(result_text)

        return result_text

    def extract_name(self, column_index):
        # Access the value of the specified cell
        value = self.df.iloc[0, column_index]

        # Extract the last word (excluding the last character, which is '?')
        words = value.split()
        name = words[-1][:-1]
        

        # Assuming usr_email is defined elsewhere
        user_inf = [name, usr_email[name]]

        return user_inf

    def translate_column(self, column_index):
        # Extract the values from the specified column starting from the specified row to the end
        column_text = self.df.iloc[1:, column_index].tolist()

        column_text = [text for text in column_text if pd.notna(text)]

        print("feedback_number",len(column_text))

        # Translate the extracted text to English
        translated_text = self.translate_to_english(column_text)

        return translated_text



# Translator = ExcelTranslator()
# name_list = Translator.extract_name(31)
# print(name_list)
# text = Translator.translate_column(30)
# print("\nApriciated areas:",text)
# text = Translator.translate_column(31)
# print("\n\nAprovement areas:",text)
# text = Translator.translate_column(32)
# print("\n\nTips:",text)
