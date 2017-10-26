import wikipedia
search_input = input('Enter a page title or search phrase:')
while search_input !='':
    try:
        error = 0
        summary = wikipedia.summary(search_input)
    except wikipedia.exceptions.DisambiguationError as e:
        print (e.options)
        error = 1
    if error ==0:
        page_input=wikipedia.page(search_input)
        print(page_input.title)
        print(wikipedia.summary(search_input))
        print(page_input.url)
    search_input = input('Enter a page title or search phrase')