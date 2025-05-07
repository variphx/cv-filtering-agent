from .promptform import Form
from .messages import MessagesOfAgent
from .llmapi import LlmApiCalling
from .messages.insidetools import format_title_message, format_message

# from IPython.display import Image, display
from langgraph.graph import MessagesState, StateGraph, START, END


class Graph:
    def __init__(self):

        # LLM API
        self.client, self.chat = LlmApiCalling().choose_api()

        # Messages
        self.messages_name = ['human', 'system', 'bot']
        self.human_message, self.system_message, self.bot_message = (
            MessagesOfAgent(
                messages=self.messages_name
            ).create_messages()
        )

        # Graph is built?
        self.is_built = False

    def __create_fullform_NODE(self, state: MessagesState):
        # create a json form
        fullform = Form().create_json()

        print(state['messages'])
        # Set up system prompt
        system_prompt = (
            f"Analyze the requirement: \"{state['messages'][0].content}\","
            f"then fill received form below (just keywords):\n{fullform}"
        )
        return {"messages": [self.system_message(content=system_prompt)]}

    # Create nodes
    def __use_gemini_llm_NODE(self, state: MessagesState):
        response = self.chat.send_message(
            state['messages'][0].content + state['messages'][1].content
        )
        return {"messages": [self.bot_message(content=response.text[8:-4])]}

    # Build graph
    def build(self):
        # Create builder
        builder = StateGraph(MessagesState)

        # Add node
        builder.add_node(
            "create_fullform_NODE",
            action=self.__create_fullform_NODE
        )
        builder.add_node(
            "use_gemini_llm_NODE",
            action=self.__use_gemini_llm_NODE
        )

        # Add edge
        builder.add_edge(START, "create_fullform_NODE")
        builder.add_edge("create_fullform_NODE",
                         "use_gemini_llm_NODE")
        builder.add_edge("use_gemini_llm_NODE", END)

        # Compile
        self.graph = builder.compile()

        # Set is_built is True
        self.is_built = True

    def invoke(self, your_prompt: str) -> str:
        if self.is_built:
            result = self.graph.invoke({
                "messages": [self.human_message(content=your_prompt)]
            })
            for message_name, message_content in zip(
                self.messages_name,
                result['messages']
            ):
                print(format_title_message(message_name))
                print(format_message(message_content.content))
            # for message_name, message in [self.messages_name, result]:
            #     print(format_title_message(message_name))
            #     print(format_message(message.content))
            return result['messages'][-1].content

        else:
            print("Your must build GRAPH first by using 'build' method.")
            return None
