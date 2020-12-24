from livereload import Server, shell

shell(['python', 'build.py'])()
server = Server()
server.watch('src', shell(['python', 'build.py']))
server.watch('dist')
server.serve(port=8000, root='dist')
