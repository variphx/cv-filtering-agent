from promptlybot.promptlybot import Graph

if __name__ == '__main__':
    graph = Graph()
    graph.build()
    user_prompt = (
        "I want to employ a person that has at least college degree about "
        "majors relating IT, better if you are AI Engineer. This person must "
        "have more than 2 years experiments and know MVP, Java and Python. "
        "Having Ielts more than 6.5 is advantage."
    )
    result = graph.invoke(user_prompt)
