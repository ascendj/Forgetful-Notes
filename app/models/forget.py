from .base import ObservableModel
import openai
openai.api_key = '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'
import RAKE

class Forget(ObservableModel):
    def __init__(self):
        super().__init__()
        self.auto_forget = False
        self.forget_on = False
        self.revealed = True
        self.reverted = True
        self.original = ""
        self.temperature = 0.7 
        self.max_tokens = 64
        self.mode = "RAKE NLP"

    def on_forget(self, inputted) -> str:
        self.original = inputted
        if self.forget_on and self.revealed and self.reverted:
            self.revealed = False
            self.reverted = False
            self.original = inputted

            if self.mode == "RAKE NLP":
                rake = RAKE.Rake(RAKE.SmartStopList())
                top_keywords = rake.run(self.original, maxWords=1)

                modified_text = self.original

                for keyword, _ in top_keywords:
                    modified_text = modified_text.replace(keyword, '␣', 1)

                self.modified = modified_text
                return modified_text

            elif self.mode == "GPT-3.5 Blanks":
                self.prompt_blankwords = f"Omit key words and symbols in \n{self.original}, target key words and symbols, to create a fill-in-the-blanks exercise:"
                self.response_bw = openai.ChatCompletion.create(
                    model="gpt-3.5-turbo",
                    messages=[
                        {"role": "system", "content": "You are a teacher who is"
                                "creating a memory game to test a student's understanding of the topic"
                                "You will pick out key terminology and definitions and omit them"
                                "You will replace the key words with the word table"
                                "Ignore stop words, do not remove words which have little meaning"
                                "Preserve markdown formatting"
                                "Do not remove markdown formatting, remove only important terminology or definitions"
                                "Each omitted word must be replaced by a single ␣"
                                "For example: 'The quick brown fox jumps over the lazy dog' becomes 'The ␣ brown ␣ jumps over the ␣ ␣'"
                                },
                        {"role": "user", "content": self.prompt_blankwords}
                    ],
                    temperature=self.temperature,
                    max_tokens= 300
                )
                self.modified = self.response_bw['choices'][0]['message']['content']
                return self.modified
            
            elif self.mode == "GPT-3.5 Incorrects":
                self.prompt_changemeaning = f"Sabotage the content in \n{self.original}, change key words and symbols, make some of them incorrect:"
                self.response_cm = openai.ChatCompletion.create(
                    model="gpt-3.5-turbo",
                    messages=[
                        {"role": "system", "content": "You are a sneaky teacher"
                                "who is trying to sabotage students' notes"
                                "Change some key terminology or definitions to be wrong"
                                "Some modified statements are now incorrect"
                                "You target the changing of keywords and key symbols of their notes and ignore stop words"
                                "Try not to make the changes obvious"
                                },
                        {"role": "user", "content": self.prompt_changemeaning}
                    ],
                    temperature=self.temperature,
                    max_tokens= 300
                )
                self.modified = self.response_cm['choices'][0]['message']['content']
                return self.modified

    def on_reveal(self, inputted) -> str:
        original_paragraph = self.original
        modified_paragraph = self.modified

        # Split the paragraphs into lines
        original_lines = original_paragraph.splitlines()
        modified_lines = modified_paragraph.splitlines()

        # Iterate through the lines and identify changes
        highlighted_lines = []
        for original_line, modified_line in zip(original_lines, modified_lines):
            original_words = original_line.split()
            modified_words = modified_line.split()

            # Iterate through the words and identify changes
            highlighted_words = []
            for original_word, modified_word in zip(original_words, modified_words):
                if original_word != modified_word:
                    highlighted_word = f"[{original_word}]"
                else:
                    highlighted_word = original_word
                highlighted_words.append(highlighted_word)

            # Join the highlighted words back into a line
            highlighted_line = " ".join(highlighted_words)
            highlighted_lines.append(highlighted_line)

        # Join the highlighted lines back into a paragraph
        revealed = "\n".join(highlighted_lines)

        return revealed

    
    def on_revert(self) -> str:
        return self.original
