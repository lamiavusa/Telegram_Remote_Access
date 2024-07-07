from InquirerPy import prompt
import re

class Config:

    def __init__(self) -> None:
        
        def is_valid_token(token):
            pattern = r"^\d+:[\w-]{35}$"
            match = re.match(pattern, token.strip())
            return bool(match)

        def validate_telegram_user_id(user_id):
            pattern = r"^\d{10}$"
            match = re.match(pattern, user_id.strip())
            return bool(match)
        
        self.questions = [
            {
                "type": "input",
                "name": "TOKEN",
                "message": "BOT TOKEN",
                "validate": lambda x: is_valid_token(x)
                
            },  
            {
                "type": "input",
                "name": "MY_USER_ID",
                "message": "USER_ID",
                "validate": lambda x: validate_telegram_user_id(x)

            },
        ]

    def get_config(self) -> dict:
        return prompt(
            questions=self.questions,
            style={
                "questionmark": "#2DFF03 bold",
                "selected": "#FF03E4",
                "answer": "#FF03E4 bold",
                "question": "",
            },
        )
