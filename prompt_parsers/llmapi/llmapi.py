from google import genai


def cal_gemini_llm(model, api):
    # Define LLM model
    client = genai.Client(api_key=api)
    chat = client.chats.create(model=model)
    return client, chat


class LlmApiCalling:
    def __init__(self):
        self.api_dict = {"gemini-2.0-flash": "AIzaSyCaHjMpBgDv_ZcfCXje5JEWzoU00Yxe0g8"}

    def help(self) -> None:
        valid_api = "value 0: Gemini 2-0-flash API"
        print(f"Available APIs:\n{valid_api}")

    def choose_api(self, what_llm: int = 0, custom_api: str | None = None):

        # Make sure param 'what_llm' is an integer number
        notice1 = (
            "'what_llm' must be an integer, call 'help' method to get "
            "more information about valid apis!"
        )
        assert isinstance(what_llm, int), notice1

        # Make sure value of param 'what_llm' is valid
        notice2 = (
            f"Valid values of param 'what_llm' are:\n"
            f"{list(range(len(self.api_dict)))}"
        )
        assert what_llm in list(range(len(self.api_dict))), notice2

        # Switch case
        if what_llm == 0:
            try:
                if custom_api is None:
                    api = list(self.api_dict.values())[what_llm]
                else:
                    api = self.api_dict[custom_api]
                return cal_gemini_llm(
                    model=list(self.api_dict.keys())[what_llm], api=api
                )
            except:
                raise ValueError("Check again your API key!")

        raise NotImplementedError("Not implemented for other LLMs")
