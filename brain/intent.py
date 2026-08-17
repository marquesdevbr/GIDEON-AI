class Intent:

    def detect(self, text):

        text = text.lower()

        if "abrir" in text:
            return "automation"

        if "pesquise" in text:
            return "search"

        if "lembre" in text:
            return "memory"

        return "conversation"