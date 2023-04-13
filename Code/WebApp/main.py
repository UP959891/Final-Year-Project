from Website import create_app

app = create_app()

if __name__ == '__main__':
    app.run(debug=True) # in production make this false as it means the webserver is re-started every time there is a change in the python code.
