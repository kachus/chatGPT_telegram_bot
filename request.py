import openai

def askGPT(text):
    openai.api_key = "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"
    response = openai.Completion.create(
        engine = "text-davinci-003",
        prompt = text,
        temperature=0.6,
        max_tokens = 500,

    )
    return print(response.choices[0].text)

def main():
    while True:
        print('GPT: ask me a question \n')
        myQn = input()
        askGPT(myQn)
main()