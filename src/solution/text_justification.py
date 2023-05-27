class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        current_width = maxWidth
        text = []
        for word in words:
            word_length = len(word)
            if current_width + word_length + 1 <= maxWidth:
                text[-1].append(word)
                current_width += word_length + 1
            else:
                text.append(list())
                text[-1].append(word)
                current_width = word_length

        output = list()
        for index, line in enumerate(text):
            words_count = len(line)
            line_text = ""
            if index == len(text) - 1 or words_count == 1:
                line_text = " ".join(line)
                line_text += " " * (maxWidth - len(line_text))
            else:
                text_length = sum(len(word) for word in line)
                all_spaces = maxWidth - text_length
                spaces_between, extra_spaces = divmod(all_spaces, words_count - 1)
                for word_index in range(len(line) - 1):
                    spaces = spaces_between + (1 if extra_spaces > 0 else 0)
                    extra_spaces -= 1
                    line_text += line[word_index] + (" " * spaces)

                line_text += line[-1]

            output.append(line_text)

        return output
