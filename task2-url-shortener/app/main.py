from __init__ import create_app  # remove the dot

app = create_app()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
