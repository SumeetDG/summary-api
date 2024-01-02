import openai
key_1="api_key_1"
key_2="api_key_2"
summarized_list=[]
def summarizer(text):
    if text=="" or text==" ":
        return text

    try:
        openai.api_key=key_1
        response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "system", "content": f"Summarize the given text such that output remains coherent,readable and retain important information and keywords {text}"}]
        )
        return response["choices"][0]["message"]["content"]

    except:
        openai.api_key=key_2
        response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "system", "content": f"Summarize the given text such that output remains coherent,readable and retain important information and keywords {text}"}]
        )
        return response["choices"][0]["message"]["content"]
def Summarize(word_list):
    for i in word_list:
        summarized_list.append(summarizer(i))
    return summarized_list