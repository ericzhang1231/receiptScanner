import dspy
import os

def main():
    apiKey = os.environ['OPENAI_API_KEY']
    print(apiKey)
    lm = dspy.LM('openai/gpt-4o-mini')
    dspy.configure(lm=lm)

if __name__ == "__main__":
    main()