class ValidString:
    def validate(self, strings: str):
        stack = []
        hashmap = {
                "(": {"state": "open", "match": ")"},
                "[": {"state": "open", "match": "]"},
                "{": {"state": "open", "match": "}"},
                ")": {"state": "closed", "match": "("},
                "]": {"state": "closed", "match": "["},
                "}": {"state": "closed", "match": "{"},
        }

        for index, string in enumerate(list(strings)):
            hash_string = hashmap[string]
            if hash_string["state"] == "open":
                stack.append(string)
            elif hash_string["state"] == "closed":
                if not stack:
                    return False

                last_hash_string = hashmap[stack[-1]]
                last_hash_string_state = last_hash_string["state"]
                last_hash_string_match = last_hash_string["match"]
                if last_hash_string_state == "open" and string == last_hash_string_match:
                    stack.pop()

        return not stack


strings = "(())"
valid_string = ValidString()
result = valid_string.validate(strings)
print(result)