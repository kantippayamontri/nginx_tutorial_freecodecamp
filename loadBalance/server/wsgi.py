from flask_app import create_app
app = create_app(servername=3) 

if __name__ == "__main__":
    app.run(port=8000, host="0.0.0.0")

