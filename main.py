from website import create_app
#create app and run main
app = create_app()

if __name__ == '__main__':
    app.run(ssl_context='adhoc', debug=True)