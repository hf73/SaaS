from website import create_app #accesses website file to import create_app from __init__

app = create_app()

if __name__ == '__main__': #if file is ran, not when it is imported, then the website gets ran 
    app.run(debug=True) #anytime a change is done to the code, then the website get rerun (turn off for prod good for dev)

    