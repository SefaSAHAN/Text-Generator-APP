import sys
from PyQt5.QtWidgets import QApplication
from utils.ui import MainWindow
import pandas as pd
import openai

# Configuration for OpenAI API
openai.api_base = "http://localhost:1234/v1"
openai.api_key = "not-needed"

class MainApp(MainWindow):
	def __init__(self):
		super().__init__()
		file_path = 'utils//Feedbacks.xlsx'
		self.df = pd.read_excel(file_path)
		#self.combined_text="..."
		self.dropdown.activated.connect(self.dropdownClicked)
		self.regenerate_button.clicked.connect(self.regenerateResponse)
		self.generate_button.clicked.connect(self.generateResponse)
		self.save_button.clicked.connect(self.saveData)  # Connect save button to saveData method
		#self.dropdownClicked()
		
	
		   
	def create_AIresponse(self, user_input, system_message):
		completion = openai.ChatCompletion.create(
			model="local-model",
			messages=[
				{"role": "system", "content": system_message},
				{"role": "user", "content": user_input}
			],
			temperature=0.7,
		)
		self.resposse_message=(completion.choices[0].message.content)
		self.response_text.setPlainText(self.resposse_message)
		

	def dropdownClicked(self):
		current_index = self.dropdown.currentIndex()
		excel_column_text = list(self.df.iloc[:, current_index])

		# Create a string variable to hold the combined text
		self.combined_text = "\n".join(excel_column_text)

		# Add the summary text
		entry_text = ""
		if current_index == 0:
			entry_text = "\nThese are the feedbacks about John from his coworkers."
		elif current_index == 1:
			entry_text = "\nThese feedbacks are potential improvements that John can make according to his coworkers."
		elif current_index == 2:
			entry_text = "\nThese are the tips and advices shared with John by his coworkers."

		# Append the summary text to the combined text
		self.combined_text = entry_text + self.combined_text

		# Add the additional text at the end
		self.additional_text = "\nCan you please summarize these feedbacks in detail?"
		self.create_AIresponse(self.additional_text, self.combined_text)

		# Set the combined text to the input text area
		self.input_text.setPlainText(self.combined_text)
		
	
		
	def regenerateResponse(self):
		self.create_AIresponse(self.additional_text, self.combined_text)
		
	def generateResponse(self):
		# Generate response based on the current input text
		input_text = self.input_text.toPlainText()
		self.create_AIresponse(input_text, self.combined_text)
		
		
	def saveData(self):
		try:
			# Try to read the existing Excel file
			existing_data = pd.read_excel('feedback_data.xlsx')
			# Append new data to the existing file
			new_data = pd.DataFrame({
				'Dropdown Selection': [self.dropdown.currentText()],
				'Input Text': [self.input_text.toPlainText()],
				'Response': [self.resposse_message]
			})
			existing_data = pd.concat([existing_data, new_data], ignore_index=True)
			print(existing_data)
			# Write the updated data back to the Excel file
			existing_data.to_excel('feedback_data.xlsx', index=False)
		except FileNotFoundError:
			# If the file doesn't exist, create a new Excel file
			data = {
				'Dropdown Selection': [self.dropdown.currentText()],
				'Input Text': [self.input_text.toPlainText()],
				'Response': [self.resposse_message]
			}
			df = pd.DataFrame(data)
			df.to_excel('feedback_data.xlsx', index=False)

if __name__ == "__main__":
	app = QApplication(sys.argv)
	window = MainApp()
	window.show()
	sys.exit(app.exec_())
