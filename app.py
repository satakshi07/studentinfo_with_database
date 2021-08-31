from myapp import create_app
import os

config_name=os.getenv('FLASK_CONFIG','development')#Default is 'development' if Flask_config is not set
app=create_app(config_name)



if __name__=="__main__":
    app.run(debug=True)