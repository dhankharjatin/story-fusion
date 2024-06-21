from flask import Flask,render_template,request,url_for
from flask_sqlalchemy import SQLAlchemy



app=Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///sample.sqlite3"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

class Story(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    story = db.Column(db.String)

    def __init__(self, story):
        self.story = story

input_list=[]
        
@app.route("/")
def main():
    return render_template("index.html")





@app.route("/fiction")
def fiction():
    fiction="Once upon a time, in a quaint village nestled at the edge of a dense forest, there lived a young girl named Lily. She was known for her curious nature and adventurous spirit, always seeking new experiences beyond the boundaries of her familiar surroundings.One bright morning, as the sun painted the sky with hues of gold and pink, Lily decided to explore the mysterious forest that had always intrigued her.\n The villagers often spoke of the forest in hushed tones, sharing tales of ancient magic, mythical creatures, and hidden treasures that lay deep within its enchanted depths.With a sense of excitement tinged with apprehension, Lily packed a small bag with provisions, a map she had drawn herself, and a journal to document her discoveries. She set off on her journey, her heart pounding with anticipation as she ventured into the unknown"
    return render_template("writing.html",prompt=fiction,title="The Enchanted Forest")

@app.route("/scifi")
def scifi():
    scifi="The day had arrived, marked by the alignment of Arkanis' twin moons in the indigo sky. In a modest dwelling nestled amidst the ancient woods, a young woman named Alara stirred from her slumber. Her eyes, the color of sapphire, reflected the pre-dawn light filtering through the canopy of towering trees.Alara was not like others of her kind.\n From a young age, she had felt a deep connection to the unseen forces that governed the universe. Dreams of distant galaxies and celestial harmonies often visited her sleep, leaving behind a lingering sense of purpose yet to be unveiled.As she rose from her bed, the air seemed charged with anticipation, as if the very essence of Arkanis awaited her awakening. Outside, the forest murmured with the awakening of life, and a gentle breeze carried whispers of forgotten lore.\nWith a sense of quiet determination, Alara dressed in garments woven from the fibers of ancient vines, adorned with symbols of constellations long extinct. Her bare feet touched the earth with reverence, as if each step resonated with the echoes of cosmic melodies.Guided by an inner calling, Alara ventured deeper into the woods, following a path only she could perceive. The trees whispered secrets of the past and prophecies of the future, weaving a tapestry of knowledge around her."
    return render_template("writing.html",prompt=scifi,title="Echoes of Eternity")

@app.route("/horror")
def horror():
    horror="The air was thick with an unsettling silence as the moon cast an eerie glow upon the Whispering Woods. Sarah, a young journalist with a passion for unraveling mysteries, found herself standing at the edge of this infamous forest. Tales of inexplicable occurrences and vanishing travelers had shrouded the woods in a cloak of fear for generations.\nIgnoring the warnings echoing in her mind, Sarah took a tentative step forward, her curiosity overpowering any sense of apprehension. The trees seemed to lean closer, their twisted branches reaching out like skeletal fingers. As she ventured deeper, the forest enveloped her in an oppressive darkness, broken only by sporadic beams of moonlight.\nA soft whispering sound began to fill the air, barely audible at first but growing in intensity with each passing moment. It was as if the very essence of the woods was murmuring secrets, secrets that beckoned Sarah to uncover their truth. She pressed on, her heart pounding in anticipation and fear intertwining."
    return render_template("writing.html",prompt=horror,title="The Whispering Woods")

@app.route("/mystery")
def mystery():
    mystery="The rain pounded against the windows of Detective Jackson's office, casting shadows that danced ominously across the dimly lit room. Jackson sat at his desk, his eyes fixed on the ancient pocket watch resting in his hand. It was a curious heirloom, passed down through generations in his family, each whispering tales of secrets it held.As the clock struck midnight, a knock interrupted the silence. Jackson glanced up to see his assistant, Emma, enter with a letter in hand. Her expression hinted at both intrigue and concern."
    return render_template("writing.html",prompt=mystery,title="The Enigmatic Heirloom")





@app.route("/display", methods=["GET", "POST"])
def display():
    if request.method == "POST":
        input_text = request.form["story_input"]

        input_list.append(input_text)
        

        to_add = Story(input_text)
        db.session.add(to_add)
        db.session.commit()

        fiction="Once upon a time, in a quaint village nestled at the edge of a dense forest, there lived a young girl named Lily. She was known for her curious nature and adventurous spirit, always seeking new experiences beyond the boundaries of her familiar surroundings.One bright morning, as the sun painted the sky with hues of gold and pink, Lily decided to explore the mysterious forest that had always intrigued her.\n The villagers often spoke of the forest in hushed tones, sharing tales of ancient magic, mythical creatures, and hidden treasures that lay deep within its enchanted depths.With a sense of excitement tinged with apprehension, Lily packed a small bag with provisions, a map she had drawn herself, and a journal to document her discoveries. She set off on her journey, her heart pounding with anticipation as she ventured into the unknown"
    

        return render_template("display.html",input_text=input_list,prompt=fiction,title="The Enchanted Forest")

    else :
        return render_template("writing.html")


if __name__=="__main__":
    with app.app_context():
        db.create_all()

    app.run(debug=True)