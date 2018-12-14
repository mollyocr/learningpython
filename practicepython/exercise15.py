### 2018-12-11 mollyocr
#### practicepython.org exercise 15: reverse word order

## Write a program (using functions!) that asks the user for a long string containing multiple words. Print back to the user the same string, except with the words in backwards order. For example, say I type the string:
# My name is Michele

## Then I would see the following string shown back to me.:
# Michele is name My

def get_string(help_text="Please provide a string: "):
    return str(input(help_text))

# def switcheroo(lovely_sentence):
#
#     # get something
#     flip_me = lovely_sentence
#
#     # chop it up
#     flip_me = flip_me.split(" ")
#
#     # flip it around
#     flip_me = flip_me[::-1]
#
#     # glue it back together
#     flip_me = " ".join(flip_me)
#
#     return flip_me

#### But this is really long and Mike showed me how I can daisy-chain a ton of functions, nested one inside the other -- which, of course I can, because that how I'm calling the functions to run the thing in the first place.

# def switcheroo(lovely_sentence):
#
#     flip_me = " ".join(lovely_sentence.split()[::-1])
#
#     return flip_me

#### And then I looked at the solution and there's an EVEN TIDIER way: just stick it in the return!

def switcheroo(lovely_sentence):
    return " ".join(lovely_sentence.split()[::-1])

print(switcheroo(get_string("Please provide a string, and I'll switcheroo the words for you: ")))

##### Neat and cute, but QUESTION: like, what even is the point of putting it into a function instead of just dropping that line somewhere on its own? 
#### QUESTION: is neat and tidy worth the abstraction away from easily human-parsable? I'd def argue no in such a simple program as this, but the question is probz how fast things run with big stuff. Oo, let's science!

# short_string = "My name is Molly"
#
# long_string = """Lorem ipsum dolor amet excepteur edison bulb af VHS commodo kinfolk raclette portland tofu man bun nulla. In hell of lomo nostrud hexagon. Chia try-hard cillum shabby chic four loko, chicharrones vexillologist drinking vinegar consequat aute. Umami dreamcatcher quinoa brooklyn, celiac pitchfork af tempor pour-over narwhal raclette in. Chartreuse pabst narwhal literally poke vinyl hexagon post-ironic bespoke vegan hell of meggings skateboard vape fanny pack.
#
# Mixtape man braid sunt bushwick. Flannel flexitarian offal hell of aliquip glossier next level schlitz quinoa gluten-free poke raw denim cold-pressed slow-carb. Tacos cornhole laborum, gentrify reprehenderit yr fixie enamel pin tote bag. Taxidermy meggings consectetur skateboard lomo authentic.
#
# Asymmetrical cliche retro 3 wolf moon, everyday carry yuccie magna. You probably haven't heard of them unicorn pariatur, asymmetrical hella iceland ut. Raw denim chillwave keffiyeh narwhal, ennui fashion axe swag nisi drinking vinegar. Mixtape squid swag, air plant fam chicharrones you probably haven't heard of them listicle eu edison bulb sint banh mi food truck. Coloring book selfies messenger bag twee migas taxidermy palo santo cronut kitsch actually incididunt in.
#
# 90's bicycle rights authentic heirloom, aliquip hella quis adipisicing godard. Truffaut laborum lorem 8-bit magna semiotics nulla health goth lomo, flannel dreamcatcher irony plaid meh. Dolore cray dolor photo booth, YOLO franzen veniam magna wolf four loko pariatur duis iceland church-key. Viral VHS duis, af reprehenderit narwhal gochujang messenger bag chartreuse ut. Shoreditch cornhole tousled prism thundercats ethical. YOLO palo santo fugiat 8-bit, banjo dreamcatcher microdosing est.
#
# Kickstarter air plant occupy humblebrag. 8-bit nostrud tousled, cornhole subway tile officia ipsum viral street art squid kickstarter twee sustainable. 90's man braid scenester deserunt. Woke leggings pinterest whatever ut sriracha heirloom intelligentsia. Pitchfork et PBR&B fixie chicharrones, yuccie ea cardigan. Forage tousled ut swag.
#
# Scenester mustache street art man braid beard. Consectetur non wayfarers banh mi. Aesthetic chartreuse ipsum minim proident. Polaroid hella shoreditch you probably haven't heard of them everyday carry typewriter. Ramps vice pinterest, street art small batch tumblr fingerstache pork belly mollit tacos consequat health goth 3 wolf moon occaecat et. Knausgaard single-origin coffee pickled craft beer bitters ex next level XOXO authentic narwhal mumblecore cloud bread tumeric hammock.
#
# Nulla vexillologist brunch unicorn air plant hammock hoodie. Beard butcher keffiyeh yr succulents shabby chic. Vape glossier XOXO cold-pressed bicycle rights, eu next level tbh wolf vaporware yuccie sriracha. Polaroid af pop-up, shoreditch fanny pack beard la croix. Velit kitsch coloring book roof party meditation.
#
# Dreamcatcher helvetica fanny pack aesthetic post-ironic quinoa salvia. Sartorial deep v roof party bitters in hot chicken, fanny pack fam. In celiac pok pok man braid before they sold out four dollar toast, hammock godard listicle small batch proident tumblr duis PBR&B pinterest. Dolore gluten-free taxidermy sint eu.
#
# Fingerstache poke shabby chic truffaut aute. Fingerstache dreamcatcher cupidatat green juice, actually cray selfies in authentic everyday carry tousled. Gochujang swag ugh farm-to-table, edison bulb laborum mixtape echo park ut. Chillwave man braid la croix aliquip, tempor semiotics keffiyeh anim 8-bit esse readymade drinking vinegar.
#
# Food truck ennui retro intelligentsia marfa tempor blue bottle ipsum esse biodiesel williamsburg brunch. Vexillologist small batch green juice dolore, tumblr dreamcatcher polaroid anim yr gentrify sustainable. Shoreditch jianbing celiac commodo, you probably haven't heard of them viral chartreuse pitchfork sunt in kale chips reprehenderit in nisi selvage. Sustainable qui truffaut, pop-up freegan lorem nisi microdosing ea before they sold out irure cardigan. Thundercats aliquip organic, small batch pickled pariatur tofu fashion axe elit heirloom commodo shoreditch man bun. Four dollar toast narwhal tumblr, culpa whatever duis lyft. Snackwave pug nulla knausgaard vice artisan irure try-hard."""
#
# import time
#
# def switcheroo(lovely_sentence):
#     start_nanos = time.perf_counter_ns()
#     flip_me = " ".join(lovely_sentence.split()[::-1])
#     elapsed_time = start_nanos - time.perf_counter_ns()
#     return elapsed_time
#
# print(f"Elapsed time for long_string processing: {switcheroo(long_string)} ns ")
#
# print(f"Elapsed time for short_string processing: {switcheroo(short_string)} ns ")

#### Uh, so cool now I can set up timing experiments but uh it didn't actually test the thing I wanted to test: QUESTION: Is daisy-chaining functions faster than chronological steps inside of a function def? Idk how to put in the timing test inside of one line, lol.
