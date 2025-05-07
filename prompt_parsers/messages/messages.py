from pydantic import Field
from typing import Type, List, Literal
from langchain_core.messages import BaseMessage


class MessageInterface:
    def __init__(self):
        pass

    def build_message(
        self,
        message_name: str = "my_message"
    ) -> Type[BaseMessage]:

        # Make sure message_name is a string
        notice = "'message_name' variable must be a string"
        assert isinstance(message_name, str), notice

        # Create Message
        class Message(BaseMessage):
            type: str = Field(message_name)

            def __init__(self, content: str, **kwargs):
                super().__init__(
                    content=content,
                    **kwargs
                )

            def __repr__(self):
                return f"{message_name.title()}Message(content={self.content})"

        return Message


class MessagesOfAgent:
    def __init__(self, messages: List[str]):
        self.messages = messages
        self.m_interface = MessageInterface()

        # Make sure 'messages' param is a list
        self.__notice1 = "The input musts be a list!"
        assert isinstance(self.messages, list), self.__notice1

        # Make sure all messages inside 'messages' param is a string
        self.__notice2 = "Each message must to be a string!"
        for message in self.messages:
            assert isinstance(message, str), self.__notice2

    def create_messages(self) -> List[Type[BaseMessage]]:
        messages = []
        for message in self.messages:
            messages.append(self.m_interface.build_message(message))
        return messages
