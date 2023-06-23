
        # r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f" user said: {query}")

    except Exception as e:
        # print(e)
        print("Say that again please...")
        return "None"
    return query
