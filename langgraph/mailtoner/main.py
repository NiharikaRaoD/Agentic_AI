from mail_tone import graph, Email

def main():
    state = Email(
        Draft_Email='I will be out of office from Nov 3rd and will be returning on Nov 10th. I cannot access my emails or messages during this time. Reach out on my mobile xxx-xxx-xxxx if you need anything. If tehre any any critical things, contact my Manager',
        Email_Tone='Formal'
    )
    response = graph.invoke(state)
    print(response['Final_Email'])


if __name__ == "__main__":
    main()
