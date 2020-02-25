import General,PersonOrLocation,Chat

words = input('Hi. I am bot. What can I help you with today? \n')
branch = PersonOrLocation.determineBranch(words.split())
Chat.setBranch(branch)
Chat.Chat(words)
while True:
    branch = Chat.getBranch()
    words = input(General.genResponse(branch))
    branch = PersonOrLocation.determineBranch(words)
    Chat.setBranch(branch)
    Chat.Chat(words)