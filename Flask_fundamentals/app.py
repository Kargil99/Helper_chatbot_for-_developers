from flask import Flask

'''
It will create an instance of the flask class.
This instance will be our WSGI(web server gateway interface)for the application.
'''
#WSGI Application
app = Flask(__name__)

@app.route("/")
def welcome():
    return "Welcome Home Legend. You did a super work....!!"


'''(rule: str, **options: Any) -> ((T_route@route) -> T_route@route)
rule
The URL rule string.
Decorate a view function to register it with the given URL rule and options. Calls add_url_rule, which has more details about the implementation.

    @app.route("/")
    def index():
        return "Hello, World!"

See url-route-registrations.
The endpoint name for the route defaults to the name of the view function if the endpoint parameter isn't passed.
The methods parameter defaults to ["GET"]. HEAD and OPTIONS are added automatically.
Parameters
rule
The URL rule string.
options
Extra options passed to the ~werkzeug.routing.Rule object.
'''





if __name__ == "__main__":
    app.run()



'''
(method) def run(
    host: str | None = None,
    port: int | None = None,
    debug: bool | None = None,
    load_dotenv: bool = True,
    **options: Any
) -> None
'''