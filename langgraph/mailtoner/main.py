from dotenv import load_dotenv
import os

def main():
    print(os.getenv('LANGSMITH_TEST_KEY', 'No key found'))
    load_dotenv()
    print(os.getenv('LANGSMITH_TEST_KEY', 'No key found'))


if __name__ == "__main__":
    main()
