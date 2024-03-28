import openai
import pandas as pd
from utils.read_excel import ExcelTranslator
from utils.send_email import EmailSender
from docx import Document

# Configuration for OpenAI API
openai.api_base = "http://localhost:1234/v1"
openai.api_key = "not-needed"

class FeedbackProcessor:
    def __init__(self):
        self.translator = ExcelTranslator()
        self.feedback_owner=""
        self.feedback_owner_email=""

    def extract_feedback(self, selection_index):
        feedback_text = self.translator.translate_column(selection_index)

        feedback_owner_list=self.translator.extract_name(selection_index)
        # print(feedback_owner_list)

        self.feedback_owner=feedback_owner_list[0]
        self.feedback_owner_email=feedback_owner_list[1]
          
        return feedback_text


    def generate_response(self, input_text):
        completion = openai.ChatCompletion.create(
            model="local-model",
            messages=[
                {"role": "user", "content": input_text}
            ],
            temperature=0.3,
        )
        return completion.choices[0].message.content
    

# def write_to_word(text, filename):
#     doc = Document()
#     doc.add_paragraph(text)
#     doc.save(f"output\\{filename}.docx")
#     print(f"Text written to {filename}.docx")

def main():
   
    feedback_processor = FeedbackProcessor()
    email_sender = EmailSender()
    for selection_index in range(3):
        if selection_index % 3 == 0:
            final_text = ""
            response = feedback_processor.extract_feedback(selection_index)
            final_text += response
        elif selection_index % 3 == 1:
            response = feedback_processor.extract_feedback(selection_index)
            final_text += response
        else:
            response = feedback_processor.extract_feedback(selection_index)
            final_text += response
            feedback_owner = feedback_processor.feedback_owner
            email_adres=feedback_processor.feedback_owner_email
            print(feedback_owner, email_adres)
            
            starting_text=f"""Dear {feedback_owner}, We hope this message finds you in good health and high spirits. We are reaching out to share your recent feedback analysis with you. Our AI Feedback App utilizes advanced Language Model (LLM) for comprehensive analysis and sends automatic email notifications directly to you. Your feedback remains confidential, and we take great care to ensure its privacy. If you have any questions or concerns about the feedback, please do not hesitate to reach out to us"""
            
            ending_text="""Follow up action: Please decide with whom you would like to share and discuss the feedback(counselor or Marco) and schedule a meeting.We look forward to continuing our collaboration and supporting your growth and development within the team. \n\nBest regards,\nAI Feedback Team"""

            final_text = f"""These are the feedbacks texts from colleagues for {feedback_owner}.""" + final_text + f""" I want you to create a proper detailed new mail text by using this feedback text. The prepared text should not contain company names, project names, personal names and similar special names. Structure the text in two categories: strenghts and weaknesses. Here are my starting text : '{starting_text}' and end the mail:'{ending_text}'"""
            
            final_response = feedback_processor.generate_response(final_text)

            subject=F"Feedback analyze for {feedback_owner}"

            # Send the email
            email_sender.send_email(email_adres, subject, final_response)
            print('Email sent successfully!')

            # write_to_word(final_response,feedback_owner)



if __name__ == "__main__":
    main()
